"""
Phase 1: Collect ALL core + tech data
Robust approach with fallbacks for each source
"""

import pandas as pd
import numpy as np
import wbgapi as wb
import requests
from io import StringIO, BytesIO
import os
import json
import re
from datetime import datetime
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "..", "data", "raw")
META_DIR = os.path.join(BASE_DIR, "..", "data", "metadata")
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)

COUNTRIES_WB = ["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]
COUNTRIES_ALL = COUNTRIES_WB + ["TWN"]
YEARS_RANGE = range(2000, 2025)
DOWNLOAD_DATE = datetime.now().strftime("%Y-%m-%d")

source_registry = {}

def log_source(name, url, status, notes=""):
    source_registry[name] = {
        "url": url,
        "download_date": DOWNLOAD_DATE,
        "status": status,
        "notes": notes
    }

# ================================================================
# 1. World Bank WDI
# ================================================================
print("=" * 70)
print("1. WORLD BANK WDI")
print("=" * 70)

wb_indicators = {
    "gdp_pc_ppp": "NY.GDP.PCAP.PP.KD",
    "gdp_real_growth": "NY.GDP.MKTP.KD.ZG",
    "researchers_per_million": "SP.POP.SCIE.RD.P6",
    "scopus_articles": "IP.JRN.ARTC.SC",
    "hitech_export_share": "TX.VAL.TECH.MF.ZS",
    "mva_pct_gdp": "NV.IND.MANF.ZS",
}

wb_all = {}
for var, ind in wb_indicators.items():
    print(f"  {var} ({ind})...", end=" ")
    try:
        raw = wb.data.fetch(ind, economy=";".join(COUNTRIES_WB), time=YEARS_RANGE, skipBlanks=True)
        rows = []
        for item in raw:
            country = item.get("economy", item.get("country", {}).get("id", ""))
            year_str = item.get("date", item.get("time", ""))
            val = item.get("value")
            if year_str and val is not None:
                try:
                    year = int(year_str)
                    rows.append({"country": country, "year": year, var: val})
                except ValueError:
                    pass
        if rows:
            df = pd.DataFrame(rows)
            wb_all[var] = df
            print(f"OK ({len(df)} rows)")
        else:
            print("EMPTY")
    except Exception as e:
        print(f"ERR: {e}")

if wb_all:
    wb_merged = list(wb_all.values())[0]
    for df in list(wb_all.values())[1:]:
        wb_merged = wb_merged.merge(df, on=["country", "year"], how="outer")
    wb_merged = wb_merged.sort_values(["country", "year"]).reset_index(drop=True)
    wb_merged.to_csv(os.path.join(RAW_DIR, "wb_wdi_selected.csv"), index=False)
    print(f"  => Saved wb_wdi_selected.csv: {len(wb_merged)} rows, {len(wb_merged.columns)-2} indicators")
    log_source("wb_wdi", "https://data.worldbank.org/ via wbgapi", "OK",
               f"Indicators: {list(wb_indicators.keys())}; Taiwan not in WB")
else:
    print("  FATAL: No WB data!")
    log_source("wb_wdi", "https://data.worldbank.org/", "FAILED", "wbgapi error")

time.sleep(1)

# ================================================================
# 2. OECD MSTI via SDMX-JSON
# ================================================================
print("\n" + "=" * 70)
print("2. OECD MSTI (GERD, BERD)")
print("=" * 70)

oecd_msti_countries = ["USA", "CHN", "TWN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]
oecd_base = "https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI,1.0/"

oecd_msti_rows = []
for measure in ["GERD_X_GDP", "BERD_X_GDP"]:
    print(f"  {measure}...", end=" ")
    url = f"{oecd_base}ALL.{measure}.....ALL.{'.'.join(oecd_msti_countries)}."
    try:
        resp = requests.get(url, params={
            "startPeriod": "2000",
            "endPeriod": "2024",
            "format": "csvfile",
            "labels": "both"
        }, timeout=60)
        if resp.status_code == 200 and len(resp.content) > 100:
            df = pd.read_csv(StringIO(resp.text))
            time_col = [c for c in df.columns if "TIME_PERIOD" in c or "TIME" in c]
            val_col = [c for c in df.columns if "OBS_VALUE" in c or "value" in c.lower()]
            ref_col = [c for c in df.columns if "REF_AREA" in c or "REF" in c]
            
            if time_col and val_col and ref_col:
                for _, row in df.iterrows():
                    try:
                        year = int(str(row[time_col[0]])[:4])
                        val = float(row[val_col[0]])
                        country = str(row[ref_col[0]])
                        if 2000 <= year <= 2024:
                            oecd_msti_rows.append({
                                "country": country,
                                "year": year,
                                "measure": measure,
                                "value": val
                            })
                    except (ValueError, TypeError):
                        pass
                print(f"OK ({len([r for r in oecd_msti_rows if r['measure']==measure])} rows)")
            else:
                print(f"PARSE FAIL (cols: {list(df.columns)})")
        else:
            print(f"HTTP {resp.status_code} / {len(resp.content)} bytes")
    except Exception as e:
        print(f"ERR: {e}")

if oecd_msti_rows:
    oecd_df = pd.DataFrame(oecd_msti_rows)
    oecd_pivot = oecd_df.pivot_table(
        index=["country", "year"],
        columns="measure",
        values="value"
    ).reset_index()
    oecd_pivot.columns.name = None
    oecd_pivot = oecd_pivot.rename(columns={
        "GERD_X_GDP": "gerd_pct_gdp",
        "BERD_X_GDP": "berd_pct_gdp"
    })
    oecd_pivot.to_csv(os.path.join(RAW_DIR, "oecd_msti.csv"), index=False)
    print(f"  => Saved oecd_msti.csv: {len(oecd_pivot)} rows")
    log_source("oecd_msti", "https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI", "OK",
               "GERD_X_GDP, BERD_X_GDP")
else:
    print("  Trying simplified OECD SDMX endpoint...")
    for measure in ["GERD_X_GDP", "BERD_X_GDP"]:
        print(f"  {measure} (JSON)...", end=" ")
        url = f"https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI,1.0/ALL.{measure}.....ALL.{'.'.join(oecd_msti_countries)}.?startPeriod=2000&endPeriod=2024&format=sdmx-json"
        try:
            resp = requests.get(url, timeout=60)
            if resp.status_code == 200:
                data = resp.json()
                if "dataSets" in data and len(data["dataSets"]) > 0:
                    ds = data["dataSets"][0]
                    obs = ds.get("observations", {})
                    dims = data.get("structure", {}).get("dimensions", {}).get("observation", [])
                    
                    dim_names = [d["id"] for d in dims]
                    dim_values = [d["values"] for d in dims]
                    
                    ref_idx = dim_names.index("REF_AREA") if "REF_AREA" in dim_names else None
                    time_idx = dim_names.index("TIME_PERIOD") if "TIME_PERIOD" in dim_names else None
                    
                    if ref_idx is not None and time_idx is not None:
                        country_vals = [v["id"] for v in dim_values[ref_idx]]
                        time_vals = [v["id"] for v in dim_values[time_idx]]
                        
                        for key_str, obs_data in obs.items():
                            key_parts = key_str.split(":")
                            ci = int(key_parts[ref_idx])
                            ti = int(key_parts[time_idx])
                            country = country_vals[ci] if ci < len(country_vals) else ""
                            year_str = time_vals[ti] if ti < len(time_vals) else ""
                            val = obs_data[0] if obs_data and obs_data[0] is not None else None
                            
                            if val is not None:
                                try:
                                    year = int(year_str[:4])
                                    if 2000 <= year <= 2024:
                                        oecd_msti_rows.append({
                                            "country": country,
                                            "year": year,
                                            "measure": measure,
                                            "value": float(val)
                                        })
                                except (ValueError, TypeError, IndexError):
                                    pass
                        print(f"OK ({len([r for r in oecd_msti_rows if r['measure']==measure])} rows)")
                    else:
                        print(f"DIM MISS: {dim_names}")
                else:
                    print("NO DATA")
            else:
                print(f"HTTP {resp.status_code}")
        except Exception as e:
            print(f"ERR: {e}")
    
    if oecd_msti_rows:
        oecd_df = pd.DataFrame(oecd_msti_rows)
        oecd_pivot = oecd_df.pivot_table(
            index=["country", "year"],
            columns="measure",
            values="value"
        ).reset_index()
        oecd_pivot.columns.name = None
        oecd_pivot = oecd_pivot.rename(columns={
            "GERD_X_GDP": "gerd_pct_gdp",
            "BERD_X_GDP": "berd_pct_gdp"
        })
        oecd_pivot.to_csv(os.path.join(RAW_DIR, "oecd_msti.csv"), index=False)
        print(f"  => Saved oecd_msti.csv: {len(oecd_pivot)} rows")
        log_source("oecd_msti", "OECD SDMX-JSON API", "OK", "GERD_X_GDP, BERD_X_GDP via JSON")
    else:
        print("  FAILED: No OECD MSTI data")
        log_source("oecd_msti", "OECD SDMX API", "FAILED", "Both CSV and JSON failed")

time.sleep(1)

# ================================================================
# 3. Penn World Table 11.0
# ================================================================
print("\n" + "=" * 70)
print("3. PENN WORLD TABLE 11.0")
print("=" * 70)

pwt_urls = [
    "https://www.rug.nl/ggdc/docs/pwt110.xlsx",
    "https://www.rug.nl/ggdc/docs/pwt110.dta",
    "https://www.fecd.org/ggdc/docs/pwt110.xlsx",
]

pwt_df = None
for pwt_url in pwt_urls:
    print(f"  Trying {pwt_url.split('/')[-1]}...", end=" ")
    try:
        resp = requests.get(pwt_url, timeout=120)
        if resp.status_code == 200 and len(resp.content) > 10000:
            ext = pwt_url.split(".")[-1]
            pwt_full = None
            if ext == "xlsx":
                pwt_full = pd.read_excel(BytesIO(resp.content), sheet_name="Data")
            elif ext == "dta":
                pwt_full = pd.read_stata(BytesIO(resp.content))
            
            if pwt_full is None:
                print("PARSE FAIL")
                continue
            
            pwt_cc_col = [c for c in pwt_full.columns if c.lower().startswith("country") or c.lower() == "countrycode" or c == "ccode"]
            pwt_cc = pwt_cc_col[0] if pwt_cc_col else "countrycode"
            
            pwt_vars_needed = ["year", "rgdpe", "pop", "rtfpna", "avh", "rgdpna", "emp"]
            pwt_vars_avail = [c for c in pwt_full.columns if c.lower() in [v.lower() for v in [pwt_cc] + pwt_vars_needed]]
            
            subset = pwt_full[pwt_full[pwt_cc].isin(COUNTRIES_ALL)][pwt_vars_avail].copy()
            subset = subset[subset["year"] >= 2000].copy()
            if "rgdpe" in subset.columns and "pop" in subset.columns:
                subset["gdp_pc_ppp_pwt"] = subset["rgdpe"] / subset["pop"]
            
            subset.to_csv(os.path.join(RAW_DIR, "pwt11_subset.csv"), index=False)
            print(f"OK ({len(subset)} rows, {len(subset.columns)} cols)")
            log_source("pwt11", "https://www.rug.nl/ggdc/productivity/pwt/", "OK",
                       f"Vars: {list(subset.columns)}")
            pwt_df = subset
            break
        else:
            print(f"HTTP {resp.status_code}")
    except Exception as e:
        print(f"ERR: {e}")

if pwt_df is None:
    print("  FAILED: Could not download PWT 11.0")
    log_source("pwt11", "https://www.rug.nl/ggdc/productivity/pwt/", "FAILED", "All URLs failed")

# ================================================================
# 4. WIPO Patent Data via API
# ================================================================
print("\n" + "=" * 70)
print("4. WIPO PATENT DATA (resident applications by origin)")
print("=" * 70)

wipo_codes = {"USA": "US", "CHN": "CN", "TWN": "TW", "KOR": "KR",
              "JPN": "JP", "DEU": "DE", "GBR": "GB", "ISR": "IL", "FRA": "FR"}

wipo_rows = []
for iso3, code in wipo_codes.items():
    print(f"  {iso3} ({code})...", end=" ")
    
    urls_to_try = [
        f"https://www3.wipo.int/ipstats/api/patentData/{code}/origin/resident",
        f"https://www3.wipo.int/ipstats/rest/patentData/{code}/origin/resident",
    ]
    
    got_data = False
    for url in urls_to_try:
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 200:
                try:
                    data = resp.json()
                    if "data" in data:
                        for yr, val in data["data"].items():
                            try:
                                year = int(yr)
                                if 2000 <= year <= 2024 and val is not None:
                                    wipo_rows.append({
                                        "country": iso3,
                                        "year": year,
                                        "patents_resident_origin": int(val)
                                    })
                            except (ValueError, TypeError):
                                pass
                        got_data = True
                        break
                except:
                    pass
        except:
            continue
    
    if got_data:
        print(f"OK ({len([r for r in wipo_rows if r['country']==iso3])} rows)")
    else:
        print("SKIP")

if wipo_rows:
    wipo_df = pd.DataFrame(wipo_rows)
    wipo_df.to_csv(os.path.join(RAW_DIR, "wipo_patents_origin.csv"), index=False)
    print(f"  => Saved wipo_patents_origin.csv: {len(wipo_df)} rows")
    log_source("wipo_patents", "https://www3.wipo.int/ipstats/", "OK",
               "Resident patent applications by applicant origin")
else:
    print("  Trying WIPO bulk download...")
    try:
        wipo_bulk = "https://www.wipo.int/ipstats/en/wipi/assets/data/origin_resident_total.xlsx"
        resp = requests.get(wipo_bulk, timeout=60)
        if resp.status_code == 200 and len(resp.content) > 1000:
            df = pd.read_excel(BytesIO(resp.content))
            print(f"  Bulk download: {len(df)} rows, cols: {list(df.columns)[:10]}")
            
            name_col = [c for c in df.columns if "name" in str(c).lower() or "territory" in str(c).lower() or "economy" in str(c).lower()]
            if name_col:
                for _, row in df.iterrows():
                    name = str(row[name_col[0]]).strip()
                    code_map = {"United States of America": "USA", "China": "CHN", 
                               "Taiwan": "TWN", "Republic of Korea": "KOR", "Japan": "JPN",
                               "Germany": "DEU", "United Kingdom": "GBR", "Israel": "ISR", "France": "FRA"}
                    iso3 = code_map.get(name)
                    if not iso3:
                        code_map2 = {"United States": "USA", "China (mainland)": "CHN", 
                                    "China, Taiwan Province of": "TWN", "Korea, Republic of": "KOR"}
                        iso3 = code_map2.get(name)
                    if iso3:
                        for yr in range(2000, 2025):
                            col_candidates = [c for c in df.columns if str(c).strip() == str(yr)]
                            if col_candidates:
                                val = row[col_candidates[0]]
                                try:
                                    v = int(float(val))
                                    if v > 0:
                                        wipo_rows.append({
                                            "country": iso3,
                                            "year": yr,
                                            "patents_resident_origin": v
                                        })
                                except (ValueError, TypeError):
                                    pass
        
        if wipo_rows:
            wipo_df = pd.DataFrame(wipo_rows)
            wipo_df.to_csv(os.path.join(RAW_DIR, "wipo_patents_origin.csv"), index=False)
            print(f"  => Saved wipo_patents_origin.csv: {len(wipo_df)} rows (from bulk)")
            log_source("wipo_patents", "WIPO WIPI bulk download", "OK", "Bulk Excel from WIPO")
        else:
            print("  FAILED: No patent data extractable")
            log_source("wipo_patents", "WIPO", "FAILED", "API and bulk both failed")
    except Exception as e:
        print(f"  FAILED: {e}")
        log_source("wipo_patents", "WIPO", "FAILED", str(e))

# ================================================================
# 5. OECD Productivity (labour productivity)
# ================================================================
print("\n" + "=" * 70)
print("5. OECD PRODUCTIVITY (GDP per hour worked)")
print("=" * 70)

oecd_prod_url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PDB@DF_PDB_LV,1.0/"
oecd_prod_countries = ["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]

print(f"  GDPHRS for {len(oecd_prod_countries)} countries...", end=" ")
prod_rows = []
try:
    url = f"{oecd_prod_url}ALL.GDPHRS.....ALL.{'.'.join(oecd_prod_countries)}.?startPeriod=2000&endPeriod=2024&format=sdmx-json"
    resp = requests.get(url, timeout=60)
    if resp.status_code == 200:
        data = resp.json()
        if "dataSets" in data and len(data["dataSets"]) > 0:
            ds = data["dataSets"][0]
            obs = ds.get("observations", {})
            dims = data.get("structure", {}).get("dimensions", {}).get("observation", [])
            dim_names = [d["id"] for d in dims]
            dim_values = [d["values"] for d in dims]
            
            ref_idx = dim_names.index("REF_AREA") if "REF_AREA" in dim_names else None
            time_idx = dim_names.index("TIME_PERIOD") if "TIME_PERIOD" in dim_names else None
            
            if ref_idx is not None and time_idx is not None:
                country_vals = [v["id"] for v in dim_values[ref_idx]]
                time_vals = [v["id"] for v in dim_values[time_idx]]
                
                for key_str, obs_data in obs.items():
                    key_parts = key_str.split(":")
                    try:
                        ci = int(key_parts[ref_idx])
                        ti = int(key_parts[time_idx])
                        country = country_vals[ci]
                        year = int(time_vals[ti][:4])
                        val = obs_data[0]
                        if val is not None and 2000 <= year <= 2024:
                            prod_rows.append({
                                "country": country,
                                "year": year,
                                "labour_productivity_gdph": float(val)
                            })
                    except (ValueError, TypeError, IndexError):
                        pass
                
                print(f"OK ({len(prod_rows)} rows)")
            else:
                print(f"DIM MISS: {dim_names}")
        else:
            print("NO DATA")
    else:
        print(f"HTTP {resp.status_code}")
except Exception as e:
    print(f"ERR: {e}")

if prod_rows:
    prod_df = pd.DataFrame(prod_rows)
    prod_df.to_csv(os.path.join(RAW_DIR, "oecd_productivity.csv"), index=False)
    print(f"  => Saved oecd_productivity.csv: {len(prod_df)} rows")
    log_source("oecd_productivity", "OECD Productivity SDMX API", "OK", "GDPHRS")
else:
    print("  No OECD productivity data - will use PWT fallback")
    log_source("oecd_productivity", "OECD Productivity SDMX API", "NO_DATA", "Using PWT fallback")

# ================================================================
# 6. OECD TiVA (GVC foreign VA share)
# ================================================================
print("\n" + "=" * 70)
print("6. OECD TiVA (GVC foreign value added share)")
print("=" * 70)

tiva_url = "https://sdmx.oecd.org/public/rest/data/OECD.STI.PIE,DSD_TIVA@DF_TIVA,1.0/"
tiva_countries = ["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "FRA"]

print(f"  EXGR_FVASH...", end=" ")
tiva_rows = []
try:
    url = f"{tiva_url}ALL.EXGR_FVASH..TOT....ALL.{'.'.join(tiva_countries)}.?startPeriod=2000&endPeriod=2024&format=sdmx-json"
    resp = requests.get(url, timeout=60)
    if resp.status_code == 200:
        data = resp.json()
        if "dataSets" in data and len(data["dataSets"]) > 0:
            ds = data["dataSets"][0]
            obs = ds.get("observations", {})
            dims = data.get("structure", {}).get("dimensions", {}).get("observation", [])
            dim_names = [d["id"] for d in dims]
            dim_values = [d["values"] for d in dims]
            
            ref_idx = dim_names.index("REF_AREA") if "REF_AREA" in dim_names else None
            time_idx = dim_names.index("TIME_PERIOD") if "TIME_PERIOD" in dim_names else None
            
            if ref_idx is not None and time_idx is not None:
                country_vals = [v["id"] for v in dim_values[ref_idx]]
                time_vals = [v["id"] for v in dim_values[time_idx]]
                
                for key_str, obs_data in obs.items():
                    key_parts = key_str.split(":")
                    try:
                        ci = int(key_parts[ref_idx])
                        ti = int(key_parts[time_idx])
                        country = country_vals[ci]
                        year = int(time_vals[ti][:4])
                        val = obs_data[0]
                        if val is not None and 2000 <= year <= 2024:
                            tiva_rows.append({
                                "country": country,
                                "year": year,
                                "gvc_foreign_va_share": float(val)
                            })
                    except (ValueError, TypeError, IndexError):
                        pass
                
                print(f"OK ({len(tiva_rows)} rows)")
            else:
                print(f"DIM MISS: {dim_names}")
        else:
            print("NO DATA")
    else:
        print(f"HTTP {resp.status_code}")
except Exception as e:
    print(f"ERR: {e}")

if tiva_rows:
    tiva_df = pd.DataFrame(tiva_rows)
    tiva_df.to_csv(os.path.join(RAW_DIR, "oecd_tiva.csv"), index=False)
    print(f"  => Saved oecd_tiva.csv: {len(tiva_df)} rows")
    log_source("oecd_tiva", "OECD TiVA SDMX API", "OK", "EXGR_FVASH")
else:
    print("  No TiVA data")
    log_source("oecd_tiva", "OECD TiVA SDMX API", "NO_DATA", "")

# Save source registry so far
with open(os.path.join(META_DIR, "sources_core.json"), "w") as f:
    json.dump(source_registry, f, indent=2)

print("\n" + "=" * 70)
print("CORE DATA COLLECTION COMPLETE")
print(f"Files: {os.listdir(RAW_DIR)}")
print(f"Source registry: {list(source_registry.keys())}")
print("=" * 70)
