#!/usr/bin/env python3
"""Agent 4: compact quantitative + econometric analysis (US vs China tech potential).
Descriptive + max 2 FE models + PCA capability index. No statsmodels dependency.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
PROC = ROOT / "data" / "processed"
FIG = ROOT / "figures"
RES = ROOT / "results"
REP = ROOT / "reports"
FIG.mkdir(exist_ok=True); RES.mkdir(exist_ok=True)

plt.rcParams.update({"figure.dpi": 150, "axes.grid": True, "grid.alpha": 0.3, "font.size": 9})

core = pd.read_csv(PROC / "core_panel.csv")
tech = pd.read_csv(PROC / "tech_panel.csv")
df = core.merge(tech[["country_iso3","year","semi_exports_hs8542"]], on=["country_iso3","year"], how="left")
df = df.sort_values(["country_iso3","year"]).reset_index(drop=True)
COUNTRIES = ["USA","CHN","KOR","JPN","DEU","GBR","ISR","FRA"]
LAB = {"USA":"USA","CHN":"China","KOR":"Korea","JPN":"Japan","DEU":"Germany","GBR":"UK","ISR":"Israel","FRA":"France"}

WIN = df[(df.year>=2010)&(df.year<=2023)].copy()
US = WIN[WIN.country_iso3=="USA"].set_index("year")
CN = WIN[WIN.country_iso3=="CHN"].set_index("year")

# ---------- helpers ----------
def cagr(s0,s1,n): return (s1/s0)**(1/n)-1 if s0 and s1 and s0>0 and s1>0 else np.nan
def ols_slope(x,y):
    m = np.isfinite(x)&np.isfinite(y)
    x,y = x[m],y[m]
    if len(y)<4: return np.nan,np.nan,np.nan,np.nan
    X = np.column_stack([np.ones(len(x)),x])
    b,_,_,_ = np.linalg.lstsq(X,y,rcond=None)
    e = y - X@b
    k=2; s2 = e@e/(len(y)-k)
    V = s2*np.linalg.inv(X.T@X)
    se = np.sqrt(np.diag(V))[1]
    t=b[1]/se if se>0 else np.nan
    p=2*(1-stats.t.cdf(abs(t),len(y)-k)) if np.isfinite(t) else np.nan
    return b[1],se,t,p
def fe_ols(y,X,cnames):
    """LSDV via dummies already in X. HC1 robust SE."""
    m = np.isfinite(y)&np.all(np.isfinite(X),axis=1)
    yv,Xv = y[m],X[m]
    n,k = Xv.shape
    b,_,_,_ = np.linalg.lstsq(Xv,yv,rcond=None)
    e = yv-Xv@b
    XtX_inv = np.linalg.inv(Xv.T@Xv)
    meat = (Xv*e[:,None]).T@(Xv*e[:,None])
    V = XtX_inv@meat@XtX_inv * n/(n-k)
    se = np.sqrt(np.diag(V))
    t = b/se; p = 2*(1-stats.t.cdf(np.abs(t),n-k))
    ci_l,ci_h = b-1.96*se, b+1.96*se
    r2 = 1-(e@e)/(((yv-yv.mean())**2).sum())
    out = pd.DataFrame({"coef":b,"se":se,"t":t,"p":p,"ci_lo":ci_l,"ci_hi":ci_h},index=cnames)
    return out,e,n,k,r2,m

# ---------- D1: levels snapshot ----------
VARS = ["gerd_pct_gdp","berd_pct_gdp","researchers_per_million","scopus_articles",
        "patents_resident","mva_pct_gdp","hitech_export_share","gdp_pc_ppp","tfp_ctfp","semi_exports_hs8542"]
rows=[]
for v in VARS:
    for yr in [2010,2015,2021,2023]:
        try: a = float(US.loc[yr,v]); b=float(CN.loc[yr,v])
        except: a,b=np.nan,np.nan
        rows.append({"var":v,"year":yr,"USA":a,"CHN":b,"CHN_USA_ratio":b/a if a else np.nan,"gap_CHN_minus_USA":b-a})
D1=pd.DataFrame(rows); D1.to_csv(RES/"descriptive_snapshot_US_CHN.csv",index=False)

# ---------- D2: CAGR ----------
rows=[]
for v in VARS:
    for c in COUNTRIES:
        s = WIN[WIN.country_iso3==c].set_index("year")[v].dropna()
        s = s[(s.index>=2010)]
        if len(s)>=2:
            y0,y1 = s.index.min(), s.index.max()
            # prefer 2010->latest common; also 2010-2023 if avail
            v0,v1 = s.iloc[0],s.iloc[-1]
            rows.append({"var":v,"country":c,"t0":int(y0),"t1":int(y1),"v0":v0,"v1":v1,
                         "CAGR":cagr(v0,v1,y1-y0),"abs_change":v1-v0})
D2=pd.DataFrame(rows); D2.to_csv(RES/"descriptive_cagr.csv",index=False)

# ---------- D3: trend slopes + convergence (US vs CHN) ----------
trows=[]
for v in ["gerd_pct_gdp","researchers_per_million","scopus_articles","mva_pct_gdp","hitech_export_share","tfp_ctfp","gdp_pc_ppp"]:
    for c in ["USA","CHN"]:
        s = WIN[WIN.country_iso3==c][["year",v]].dropna()
        b,se,t,p = ols_slope((s.year-2010).values, s[v].values)
        trows.append({"var":v,"country":c,"slope_per_year":b,"se":se,"p":p,"n":len(s)})
    # interaction: pooled US+CHN
    s = WIN[WIN.country_iso3.isin(["USA","CHN"])][["year","country_iso3",v]].dropna()
    if len(s)>=8:
        tt=(s.year-2010).values; d=(s.country_iso3=="CHN").astype(int).values; yv=s[v].values
        X=np.column_stack([np.ones(len(s)),tt,d,tt*d])
        bvec,_,_,_=np.linalg.lstsq(X,yv,rcond=None)
        e=yv-X@bvec; s2=e@e/(len(s)-4); V=s2*np.linalg.inv(X.T@X)
        se=np.sqrt(np.diag(V)); tt2=bvec/se; pp=2*(1-stats.t.cdf(np.abs(tt2),len(s)-4))
        trows.append({"var":v,"country":"DIFF_CHN_minus_USA_slope","slope_per_year":bvec[3],"se":se[3],"p":pp[3],"n":len(s)})
D3=pd.DataFrame(trows); D3.to_csv(RES/"trend_slopes_convergence.csv",index=False)

# ---------- D4: conversion ratios ----------
conv=[]
for yr in [2010,2015,2021]:
    for c in ["USA","CHN"]:
        r = WIN[(WIN.country_iso3==c)&(WIN.year==yr)]
        if r.empty: continue
        r=r.iloc[0]
        conv.append({"year":yr,"country":c,
          "articles_per_1000_researchers": r.scopus_articles/(r.researchers_per_million/1000) if pd.notna(r.scopus_articles) and pd.notna(r.researchers_per_million) else np.nan,
          "patents_per_1000_articles": r.patents_resident/(r.scopus_articles/1000) if pd.notna(r.patents_resident) and pd.notna(r.scopus_articles) else np.nan,
          "patents_per_GERD_point": r.patents_resident/r.gerd_pct_gdp if pd.notna(r.patents_resident) and pd.notna(r.gerd_pct_gdp) else np.nan,
          "hitech_per_GERD_point": r.hitech_export_share/r.gerd_pct_gdp if pd.notna(r.hitech_export_share) and pd.notna(r.gerd_pct_gdp) else np.nan})
D4=pd.DataFrame(conv); D4.to_csv(RES/"conversion_ratios.csv",index=False)

# ---------- D5: correlations ----------
corr_vars=["gerd_pct_gdp","berd_pct_gdp","researchers_per_million","scopus_articles","patents_resident","mva_pct_gdp","hitech_export_share","tfp_ctfp","gdp_pc_ppp"]
C = WIN[corr_vars].corr(method="pearson",min_periods=20)
C.to_csv(RES/"correlations_pooled.csv")
# TFP bivariate with lagged GERD
tmp=WIN[["country_iso3","year","tfp_ctfp","gerd_pct_gdp","researchers_per_million"]].copy()
tmp["gerd_lag1"]=tmp.groupby("country_iso3").gerd_pct_gdp.shift(1)
tmp["lres"]=np.log(tmp.researchers_per_million)
biv = tmp[["tfp_ctfp","gerd_lag1","lres"]].corr()
biv.to_csv(RES/"correlations_tfp_inputs.csv")

# ================= FIGURES (9) =================
def savefig(p): plt.tight_layout(); plt.savefig(p,bbox_inches="tight"); plt.close()

# F1 GERD
plt.figure(figsize=(7,4))
for c in COUNTRIES:
    s=WIN[WIN.country_iso3==c].sort_values("year")
    lw=2.4 if c in ("USA","CHN") else 1.1
    plt.plot(s.year,s.gerd_pct_gdp,label=LAB[c],linewidth=lw)
plt.ylabel("GERD (% GDP)"); plt.title("R&D intensity: China converges toward US level, Korea/Israel lead"); plt.legend(ncol=4,fontsize=7); plt.xlim(2010,2023)
savefig(FIG/"F1_gerd_trends.png")

# F2 researchers (log? level with ISR missing note)
plt.figure(figsize=(7,4))
for c in COUNTRIES:
    s=WIN[WIN.country_iso3==c].sort_values("year")
    lw=2.4 if c in ("USA","CHN") else 1.1
    plt.plot(s.year,s.researchers_per_million,label=LAB[c],linewidth=lw)
plt.ylabel("Researchers per million"); plt.title("Human capital: US level ~2x China (2021); ISR missing in WDI"); plt.legend(ncol=4,fontsize=7); plt.xlim(2010,2023)
savefig(FIG/"F2_researchers.png")

# F3 articles + ratio
fig,ax=plt.subplots(2,1,figsize=(7,5),sharex=True)
for c in ["USA","CHN","JPN","DEU","KOR","GBR"]:
    s=WIN[WIN.country_iso3==c].sort_values("year")
    ax[0].plot(s.year,s.scopus_articles/1000,label=LAB[c],linewidth=2.4 if c in ("USA","CHN") else 1.1)
ax[0].set_ylabel("Articles (thousands)"); ax[0].legend(ncol=3,fontsize=7); ax[0].set_title("Science output: China overtook USA ~2020 (volume, not impact)")
piv=WIN.pivot(index="year",columns="country_iso3",values="scopus_articles")
ax[1].plot(piv.index,piv.CHN/piv.USA,color="black"); ax[1].axhline(1,color="red",ls="--",lw=1)
ax[1].set_ylabel("CHN/USA ratio"); ax[1].set_xlabel("Year")
savefig(FIG/"F3_articles_crossover.png")

# F4 patents log
plt.figure(figsize=(7,4))
for c in ["USA","CHN","JPN","KOR","DEU"]:
    s=WIN[WIN.country_iso3==c].sort_values("year")
    plt.plot(s.year,s.patents_resident,label=LAB[c],linewidth=2.4 if c in ("USA","CHN") else 1.2)
plt.yscale("log"); plt.ylabel("Resident patent applications (log scale)")
plt.title("Patents: China >> USA in counts since ~2011 — quantity, NOT quality"); plt.legend(fontsize=7); plt.xlim(2010,2021)
plt.annotate("WIPO resident counts;\nCN incl. subsidies effects",xy=(2016,968252),xytext=(2012,300000),fontsize=7,arrowprops=dict(arrowstyle="->",lw=0.8))
savefig(FIG/"F4_patents_log.png")

# F5 MVA
plt.figure(figsize=(7,4))
for c in COUNTRIES:
    s=WIN[WIN.country_iso3==c].sort_values("year")
    plt.plot(s.year,s.mva_pct_gdp,label=LAB[c],linewidth=2.4 if c in ("USA","CHN") else 1.1)
plt.ylabel("MVA (% GDP)"); plt.title("Production structure: China ~25% vs USA ~11% — persistent gap"); plt.legend(ncol=4,fontsize=7); plt.xlim(2010,2023)
savefig(FIG/"F5_mva_share.png")

# F6 hitech + events
plt.figure(figsize=(7,4))
for c in COUNTRIES:
    s=WIN[WIN.country_iso3==c].sort_values("year")
    plt.plot(s.year,s.hitech_export_share,label=LAB[c],linewidth=2.4 if c in ("USA","CHN") else 1.1)
for d,lab in [(2022.6,"CHIPS Act Aug22\nBIS controls Oct22")]:
    plt.axvline(d,color="red",ls="--",lw=1); plt.text(d+0.05,30,lab,fontsize=6,color="red")
plt.ylabel("High-tech exports (% mfg exports)"); plt.title("Export sophistication: China share fell after 2021; broad basket, not semis-only"); plt.legend(ncol=4,fontsize=7); plt.xlim(2010,2023)
savefig(FIG/"F6_hitech_exports.png")

# F7 TFP (rel USA=1)
plt.figure(figsize=(7,4))
for c in [x for x in COUNTRIES if x!="USA"]:
    s=WIN[WIN.country_iso3==c].sort_values("year")
    plt.plot(s.year,s.tfp_ctfp,label=LAB[c],linewidth=1.4)
plt.axhline(1,color="black",ls="-",lw=1.2,label="USA = 1.00 (by construction)")
plt.ylabel("TFP level (PWT ctfp, USA=1 each year)"); plt.title("Aggregate TFP: China ~0.40→0.47 of US; macro proxy, not tech-TFP"); plt.legend(ncol=4,fontsize=7); plt.xlim(2010,2023)
savefig(FIG/"F7_tfp_levels.png")

# F8 semi exports
plt.figure(figsize=(7,4))
for c in ["USA","CHN","KOR","JPN","DEU"]:
    s=WIN[WIN.country_iso3==c].sort_values("year")
    plt.plot(s.year,s.semi_exports_hs8542/1e9,label=LAB[c],linewidth=2.4 if c in ("USA","CHN") else 1.2,marker="o" if c=="CHN" else None,markersize=3)
plt.axvspan(2015,2017,alpha=0.15,color="gray"); plt.text(2015.1,140,"CHN 2015-17 quarantined\n(multi-record)",fontsize=6)
for d in [2022.6,2022.75]: plt.axvline(d,color="red",ls="--",lw=1)
plt.text(2022.8,120,"BIS Oct22",fontsize=6,color="red")
plt.ylabel("IC exports HS8542 (USD bn, nominal)"); plt.title("Semiconductor trade: China exports > USA in value (assembly+processing bias)"); plt.legend(fontsize=7)
savefig(FIG/"F8_semi_exports.png")

# F9 finance mix bar 2010 vs 2023
x=pd.pivot_table(WIN[WIN.year.isin([2010,2023])],index="country_iso3",columns="year",values="berd_pct_gdp")
x=x.reindex(["USA","CHN","KOR","JPN","DEU","GBR","FRA","ISR"])
plt.figure(figsize=(7,4)); w=0.35; xi=np.arange(len(x))
plt.bar(xi-w/2,x[2010],w,label="2010"); plt.bar(xi+w/2,x[2023],w,label="2023")
plt.xticks(xi,[LAB[i] for i in x.index],rotation=0); plt.ylabel("Business-financed R&D (% GDP)")
plt.title("Finance mix: business R&D rose everywhere; ISR/KOR highest"); plt.legend(fontsize=8)
savefig(FIG/"F9_berd_mix.png")

# ================= MODEL 1 =================
est = WIN[["country_iso3","year","tfp_ctfp","gerd_pct_gdp","researchers_per_million"]].copy()
est["gerd_lag1"]=est.groupby("country_iso3").gerd_pct_gdp.shift(1)
est["lres"]=np.log(est.researchers_per_million)
est1 = est.dropna(subset=["tfp_ctfp","gerd_lag1","lres"])
# dummies
cc = sorted(est1.country_iso3.unique()); yy = sorted(est1.year.unique())
Xc = pd.get_dummies(est1.country_iso3,drop_first=True,dtype=float)
Xy = pd.get_dummies(est1.year,drop_first=True,dtype=float)
X = pd.concat([est1[["gerd_lag1","lres"]].reset_index(drop=True),Xc.reset_index(drop=True),Xy.reset_index(drop=True)],axis=1)
cnames = X.columns.tolist()
res1,_,n1,k1,r2_1,_ = fe_ols(est1.tfp_ctfp.values, X.values, cnames)
res1.to_csv(RES/"model1_tfp_gerd_hc_FE_coef.csv")
m1 = res1.loc[["gerd_lag1","lres"]]

# ================= PCA + MODEL 2 =================
pca_vars = {"gerd_pct_gdp":"g","berd_pct_gdp":"b","lres":"lres","lart":"lart"}
pca_df = WIN[["country_iso3","year","gerd_pct_gdp","berd_pct_gdp","researchers_per_million","scopus_articles","tfp_ctfp"]].copy()
pca_df["lres"]=np.log(pca_df.researchers_per_million); pca_df["lart"]=np.log(pca_df.scopus_articles)
pca_df["tech_pc1_lag1"]=np.nan
# standardize on complete-case sample (pooled 2010-2023)
cc2 = pca_df.dropna(subset=["gerd_pct_gdp","berd_pct_gdp","lres","lart"])
Z = (cc2[["gerd_pct_gdp","berd_pct_gdp","lres","lart"]] - cc2[["gerd_pct_gdp","berd_pct_gdp","lres","lart"]].mean())/cc2[["gerd_pct_gdp","berd_pct_gdp","lres","lart"]].std()
Cmat = np.cov(Z.values,rowvar=False)
evals,evecs = np.linalg.eigh(Cmat)  # ascending
order=np.argsort(evals)[::-1]; evals=evals[order]; evecs=evecs[:,order]
pc1 = Z.values@evecs[:,0]
if np.mean(evecs[:,0])<0: evecs[:,0]*=-1; pc1=-pc1
load = pd.DataFrame({"variable":["gerd_pct_gdp","berd_pct_gdp","log_researchers","log_articles"],"PC1_loading":evecs[:,0],"PC2_loading":evecs[:,1]})
load.to_csv(RES/"pca_loadings.csv",index=False)
varexp = evals/evals.sum()
pd.DataFrame({"PC":[1,2,3,4],"var_exp":varexp}).to_csv(RES/"pca_variance.csv",index=False)
cc2 = cc2.copy(); cc2["pc1"]=pc1
pca_df = pca_df.merge(cc2[["country_iso3","year","pc1"]],on=["country_iso3","year"],how="left")
pca_df["pc1_lag1"]=pca_df.groupby("country_iso3").pc1.shift(1)
est2 = pca_df.dropna(subset=["tfp_ctfp","pc1_lag1"])
Xc2 = pd.get_dummies(est2.country_iso3,drop_first=True,dtype=float)
Xy2 = pd.get_dummies(est2.year,drop_first=True,dtype=float)
X2 = pd.concat([est2[["pc1_lag1"]].reset_index(drop=True),Xc2.reset_index(drop=True),Xy2.reset_index(drop=True)],axis=1)
res2,_,n2,k2,r2_2,_ = fe_ols(est2.tfp_ctfp.values, X2.values, X2.columns.tolist())
res2.to_csv(RES/"model2_tfp_techpc1_FE_coef.csv")

# F10 scatter pc1 vs tfp
plt.figure(figsize=(6,4))
for c in sorted(est2.country_iso3.unique()):
    s=est2[est2.country_iso3==c]
    plt.scatter(s.pc1_lag1,s.tfp_ctfp,label=LAB.get(c,c),s=18)
plt.xlabel("Technology capability PC1 (lagged 1y, std units)"); plt.ylabel("TFP (USA=1)")
plt.title(f"Capability vs TFP (pooled r={est2[['pc1_lag1','tfp_ctfp']].corr().iloc[0,1]:.2f}; within-FE slope n.s.)")
plt.legend(fontsize=7)
savefig(FIG/"F10_pca_tfp_scatter.png")

# ================= POLICY/EVENT simple table =================
ev=[]
for c in ["USA","CHN"]:
    for v in ["semi_exports_hs8542","hitech_export_share"]:
        s=WIN[(WIN.country_iso3==c)].set_index("year")[v]
        pre=np.nanmean([s.get(y) for y in [2020,2021]]); post=np.nanmean([s.get(y) for y in [2022,2023]])
        ev.append({"country":c,"var":v,"pre_2020_21":pre,"post_2022_23":post,"change_pct":100*(post-pre)/pre if pre else np.nan})
pd.DataFrame(ev).to_csv(RES/"event_CHIPS_BIS_prepost.csv",index=False)

# regression summary tidy
reg = pd.concat([
  res1.loc[["gerd_lag1","lres"]].assign(model="M1_TFP_FE"),
  res2.loc[["pc1_lag1"]].assign(model="M2_TFP_PC1_FE")])
reg.to_csv(RES/"regression_results.csv")
print("M1:"); print(res1.loc[["gerd_lag1","lres"]].round(4).to_string()); print("n=",n1,"k=",k1,"R2=",round(r2_1,3))
print("M2:"); print(res2.loc[["pc1_lag1"]].round(4).to_string()); print("n=",n2,"k=",k2,"R2=",round(r2_2,3))
print("PCA var exp:",np.round(varexp,3)); print(load.round(3).to_string(index=False))
print("D1/D2/D3/conv/corr/figures done")
