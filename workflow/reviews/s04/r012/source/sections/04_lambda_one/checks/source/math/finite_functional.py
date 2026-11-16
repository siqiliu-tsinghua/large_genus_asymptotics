"""Finite signed functional for Q03,Q04,Q13 once full inputs are supplied.

Canonical input symbols are N=n, DD=D, M[j]=count of degree j, P=pi^2.
Input e_j are complexity coefficients (2G-2+n)^-j; c_j are G^-j.
No proposed high-order target or unverified e3/e4/c3/c4 is embedded here.
"""
from pathlib import Path
from functools import lru_cache
import json
import sys
sys.dont_write_bytecode = True
sys.path.insert(0,str(Path(__file__).resolve().parent))
import higher_blocks as h
s, P, pf, lm = h.s,h.P,h.pf,h.lm
N, DD = pf.n,pf.D
M = s.symbols('m0:7',integer=True)
Z = (lm.z0,lm.z1,lm.z2)+s.symbols('z3:7',integer=True)
EX = s.symbols('external_0:7',integer=True)
XD = h.x
HERE = Path(__file__).resolve().parent


def signed_average(poly):
    """Normalized paired-loop L on p,D,Z[0],...,Z[6]."""
    poly = s.Poly(s.expand(poly),lm.p,DD,*Z)
    return s.factor(sum(coef*lm.moment(powers) for powers,coef in poly.terms()))


@lru_cache(None)
def gamma_ratio_coeffs(q, order):
    """Gamma(2g-2-q)/Gamma(2g-2)/(2g)^-q, powers of 1/g."""
    a = [s.Integer(1)]+[s.Integer(0)]*order
    for j in range(1,q+1):
        b = [s.Rational(j+2,2)**r for r in range(order+1)]
        a = [s.expand(sum(a[k]*b[r-k] for k in range(r+1))) for r in range(order+1)]
    return tuple(a)


def canonical_profiles():
    substitutions = {pf.Q:N-M[0],pf.m1:M[1],s.Symbol('m2',integer=True):M[2]}
    return {0:s.Integer(1),1:-pf.delta(N,DD,N-M[0]),
            2:pf.profile_potential()[0].subs(substitutions,simultaneous=True)}


def canonical_volumes():
    c20 = s.Rational(145,288)-s.Rational(395,72)/P+s.Rational(1513,72)/P**2
    return {0:s.Integer(1),1:lm.c1(N),2:c20+lm.cusp_and_c2_difference()[3]}


def root_polynomial(q,b,order,profiles,volumes):
    """Polynomial before L, with external degree/count variables retained."""
    assert all(j in profiles and j in volumes for j in range(order+1))
    c = s.Rational(q+b,2)
    nn = 2*lm.p+b
    substitution = {N:nn,DD:DD+XD,**{M[j]:Z[j]+EX[j] for j in range(len(M))}}
    e = [s.sympify(profiles[j]).subs(substitution,simultaneous=True) for j in range(order+1)]
    cc = [s.sympify(volumes[j]).subs(N,nn) for j in range(order+1)]
    gamma = gamma_ratio_coeffs(q,order)
    root_volume = [sum(cc[j]*s.rf(s.Rational(1,2)+j,r-j)/s.factorial(r-j)
                       *(lm.p+c)**(r-j) for j in range(r+1)) for r in range(order+1)]
    profile = [s.Integer(1)]+[sum(e[j]*s.binomial(r-1,r-j)/2**j
                                     *s.Rational(q+2,2)**(r-j) for j in range(1,r+1))
                                for r in range(1,order+1)]
    return s.expand(sum(gamma[i]*root_volume[j]*profile[order-i-j]
                        for i in range(order+1) for j in range(order-i+1)))


def averaged(q,b,order,profiles,volumes):
    result = signed_average(root_polynomial(q,b,order,profiles,volumes))
    assert not result.has(lm.S),result
    return s.Poly(s.expand(result),XD,*EX)


def absolute_group(q,order,profiles,volumes):
    """Exact Q_(q,order), scalar after e^S/sqrt(pi) and g^-q."""
    if q==0:
        return s.factor(averaged(0,0,order,profiles,volumes).as_expr().subs(
            {XD:0,**{a:0 for a in EX}}))
    total = 0
    for gs,matrix in h.low.enumerate_cores(q):
        b = sum(matrix[0])
        correction = averaged(q,b,order,profiles,volumes)
        total += h.integrate_block(gs,matrix,correction)
    return s.factor(total/(8*P)**q)


def verify_existing_orders():
    profiles,volumes=canonical_profiles(),canonical_volumes()
    known=json.loads((HERE/'higher_blocks.json').read_text(encoding='utf-8'))['blocks']
    checks={}
    expected={
      (0,1):s.Rational(1,12)-s.Rational(65,6)/P,
      (0,2):s.Rational(43,288)-s.Rational(469,36)/P+s.Rational(5665,72)/P**2,
      (1,2):s.sympify(known['Q12'],locals={'P':P}),
      (2,2):s.sympify(known['Q22'],locals={'P':P})}
    for (q,order),target in expected.items():
        got=absolute_group(q,order,profiles,volumes)
        assert s.factor(got-target)==0,(q,order,got,target)
        checks[f'Q{q}{order}']=str(got)
        print('verified',q,order,got,flush=True)
    (HERE/'functional_checks.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8',newline='\n')


if __name__=='__main__':
    verify_existing_orders()
