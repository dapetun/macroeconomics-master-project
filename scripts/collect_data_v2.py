#!/usr/bin/env python3
"""Data collection script v2 - using working API endpoints"""

import requests
import pandas as pd
import json
import time
from pathlib import Path
from datetime import datetime

RAW_DIR = Path("data/raw")
METADATA_DIR = Path("data/metadata")

COUNTRIES = ["USA", "CHN", "TWN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]
YEARS = list(range(2000, 2025))

def download_world_bank_direct(indicator, variable_name, description):
    """Download from World Bank using direct HTTP API"""
    print(f"\n{'='*60}")
    print(f"Downloading: {variable_name} ({indicator})")
    print(f"{'='*60}")
    
    countries_str = ";".join(COUNTRIES)
    url = f"https://api.worldbank.org/v2/country/{countries_str}/indicator/{indicator}?date=2000:2024&format=json&per_page=500"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        if len(data) < 2:
            print(f"  [ERROR] No data returned")
            return None
            
        records = []
        for item in data[1]:
            records.append({
                'country_iso3': item['countryiso3code'],
                'year': int(item['date']),
                'value': item['value']
            })
        
        df = pd.DataFrame(records)
        df = df.dropna(subset=['value'])
        
        if len(df) == 0:
            print(f"  [ERROR] All values are null")
            return None
            
        output_file = RAW_DIR / f"{variable_name}.csv"
        df.to_csv(output_file, index=False)
        
        print(f"  [OK] Downloaded {len(df)} observations")
        print(f"  [OK] Saved to {output_file}")
        print(f"  Countries: {sorted(df['country_iso3'].unique())}")
        print(f"  Years: {df['year'].min()}-{df['year'].max()}")
        
        return df
        
    except Exception as e:
        print(f"  [ERROR] {e}")
        return None

def download_oecd_msti():
    """Download OECD MSTI data using alternative endpoint"""
    print(f"\n{'='*60}")
    print(f"Downloading: OECD MSTI (GERD, BERD)")
    print(f"{'='*60}")
    
    # Try OECD SDMX REST API with proper headers
    headers = {
        'Accept': 'text/csv',
        'User-Agent': 'Mozilla/5.0'
    }
    
    indicators = {
        'gerd_pct_gdp': 'GERD',
        'berd_pct_gdp': 'BERD'
    }
    
    results = {}
    
    for var_name, indicator in indicators.items():
        # OECD SDMX URL for MSTI
        url = f"https://stats.oecd.org/SDMX-WS/rest/data/MSTI_ALL/{indicator}.{','.join(COUNTRIES)}../?startTime=2000&endTime=2024"
        
        try:
            response = requests.get(url, headers=headers, timeout=30)
            print(f"  {indicator}: HTTP {response.status_code}")
            
            if response.status_code == 200:
                # Save raw response
                output_file = RAW_DIR / f"{var_name}_raw.csv"
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                print(f"  [OK] Saved raw data to {output_file}")
                results[var_name] = True
            else:
                print(f"  [FAIL] Failed")
                results[var_name] = False
                
        except Exception as e:
            print(f"  [FAIL] Error: {e}")
            results[var_name] = False
        
        time.sleep(1)
    
    return results

def download_pwt():
    """Download Penn World Table 11.0"""
    print(f"\n{'='*60}")
    print(f"Downloading: Penn World Table 11.0")
    print(f"{'='*60}")
    
    # Try multiple possible URLs
    urls = [
        "https://www.rug.nl/ggdc/docs/pwt110.xlsx",
        "https://www.rug.nl/ggdc/docs/pwt110.dta",
        "https://cid.econ.ucdavis.edu/PWT11/pwt110.xlsx",
        "https://cid.econ.ucdavis.edu/PWT11/pwt110.dta",
    ]
    
    for url in urls:
        try:
            print(f"  Trying: {url}")
            response = requests.get(url, timeout=60, allow_redirects=True)
            
            if response.status_code == 200 and len(response.content) > 10000:
                filename = url.split('/')[-1]
                output_file = RAW_DIR / f"pwt_{filename}"
                
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                
                print(f"  [OK] Downloaded {len(response.content):,} bytes")
                print(f"  [OK] Saved to {output_file}")
                return True
            else:
                print(f"  [FAIL] HTTP {response.status_code} or file too small")
                
        except Exception as e:
            print(f"  [FAIL] Error: {e}")
        
        time.sleep(1)
    
    return False

def download_wipo_patents():
    """Download WIPO patent data"""
    print(f"\n{'='*60}")
    print(f"Downloading: WIPO Patents (Resident + Origin)")
    print(f"{'='*60}")
    
    # WIPO IP Statistics API
    url = "https://www3.wipo.int/ipstats/v2/patent"
    
    params_list = [
        {'countryCode': 'US,CH,TW,KR,JP,DE,GB,IL,FR', 'yearRange': '2000-2024', 'indicator': 'count'},
    ]
    
    try:
        for params in params_list:
            response = requests.get(url, params=params, timeout=30)
            print(f"  HTTP {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"  [OK] Got JSON response")
                    output_file = RAW_DIR / "patents_wipo.json"
                    with open(output_file, 'w') as f:
                        json.dump(data, f, indent=2)
                    print(f"  [OK] Saved to {output_file}")
                    return True
                except:
                    print(f"  [FAIL] Response is not valid JSON")
            else:
                print(f"  [FAIL] Failed")
        
        return False
        
    except Exception as e:
        print(f"  [FAIL] Error: {e}")
        return False

def save_metadata(variable_name, source, indicator, description, status):
    """Save metadata for a variable"""
    metadata = {
        'variable': variable_name,
        'source': source,
        'indicator': indicator,
        'description': description,
        'download_date': datetime.now().isoformat(),
        'status': status,
        'countries': COUNTRIES,
        'years': '2000-2024'
    }
    
    metadata_file = METADATA_DIR / f"{variable_name}_metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

def main():
    print("\n" + "="*60)
    print("DATA COLLECTION V2 - USING WORKING API ENDPOINTS")
    print("="*60)
    
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    
    results = {}
    
    # World Bank indicators (direct API - WORKS!)
    wb_indicators = {
        'gdp_pc_ppp': ('NY.GDP.PCAP.PP.KD', 'GDP per capita, PPP (constant 2017 intl $)'),
        'gdp_real_growth': ('NY.GDP.MKTP.KD.ZG', 'GDP growth (annual %)'),
        'researchers_per_million': ('SP.POP.SCIE.RS.P6', 'Researchers in R&D (per million people)'),
        'scopus_articles': ('IP.JRN.ARTC.SC', 'Scientific and technical journal articles'),
        'mva_pct_gdp': ('NV.IND.MANF.ZS', 'Manufacturing, value added (% of GDP)'),
        'hitech_export_share': ('TX.VAL.TECH.MF.ZS', 'High-technology exports (% of manufactured exports)'),
    }
    
    for var_name, (indicator, description) in wb_indicators.items():
        df = download_world_bank_direct(indicator, var_name, description)
        results[var_name] = 'success' if df is not None else 'failed'
        save_metadata(var_name, 'World Bank WDI', indicator, description, results[var_name])
        time.sleep(1)
    
    # OECD MSTI
    oecd_results = download_oecd_msti()
    for var_name, success in oecd_results.items():
        results[var_name] = 'success' if success else 'failed'
        save_metadata(var_name, 'OECD MSTI', var_name.upper(), 
                     f"{var_name.upper()} as % of GDP", results[var_name])
    
    # PWT
    pwt_success = download_pwt()
    results['pwt_data'] = 'success' if pwt_success else 'failed'
    save_metadata('pwt_data', 'Penn World Table 11.0', 'Multiple', 
                 'GDP, productivity, TFP data', results['pwt_data'])
    
    # WIPO
    wipo_success = download_wipo_patents()
    results['patents_resident_origin'] = 'success' if wipo_success else 'failed'
    save_metadata('patents_resident_origin', 'WIPO IP Statistics', 'Patents', 
                 'Patent applications (resident and origin)', results['patents_resident_origin'])
    
    # Summary
    print("\n" + "="*60)
    print("COLLECTION SUMMARY")
    print("="*60)
    
    success_count = sum(1 for v in results.values() if v == 'success')
    total_count = len(results)
    
    print(f"\n[OK] Success: {success_count}/{total_count}")
    print(f"[FAIL] Failed: {total_count - success_count}/{total_count}\n")
    
    for var_name, status in results.items():
        symbol = "[OK]" if status == 'success' else "[FAIL]"
        print(f"  {symbol} {var_name}: {status}")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
