#!/usr/bin/env python3
"""Data Quality Reviewer: build reviewed panels (no imputation, fix labels, add totals, flags)."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
OUT = ROOT / "data_reviewed"
TAB = OUT / "tables_reviewed"
FIG = OUT / "figures_reviewed"
OUT.mkdir(exist_ok=True); TAB.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)

COUNTRIES = ["USA","CHN","KOR","JPN","DEU","GBR","ISR","FRA"]
YEARS = list(range(2000,2025))
base = pd.MultiIndex.from_product([COUNTRIES, YEARS], names=["country_iso3","year"]).to_frame(index=False)

def read_series(filename, value_col="value", out_name=None):
    p = RAW / filename
    df = pd.read_csv(p)
    df = df[["country_iso3","year",value_col]].copy()
    df["country_iso3"] = df["country_iso3"].replace({"CN":"CHN","US":"USA","KR":"KOR","JP":"JPN","DE":"DEU","GB":"GBR","IL":"ISR","FR":"FRA"})
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
    df = df[df.country_iso3.isin(COUNTRIES) & df.year.isin(YEARS)].drop_duplicates(["country_iso3","year"])
    return df.rename(columns={value_col: out_name or value_col})

# --- core vars (values unchanged, no imputation) ---
specs = [
    ("gerd_pct_gdp","gerd_pct_gdp.csv","value"),
    ("researchers_per_million","researchers_per_million.csv","value"),
    ("scopus_articles","scopus_articles.csv","value"),
    ("patents_resident","patents_resident.csv","value"),
    ("mva_pct_gdp","mva_pct_gdp.csv","value"),
    ("hitech_export_share","hitech_export_share.csv","value"),
    ("gdp_pc_ppp","gdp_pc_ppp.csv","value"),
    ("tfp_ctfp","pwt_ctfp.csv","ctfp"),
    ("berd_pct_gdp","oecd_berd_pct_gdp.csv","value"),
]
panel = base.copy()
for name, fn, vc in specs:
    s = read_series(fn, vc, name)
    panel = panel.merge(s, on=["country_iso3","year"], how="left", validate="one_to_one")

# --- reliably fixable addition: total office patent filings (resident+nonresident, same office basis, same 2000-2021 coverage) ---
pr = read_series("patents_resident.csv","value","res")
pn = read_series("patents_nonresident.csv","value","nonres")
ptot = pr.merge(pn, on=["country_iso3","year"], how="outer")
ptot["patents_total_office"] = ptot["res"] + ptot["nonres"]
panel = panel.merge(ptot[["country_iso3","year","patents_total_office"]], on=["country_iso3","year"], how="left", validate="one_to_one")
panel.to_csv(OUT / "core_panel_reviewed.csv", index=False)

# --- tech: semi with explicit quarantine flag (legacy one-record rule retained; values unchanged) ---
leg = pd.read_csv(RAW / "comtrade_hs8542_exports.csv")
leg["country_iso3"] = leg.country_iso3.replace({"CN":"CHN"})
# full flag table on base grid restricted to 2010-2023 (response window)
semi_flag = base.copy()
semi_flag = semi_flag[(semi_flag.year>=2010)&(semi_flag.year<=2023)].copy()
key = leg.set_index(["country_iso3","year"])
def flag_row(r):
    if (r.country_iso3, r.year) not in key.index:
        return "missing_no_response"
    rec = key.loc[(r.country_iso3, r.year)]
    if isinstance(rec, pd.DataFrame):
        rec = rec.iloc[0]
    nr = rec["num_records"]
    v = rec["value_usd"]
    if pd.isna(v):
        return "missing_no_response"
    if nr == 1:
        return "retained_one_record"
    return "quarantined_multi_record"
semi_flag["semi_status"] = semi_flag.apply(flag_row, axis=1)
valmap = leg.drop_duplicates(["country_iso3","year"]).set_index(["country_iso3","year"])["value_usd"].to_dict()
semi_flag["semi_exports_hs8542"] = semi_flag.apply(lambda r: valmap.get((r.country_iso3,r.year)) if r.semi_status=="retained_one_record" else np.nan, axis=1)
# HS classification note: legacy file carries no classification column; USA clean pull shows H3(2010-11)/H4(2012-16)/H5(2017-21)/H6(2022-24) breaks.
tech = base.merge(semi_flag[["country_iso3","year","semi_exports_hs8542","semi_status"]], on=["country_iso3","year"], how="left", validate="one_to_one")
for c in ["hpc_top500_systems","hpc_top500_rmax_tflops","ai_publications_count","ai_citations_impact","ai_private_investment_usd_bn","ai_notable_models","quantum_ipf_count","quantum_publications"]:
    tech[c] = np.nan
tech.to_csv(OUT / "tech_panel_reviewed.csv", index=False)
semi_flag.to_csv(TAB / "semi_quarantine_map.csv", index=False)

# --- effective samples for published analyses ---
core = panel.copy()
win = core[(core.year>=2010)&(core.year<=2023)].copy()
rows = []
for v in ["gerd_pct_gdp","berd_pct_gdp","researchers_per_million","scopus_articles","patents_resident","patents_total_office","mva_pct_gdp","hitech_export_share","gdp_pc_ppp","tfp_ctfp"]:
    for c in COUNTRIES:
        s = win[win.country_iso3==c].set_index("year")[v].dropna()
        if len(s):
            rows.append({"var":v,"country":c,"n_2010_2023":len(s),"t0":int(s.index.min()),"t1":int(s.index.max())})
        else:
            rows.append({"var":v,"country":c,"n_2010_2023":0,"t0":None,"t1":None})
pd.DataFrame(rows).to_csv(TAB / "effective_samples_2010_2023.csv", index=False)

# M1 / PCA effective N
est = win[["country_iso3","year","tfp_ctfp","gerd_pct_gdp","researchers_per_million"]].copy()
est["gerd_lag1"] = est.groupby("country_iso3").gerd_pct_gdp.shift(1)
est["lres"] = np.log(est.researchers_per_million)
est1 = est.dropna(subset=["tfp_ctfp","gerd_lag1","lres"])
est1.groupby("country_iso3").size().reset_index(name="M1_n").to_csv(TAB / "model1_effective_n.csv", index=False)
pca = win[["country_iso3","year","gerd_pct_gdp","berd_pct_gdp","researchers_per_million","scopus_articles"]].copy()
pca["lres"]=np.log(pca.researchers_per_million); pca["lart"]=np.log(pca.scopus_articles)
cc = pca.dropna(subset=["gerd_pct_gdp","berd_pct_gdp","lres","lart"])
cc.groupby("country_iso3").size().reset_index(name="PCA_complete_n").to_csv(TAB / "pca_effective_n.csv", index=False)

# --- corrected tables: common-window CAGR + latest-available snapshot ---
def cagr(s0,s1,n):
    return (s1/s0)**(1/n)-1 if s0 and s1 and s0>0 and s1>0 else np.nan
out = []
# common windows chosen as largest balanced window per variable group
windows = {
 "gerd_pct_gdp":(2010,2023),"berd_pct_gdp":(2010,2023),"scopus_articles":(2010,2023),
 "hitech_export_share":(2010,2023),"gdp_pc_ppp":(2010,2023),"tfp_ctfp":(2010,2023),
 "researchers_per_million":(2010,2017),  # balanced: GBR available to 2017; USA to 2022 but common requires 2017
 "patents_resident":(2010,2021),"patents_total_office":(2010,2021),
 "mva_pct_gdp":(2010,2021),  # balanced: USA available to 2021
}
for v,(a,b) in windows.items():
    for c in COUNTRIES:
        s = win[(win.country_iso3==c)&(win.year.isin([a,b]))].set_index("year")[v]
        v0 = s.get(a); v1 = s.get(b)
        out.append({"var":v,"country":c,"t0":a,"t1":b,"v0":v0,"v1":v1,"CAGR_balanced":cagr(v0,v1,b-a) if pd.notna(v0) and pd.notna(v1) else np.nan})
pd.DataFrame(out).to_csv(TAB / "descriptive_cagr_common_window.csv", index=False)

# snapshot at latest JOINTLY available year per variable (US-CHN)
snap = []
for v in ["gerd_pct_gdp","berd_pct_gdp","researchers_per_million","scopus_articles","patents_resident","patents_total_office","mva_pct_gdp","hitech_export_share","gdp_pc_ppp","tfp_ctfp","semi_exports_hs8542"]:
    src = win if v!="semi_exports_hs8542" else win.merge(tech[["country_iso3","year","semi_exports_hs8542"]], on=["country_iso3","year"], how="left", suffixes=("","_t"))
    col = v
    su = src[src.country_iso3=="USA"].set_index("year")[col].dropna()
    sc = src[src.country_iso3=="CHN"].set_index("year")[col].dropna()
    common = sorted(set(su.index) & set(sc.index))
    if common:
        y = max(common)
        a,b = float(su.loc[y]), float(sc.loc[y])
        snap.append({"var":v,"latest_joint_year":y,"USA":a,"CHN":b,"CHN_USA_ratio":b/a if a else np.nan})
    else:
        snap.append({"var":v,"latest_joint_year":None,"USA":np.nan,"CHN":np.nan,"CHN_USA_ratio":np.nan})
pd.DataFrame(snap).to_csv(TAB / "descriptive_snapshot_latest_joint.csv", index=False)

# --- indicator quality reviewed ---
q = pd.DataFrame([
 ["gerd_pct_gdp","VALID WITH CAVEAT","WB WDI GB.XPD.RSDV.GD.ZS (UNESCO-derived), constant-2017-PPP vintage of Sep-2026 pull. 192/200 (missing all-2024). China NBS GDP revisions affect ratio denominator. NOT OECD MSTI; do not mix with OECD BERD as a decomposition."],
 ["researchers_per_million","VALID WITH CAVEAT","WDI SP.POP.SCIE.RD.P6 (UNESCO-UIS). 161/200. ISR 25/25 missing (no WB record); GBR ends 2017 (missing 2018-2024); USA ends 2022; all-2024 missing. Headcount/FTE practice differs by country; per-million denominator favours small populations. M1 n=84, ISR 0, GBR 7; PCA ISR 0."],
 ["scopus_articles","VALID WITH CAVEAT","WDI IP.JRN.ARTC.SC (NSF S&E article volume, fractional counts: decimals observed). 192/200 (missing all-2024). Volume not impact; English/field coverage bias; not AI- or quantum-specific. USA 2022-23 fall (471k->448k->431k) vs CHN rise; treat as volume only."],
 ["patents_resident","VALID WITH CAVEAT","WDI IP.PAT.RESD = resident filings AT the national office (office basis), NOT WIPO origin/inventor basis despite old label. 176/200 (2000-2021; 2022-24 missing all). Counts not quality; CN 2021 subsidy-peak composition. USA nonresidents exceed residents (2021: 329k nonres vs 262k res); resident-only CHN/USA ratio (5.44 in 2021) overstates the office-total gap. See patents_total_office."],
 ["patents_total_office","VALID WITH CAVEAT (new reviewed column)","Reviewed addition: resident+nonresident from the two stored WDI/WIPO office files (perfect 176/176 join, 2000-2021). Total office filings; still counts not quality, still office (not origin) basis. Provided to stop resident-only level comparisons."],
 ["mva_pct_gdp","VALID WITH CAVEAT","WDI NV.IND.MANF.ZS, share of GDP (not absolute scale). 193/200: CHN missing 2000-03, USA missing 2022-24 (raw). USA balanced window ends 2021; published USA-vs-CHN CAGRs over different windows are incomparable - use common 2010-2021 table."],
 ["hitech_export_share","VALID WITH CAVEAT","WDI TX.VAL.TECH.MF.ZS, broad high-tech basket (% mfg exports), series starts 2007 (2000-06 missing all => 144/200). SITC Rev.4 update break + ISR 7.6% (2007)->17.1% (2008)->23.4% (2009) instability: do not treat early years as clean trend; analysis window 2010+ retained with break caveat. Processing-trade bias for CHN."],
 ["gdp_pc_ppp","VALID WITH CAVEAT","WDI NY.GDP.PCAP.PP.KD, constant 2017 intl-$, single Sep-2026 vintage. 200/200 incl. 2024 (treat 2024 as preliminary). Normalization only; do not mix vintages."],
 ["tfp_ctfp","VALID WITH CAVEAT, HEAVILY RESTRICTED","PWT-mirror ctfp, 192/200 (missing all-2024). USA=1.000 every year by construction (verified 1994-2023): USA slope/CAGR=0 is definitional, not a finding. CHN 0.395(2010)->0.471(2023) reads ONLY as gap to contemporaneous frontier. Exclude USA from TFP trend/convergence slopes; pooled FE slopes are identified off non-USA within-variation; year FE absorbs the normalization. Macro TFP, not tech-sector TFP."],
 ["berd_pct_gdp","VALID WITH CAVEAT","OECD MSTI P_BERPCT = BERD PERFORMED as % GDP (not business-FINANCED despite F9 old title). 200/200. Different provider/vintage from WB GERD: ISR BERD>GERD in 2021-23 (e.g. 2023: 6.50>6.35) proves they do not decompose; never compute HERD+=GERD-BERD. No TWN in extraction (by design of 8-country panel)."],
 ["semi_exports_hs8542","VALID WITH CAVEAT, COMPARATOR-INCOMPLETE","UN Comtrade HS8542 nominal USD exports, one-record-retained legacy rule (values unchanged, 75 kept / 125 missing incl. 2000-09 out-of-window). Retained: USA/KOR/JPN/ISR full 2010-23 window (GBR 8: 2010-16+2018), CHN 11 (2015-17 quarantined, 157-170 records), DEU 0 (all multi-record: 10/10/5/6), FRA 0 (no response). Even retained trend spans HS H3/H4/H5/H6 revisions (see USA clean pull: H3 2010-11, H4 2012-16, H5 2017-21, H6 2022-24) + re-export/processing bias. CHN 2012-13 +63%/+63% and KOR 2016-17 +65% spikes retained but flagged. Trade value, not fab capacity. Event pre/post (2020-21 vs 2022-23, n=2/cell, nominal USD, H5->H6 break inside window) is descriptive only. F8 DEU empty line removed in fixed figure."],
 ["hpc_top500_systems","EXCLUDED (MISSING 100%)","No audited country-year extract in workspace (build emits all-NaN). Do not substitute."],
 ["hpc_top500_rmax_tflops","EXCLUDED (MISSING 100%)","Same as above."],
 ["ai_publications_count","EXCLUDED (MISSING 100%)","Stanford HTML folder present but no audited country-year export. Generic article counts must not substitute."],
 ["ai_citations_impact","EXCLUDED (MISSING 100%)","No consistent country-year impact series stored."],
 ["ai_private_investment_usd_bn","EXCLUDED (MISSING 100%)","Proprietary deal coverage + China undercoverage; no verified substitute."],
 ["ai_notable_models","EXCLUDED (MISSING 100%)","Snapshots, not a historical country-year panel."],
 ["quantum_ipf_count","EXCLUDED (MISSING 100%)","EPO-OECD comparable source identified but no chart-digitised extraction performed."],
 ["quantum_publications","EXCLUDED (MISSING 100%)","No audited country-year extract."],
 ["gvc_foreign_va_share / vc_investment","EXCLUDED (NEVER COLLECTED)","Planned in data_map (TiVA/VC) but no raw file and no panel column exists. Must not appear in results."],
], columns=["variable","status","caveat"])
q.to_csv(OUT / "indicator_quality_reviewed.csv", index=False)

# --- data dictionary reviewed ---
d = pd.DataFrame([
 ["gerd_pct_gdp","R&D expenditure (% GDP)","RD","% GDP","World Bank WDI (UNESCO-derived)","GB.XPD.RSDV.GD.ZS","2000-2023 effective (2024 missing)","VALID WITH CAVEAT"],
 ["researchers_per_million","Researchers in R&D","HC","per million people","World Bank WDI / UNESCO UIS","SP.POP.SCIE.RD.P6","2000-2023 eff.; ISR none, GBR to 2017, USA to 2022","VALID WITH CAVEAT"],
 ["scopus_articles","S&E journal articles (fractional-count volume)","S","count (fractional)","World Bank WDI (NSF-derived)","IP.JRN.ARTC.SC","2000-2023 effective","VALID WITH CAVEAT"],
 ["patents_resident","Resident patent applications AT national office (office basis)","INN","count","World Bank WDI / WIPO","IP.PAT.RESD","2000-2021 effective","VALID WITH CAVEAT"],
 ["patents_total_office","Total (resident+nonresident) applications at office","INN","count","WDI/WIPO office files (reviewed sum)","IP.PAT.RESD+IP.PAT.NRES","2000-2021 effective","VALID WITH CAVEAT (reviewed)"],
 ["mva_pct_gdp","Manufacturing value added","PRD","% GDP (share, not scale)","World Bank WDI","NV.IND.MANF.ZS","2000-2021 balanced; CHN from 2004, USA to 2021","VALID WITH CAVEAT"],
 ["hitech_export_share","High-tech exports (broad basket)","ADE","% manufactured exports","World Bank WDI / UN Comtrade","TX.VAL.TECH.MF.ZS","2007-2024 effective; use 2010+ with break caveat","VALID WITH CAVEAT"],
 ["gdp_pc_ppp","GDP per capita, PPP (constant 2017 intl-$; single vintage)","Macro","constant intl $","World Bank WDI","NY.GDP.PCAP.PP.KD","2000-2024 (2024 preliminary)","VALID WITH CAVEAT"],
 ["tfp_ctfp","TFP level relative to contemporaneous USA (=1)","Productivity","index (USA=1/yr)","PWT mirror","ctfp","2000-2023; USA constant","VALID WITH CAVEAT, RESTRICTED"],
 ["berd_pct_gdp","BERD PERFORMED (% GDP; not business-financed)","FIN","% GDP","OECD MSTI","P_BERPCT","2000-2024","VALID WITH CAVEAT"],
 ["semi_exports_hs8542","Integrated-circuit exports, nominal USD (HS8542, mixed revisions)","ADE/PRD","current USD","UN Comtrade (one-record retained)","HS 8542","2010-2023 window; 75 kept","VALID WITH CAVEAT, INCOMPLETE"],
], columns=["variable","label","tci_block","unit","source","source_series","effective_period","comparability_status"])
d.to_csv(OUT / "data_dictionary_reviewed.csv", index=False)
print("reviewed panels built:", panel.shape, tech.shape)
print("M1 n:", len(est1), "PCA n:", len(cc))
