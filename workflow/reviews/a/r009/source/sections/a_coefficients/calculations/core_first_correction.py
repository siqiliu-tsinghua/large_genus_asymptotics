"""Exact q=1 leading and first-correction contributions, including all loops.

The scalar 1/sqrt(pi) and exp(S) are factored out of absolute Z_g(1)/F_g.
Only MZ's proved c1(n), W26's first profile, exact low-type polynomials,
and the signed-loop functional enter.  No old contribution value is input.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from math import comb,factorial
import json
import sys
sys.dont_write_bytecode = True
from runtime import OUTPUT, require_symbolic
require_symbolic()
import sympy as sp
from wp_profiles import P,n,D,Q,delta
from loop_moments import p,z0,S,c1,signed_sum,side_moment

degree,zeros=sp.symbols('degree zeros',integer=True,nonnegative=True)


def compositions(k,m):
    if m==1:
        yield (k,)
    else:
        for first in range(k+1):
            for rest in compositions(k-first,m-1):yield (first,)+rest


def multinomial(k,parts):
    return factorial(k)//sp.prod(factorial(r) for r in parts)


def raw_unit(k):
    return 2*side_moment(0,k)


def raw_elliptic(k):
    # J1(z)=-24*z**-1*L1(z), Eell(z)=(2P*J0(z)-J1(z))/24.
    shifted=sum(comb(k,i)*(-1)**(k-i)*side_moment(1,i) for i in range(k+1))
    return sp.factor(P*side_moment(0,k)/6+shifted)


def external_moment(m,ka,kz,kind):
    raw=raw_unit if kind=='unit' else raw_elliptic
    zero=2*P if kind=='unit' else P**2/12
    ans=0
    for a in compositions(ka,m):
        for z in compositions(kz,m):
            term=multinomial(ka,a)*multinomial(kz,z)
            for ai,zi in zip(a,z):
                if zi and ai:term=0;break
                term*=zero if zi else raw(ai)
            ans+=term
    return sp.factor(ans)


def external_sum(poly,m,kind):
    poly=sp.Poly(sp.expand(poly),degree,zeros)
    return sp.factor(sum(coef*external_moment(m,*powers,kind)
                         for powers,coef in poly.terms()))


def q1_core(n0,c,m,kind,front):
    """front includes 1/(8P), core Aut, and integrated small-core loops."""
    d=delta(2*p+n0,D+degree,2*p-z0+n0-zeros)
    v1=sp.Rational(3,2)+(p+c)/2+c1(2*p+n0)
    loop_averaged=signed_sum(v1-d/2)
    correction=sp.factor(front*external_sum(loop_averaged,m,kind))
    leading=sp.factor(front*external_moment(m,0,0,kind))
    assert not correction.has(S)
    return leading,correction,sp.factor(loop_averaged)


if __name__=='__main__':
    data={}
    specs=[('elliptic_tail',1,1,1,'elliptic',1/(8*P)),
           ('rational_three_connectors',3,2,3,'unit',1/(48*P)),
           ('rational_small_loop',1,1,1,'unit',sp.Rational(1,8))]
    for name,*args in specs:
        lead,corr,poly=q1_core(*args)
        print(name,'leading=',lead,'first correction=',corr)
        data[name]={'leading':str(lead),'first_correction':str(corr),'loop_averaged_polynomial':str(poly)}
    total0=sp.factor(sum(sp.sympify(v['leading']) for v in data.values()))
    total1=sp.factor(sum(sp.sympify(v['first_correction']) for v in data.values()))
    print('q1 total leading:',total0)
    print('q1 total first correction:',total1)
    print('unit moments:',[raw_unit(k) for k in range(3)])
    print('elliptic moments:',[raw_elliptic(k) for k in range(3)])
    data['total_leading']=str(total0);data['total_first_correction']=str(total1)
    (OUTPUT / 'core_first_correction.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
