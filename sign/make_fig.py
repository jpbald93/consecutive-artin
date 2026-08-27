import json, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
d=json.load(open('../results/sign_analysis_1e9.json'))
T=[r['T'] for r in d]; dl=[r['delta'] for r in d]
dm=[r['delta_model'] for r in d]
col=['crimson' if x>0 else 'steelblue' for x in dl]
# OLS on delta_model
n=len(d); mx=sum(dm)/n; my=sum(dl)/n
b=sum((x-mx)*(y-my) for x,y in zip(dm,dl))/sum((x-mx)**2 for x in dm)
a0=my-b*mx
fig,ax=plt.subplots(figsize=(7.2,5))
ax.scatter(T,dl,c=col,s=42,edgecolor='k',linewidth=.4,zorder=3)
for r in d:
    if r['delta']>0.009 or r['delta']<-0.03 or r['base'] in (15,26,102):
        ax.annotate(f"${r['base']}$",(r['T'],r['delta']),textcoords="offset points",xytext=(5,3),fontsize=7)
# dashed calibration line in T-space: delta_model = k*T (proportional); recover k
k=sum(m/t for m,t in zip(dm,T) if abs(t)>1e-9)/sum(1 for t in T if abs(t)>1e-9)
xs=[min(T)+i*(max(T)-min(T))/200 for i in range(201)]
ax.plot(xs,[b*k*x+a0 for x in xs],'k--',lw=1,label=r'$\delta = 1.053\,\delta_{\rm model} - 0.0029$  ($R^2=0.958$)')
ax.axhline(0,color='gray',lw=.6); ax.axvline(0,color='gray',lw=.6)
ax.set_xlabel(r'$T(a)$  (character statistic, eq. (2))')
ax.set_ylabel(r'$\delta(a;10^9)$')
ax.legend(fontsize=8,loc='upper left')
ax.grid(alpha=.3,zorder=0)
plt.tight_layout(); plt.savefig('fig_sign_T.pdf'); plt.savefig('fig_sign_T.png',dpi=150)
print('R2 check: slope',round(b,3),'intercept',round(a0,5))
