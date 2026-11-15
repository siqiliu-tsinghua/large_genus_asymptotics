"""Independent symbolic r-Euler checks of the order-five kernel tables."""
from pathlib import Path
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import finite_functional as f
sys.path.insert(0,str(HERE.parent/'root'))
import asymptotic_inputs as a
s,P=f.s,f.P
r=s.Symbol('r')
degree=10
mu=s.series((2+3*r+r*r)*s.sqrt(P)*r/s.sin(s.sqrt(P)*r),r,0,degree+1).removeO().expand()
nu=s.series(s.cos(s.sqrt(P)*r)-s.sin(s.sqrt(P)*r)/(s.sqrt(P)*(1+r)),r,0,degree+1).removeO().expand()
expected=a.moments(degree)
rows=[]
for j in range(degree+1):
    for name,pol,table in [('mu',mu,expected[0]),('nu',nu,expected[1])]:
        got=s.expand(pol.subs(r,0))
        assert s.factor(got-table[j])==0,(name,j,s.factor(got-table[j]))
        rows.append({'kernel':name,'moment':j,'exact':str(got),'difference':'0'})
    mu=s.expand((1+r)*s.diff(mu,r)/2)
    nu=s.expand((1+r)*s.diff(nu,r)/2)
print('All 22 symbolic mu/nu moments through degree 10 independently verified',flush=True)
(HERE/'kernel_moment_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
