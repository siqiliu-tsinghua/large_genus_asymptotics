"""Direct factorial-series guard for the high paired cumulants.

This numerical guard checks the exact functional implementation, not the
asymptotic coefficient by extrapolation. No candidate coefficient is read.
"""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent))
import finite_functional as f
import mpmath as mp
mp.mp.dps=110

patterns=[
 (0,8,0,0,0,0,0,0,0),
 (2,6,2,0,0,0,0,0,0),
 (0,5,0,0,0,0,0,1,0),
 (1,3,0,0,2,0,0,0,0),
 (0,2,0,1,0,0,0,0,2),
 (0,0,0,0,0,0,0,0,4),
 (0,4,1,0,0,2,0,0,0),
 (0,1,1,1,1,0,0,0,0)]
N=64
fac=[mp.factorial(2*a+1) for a in range(N+1)]
weights={(a,b):(-1)**(a+b)*mp.pi**(2*(a+b+1))/((a+b+1)*fac[a]*fac[b])
         for a in range(N+1) for b in range(N+1)}
rows=[]
for powers in patterns:
    _, kd,*lows=powers
    direct=mp.mpf(0)
    for (a,b),w in weights.items():
        stat=(a+b)**kd
        for j,k in enumerate(lows):
            if k: stat*=((a==j)+(b==j))**k
        direct+=w*stat
    exact=f.lm.cumulant(powers)
    special=mp.euler+mp.log(2*mp.pi)-mp.ci(2*mp.pi)
    numerical=mp.mpf(str(exact.subs({f.P:f.s.pi**2,f.lm.S:f.s.Float(str(special),110)}).evalf(105)))
    difference=abs(direct-numerical)
    assert difference<mp.mpf('1e-95')*(1+abs(numerical)),(powers,difference)
    rows.append({'powers':powers,'exact':str(exact),'direct_minus_exact':str(direct-numerical)})
    print('checked',powers,'difference',mp.nstr(difference,5),flush=True)
out={'method':'direct paired factorial series for endpoint degrees 0..64; 110 decimal digit guard, not asymptotic extrapolation',
     'rows':rows}
out['raw_connector_rows']=[]
for d,k in [(0,8),(1,6),(2,4),(3,2),(4,1),(5,0)]:
    direct=mp.fsum((-1)**a*2**(d+1)*mp.pi**(2*(d+a+1))*a**k/
                   ((a+d+1)*fac[a]) for a in range(N+1))
    exact=f.h.root_raw_moment(d,k)
    numerical=mp.mpf(str(exact.subs(f.P,f.s.pi**2).evalf(105)))
    difference=abs(direct-numerical)
    assert difference<mp.mpf('1e-95')*(1+abs(numerical)),(d,k,difference)
    out['raw_connector_rows'].append({'d':d,'degree_moment':k,'exact':str(exact),'direct_minus_exact':str(direct-numerical)})
    print('raw connector checked',d,k,'difference',mp.nstr(difference,5),flush=True)
(f.HERE/'high_moment_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
