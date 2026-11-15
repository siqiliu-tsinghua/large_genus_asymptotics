"""Independent Wick mass certificate for every enumerated q<=4 core.

Gaussian contractions enumerate labelled small flags. Dividing out vacuum
components leaves precisely graphs connected to the distinguished root.
No target core count or asymptotic coefficient enters the construction.
"""
from pathlib import Path
import sys,json
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent))
import higher_blocks as h
s=h.s
x,z,T=s.symbols('complexity small_flags root_valence')
K=4
potential=0
for k in range(1,K+1):
    for genus in range((k+1)//2+1):
        n=k+2-2*genus
        assert n>=1
        potential+=x**k*z**n/s.factorial(n)

def trunc(expr):
    return s.Poly(s.expand(expr),x).as_dict()

partition=s.Integer(1)
power=s.Integer(1)
for v in range(1,K+1):
    power=s.expand(power*potential)
    power=sum(coef*x**j[0] for j,coef in trunc(power).items() if j[0]<=K)
    partition+=power/s.factorial(v)
wick=0
for (q,n),coef in s.Poly(s.expand(partition),x,z).terms():
    wick+=coef*x**q*sum(s.factorial(n)*T**(n-2*ell)/
              (2**ell*s.factorial(ell)*s.factorial(n-2*ell)) for ell in range(n//2+1))
wick=s.Poly(s.expand(wick),x)
vacuum=[wick.nth(q).subs(T,0) for q in range(K+1)]
root=[s.Integer(1)]
out={}
for q in range(1,K+1):
    root.append(s.expand(wick.nth(q)-sum(vacuum[j]*root[q-j] for j in range(1,q+1))))
    enumerated=0
    cores=h.low.enumerate_cores(q)
    for gs,matrix in cores:
        enumerated+=T**sum(matrix[0])/h.low.automorphism_formula(gs,matrix)
    assert s.expand(root[q]-enumerated)==0,(q,root[q],enumerated)
    out[str(q)]={'core_count':len(cores),'sum_t^root_valence_divided_by_Aut':str(root[q])}
    print('Wick mass equality',q,len(cores),root[q],flush=True)
(h.HERE/'core_mass_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
