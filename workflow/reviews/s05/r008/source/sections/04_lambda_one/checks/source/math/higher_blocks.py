"""Independent higher-order blocks, not an assertion of full coefficients.

No proposed third/fourth final coefficient is an input.  Exact psi recursion,
partition inversion, root-core enumeration and the approved e1/e2 inputs.
All output is confined to this directory; use python -B.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
from itertools import product
from math import factorial, comb
import json
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT/'sections/a_coefficients/calculations'))
import runtime
runtime.OUTPUT = HERE
runtime.require_symbolic()
import sympy as s
import enumerate_cores as low
import wp_profiles as pf
import loop_moments as lm

P = pf.P


def df(n):
    z = 1
    for j in range(n, 0, -2):
        z *= j
    return z


@lru_cache(None)
def psi(g, ds):
    ds = tuple(sorted(ds))
    n = len(ds)
    if g < 0 or 2*g-2+n <= 0 or any(x < 0 for x in ds):
        return F(0)
    if sum(ds) != 3*g-3+n:
        return F(0)
    if g == 0:
        return F(factorial(n-3), __import__('math').prod(factorial(d) for d in ds))
    if g == 1 and ds == (1,):
        return F(1, 24)
    if 0 in ds:
        rest = ds[1:]
        return sum((psi(g, tuple(sorted(rest[:i]+(d-1,)+rest[i+1:])))
                    for i,d in enumerate(rest) if d), F(0))
    if 1 in ds:
        j = ds.index(1)
        return (2*g+n-3)*psi(g, ds[:j]+ds[j+1:])
    pivot, rest = ds[-1], ds[:-1]
    z = F(0)
    for j, d in enumerate(rest):
        child = tuple(sorted(rest[:j]+(pivot+d-1,)+rest[j+1:]))
        z += F(df(2*(pivot+d)-1), df(2*d-1))*psi(g, child)
    for a in range(pivot-1):
        b = pivot-2-a
        split = psi(g-1, tuple(sorted((a,b)+rest)))
        for mask in range(1 << len(rest)):
            left = tuple(rest[i] for i in range(len(rest)) if mask>>i & 1)
            right = tuple(rest[i] for i in range(len(rest)) if not mask>>i & 1)
            for h in range(g+1):
                split += psi(h, tuple(sorted((a,)+left)))*psi(g-h, tuple(sorted((b,)+right)))
        z += F(df(2*a+1)*df(2*b+1),2)*split
    return z/df(2*pivot+1)


low.psi = psi
original_vertex_poly = low.vertex_poly


@lru_cache(None)
def cached_vertex(g, flags, edge_count):
    return original_vertex_poly(g, flags, edge_count)


low.vertex_poly = lambda g, flags, edge_count: cached_vertex(g, tuple(flags), edge_count)


@lru_cache(None)
def bracket(g, ds):
    """Paper bracket [tau_ds]_(g,len(ds)), a SymPy polynomial in P=pi^2.

    Uses exact DVV and kappa partition inversion, with no WP table input.
    This is the paper stack bracket (V_1,1=P/12, [tau_1]_1,1=1/2).
    """
    ds = tuple(sorted(ds))
    n = len(ds)
    m = 3*g-3+n-sum(ds)
    if 2*g-2+n<=0 or m<0 or any(d<0 for d in ds):
        return s.Integer(0)
    inter = low.kappa_psi(g,ds,m)
    return (s.Rational(inter.numerator,inter.denominator)*(2*P)**m/factorial(m)
            *4**sum(ds)*__import__('math').prod(df(2*d+1) for d in ds))


def volume(g, n):
    """Paper stack V_(g,n), a SymPy polynomial in P=pi^2."""
    return bracket(g,(0,)*n)


def sympoly(poly):
    return s.expand(sum(s.Rational(c.numerator,c.denominator)*P**k[0]
                        for k,c in poly.items()))


@lru_cache(None)
def root_raw_moment(d, k):
    z = sympoly(low.f_moment(d))
    for j in range(1,k+1):
        boundary = lm.euler_value(lm.fseries(j), j-1)
        z = s.expand((2*P)**(d+1)*boundary-(d+1)*z)
    return z


@lru_cache(None)
def root_single(d, powers):
    kd, *lows = powers
    active = [j for j,x in enumerate(lows) if x]
    if len(active)>1:
        return s.Integer(0)
    if not active:
        return root_raw_moment(d,kd)
    a = active[0]
    # Indicator of endpoint degree a, with its original signed coefficient.
    return s.Rational((-1)**a,2**a*factorial(2*a+1))*(2*P)**(d+a+1)/(d+a+1)*s.Integer(a)**kd


@lru_cache(None)
def external_moment(ds, powers):
    ds = tuple(sorted(ds))
    if not ds:
        return s.Integer(not any(powers))
    if len(ds)==1:
        return root_single(ds[0],powers)
    ans = 0
    for first in product(*(range(k+1) for k in powers)):
        mult = __import__('math').prod(comb(k,j) for k,j in zip(powers,first))
        remain = tuple(k-j for k,j in zip(powers,first))
        ans += mult*root_single(ds[0],first)*external_moment(ds[1:],remain)
    return s.expand(ans)


x, a0, a1, a2 = s.symbols('external_degree external_zero external_one external_two')


@lru_cache(None)
def averaged_root_correction(q, b, order):
    c = s.Rational(q+b,2)
    nn = 2*lm.p+b
    total_D = pf.D+x
    total_Q = 2*lm.p-lm.z0+b-a0
    delta = pf.delta(nn,total_D,total_Q)
    v1 = s.Rational(q*(q+5),4)+(lm.p+c)/2+lm.c1(nn)
    if order == 1:
        result = lm.signed_sum(v1-delta/2)
    elif order == 2:
        c20 = s.Rational(145,288)-s.Rational(395,72)/P+s.Rational(1513,72)/P**2
        c2 = c20+lm.cusp_and_c2_difference()[3].subs(pf.n,nn)
        aq1 = s.Rational(q*(q+5),4)
        aq2 = (aq1**2+sum(s.Rational(j+2,2)**2 for j in range(1,q+1)))/2
        v2 = aq2+s.Rational(3,8)*(lm.p+c)**2+s.Rational(3,2)*(lm.p+c)*lm.c1(nn)+c2
        v2 += aq1*((lm.p+c)/2+lm.c1(nn))
        e2 = pf.profile_potential()[0].subs({pf.n:nn,pf.D:total_D,pf.Q:total_Q,
                pf.m1:lm.z1+a1,s.Symbol('m2',integer=True):lm.z2+a2}, simultaneous=True)
        result = lm.signed_sum(v2-(s.Rational(q+2,4)+v1/2)*delta+e2/4)
    else:
        raise ValueError(order)
    assert not result.has(lm.S), result
    return s.Poly(s.expand(result),x,a0,a1,a2)


def integrate_block(gs, matrix, correction=None):
    edges, integrand = low.core_integrand(gs,matrix)
    total = 0
    for powers, coeff in integrand.items():
        term = s.Rational(coeff.numerator,coeff.denominator)*P**powers[0]
        root_ds = []
        for (aa,bb), d in zip(edges,powers[1:]):
            if aa==0 or bb==0:
                root_ds.append(d)
            else:
                term *= (2*P)**(d+1)/s.Integer(d+1)
        if correction is None:
            weighted = external_moment(tuple(root_ds),(0,0,0,0))
        else:
            weighted = sum(coef*external_moment(tuple(root_ds),ps)
                           for ps,coef in correction.terms())
        total += term*weighted
    return s.factor(total/low.automorphism_formula(gs,matrix))


def run():
    assert psi(1,(1,))==F(1,24)
    assert psi(2,(4,))==F(1,1152)
    assert low.kappa_psi(1,(0,0),2)==F(1,8)
    print('Independent kappa_1^4 on M_2,1:',low.kappa_psi(2,(0,),4),flush=True)
    result={'method':'Exact DVV + partition inversion + all core enumeration + signed root moments; no final coefficient target is input',
            'blocks':{},'counts':{},'rows':[]}
    for q,order in [(1,2),(2,1),(3,0),(2,2),(3,1),(4,0)]:
        cores = low.enumerate_cores(q)
        result['counts'][str(q)] = len(cores)
        total = 0
        print('START',q,order,'core count',len(cores),flush=True)
        for number,(gs,matrix) in enumerate(cores,1):
            b=sum(matrix[0])
            assert (q+b)%2==0
            correction = averaged_root_correction(q,b,order) if order else None
            value = s.factor(integrate_block(gs,matrix,correction)/(8*P)**q)
            total += value
            result['rows'].append({'q':q,'order':order,'number':number,
                'small_genera':gs,'edge_matrix':matrix,'aut':low.automorphism_formula(gs,matrix),
                'value':str(value)})
            if number%10==0:
                print('progress',q,number,flush=True)
        total = s.factor(total)
        result['blocks'][f'Q{q}{order}']=str(s.expand(total))
        print('RESULT',q,order,total,flush=True)
        (HERE/'higher_blocks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('All partial blocks completed',flush=True)


if __name__=='__main__':
    run()
