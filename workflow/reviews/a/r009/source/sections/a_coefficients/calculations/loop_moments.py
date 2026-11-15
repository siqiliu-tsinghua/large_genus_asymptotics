"""Exact signed-loop moments and the independently derived q=0 coefficients.

P denotes pi**2 internally; S denotes Cin(2*pi).  These are algebraic
indeterminates in the cache, not new manuscript constants.  The signed
functional is an exponential generating series, not a probability law.
No numerical candidate table is used to construct a result.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from math import comb, factorial
import json
import sys
sys.dont_write_bytecode = True
from runtime import OUTPUT, require_symbolic
require_symbolic()
import sympy as sp
from sympy.functions.combinatorial.numbers import stirling
from wp_profiles import P, n, D, Q, m1, delta, profile_potential

S=sp.Symbol("S")
p,z0,z1,z2=sp.symbols("p z0 z1 z2",integer=True)
C20=sp.Symbol("C20")
eps=sp.Symbol("eps")
root=sp.sqrt(1+eps)
angle=sp.sqrt(P)*(root-1)


def euler_value(series,k):
    return sp.expand(sum(stirling(k,j,kind=2)*sp.factorial(j)*series.coeff(eps,j)
                         for j in range(k+1)))


@lru_cache(None)
def fseries(order):
    # sin(pi*sqrt(z))=-sin(pi*(sqrt(z)-1)) near z=1.
    return sp.series(-sp.sin(angle)/(sp.sqrt(P)*root),eps,0,order+1).removeO().expand()


@lru_cache(None)
def dilaton_moment(k):
    return sp.factor(-2*euler_value(fseries(k+1),k+1))


def dilaton_sum(poly,var):
    q=sp.Poly(sp.expand(poly),var)
    return sp.factor(sum(coef*dilaton_moment(power[0]) for power,coef in q.terms()))


def c1(nn):
    return -nn**2/(2*P)-(sp.Rational(1,4)-sp.Rational(5,2)/P)*nn+sp.Rational(7,12)-sp.Rational(17,6)/P


@lru_cache(None)
def cusp_and_c2_difference():
    e,_,_,a1,a2=profile_potential()
    ell=sp.Symbol("degree",integer=True,positive=True)
    sub={n:n+1,D:ell,Q:1,m1:0,sp.Symbol("m2",integer=True):0}
    egeneric=e.subs(sub,simultaneous=True)
    dgeneric=delta(n+1,ell,1)
    low1=a1.subs({n:n+1,Q:1},simultaneous=True)
    low2=a2
    h1=sp.factor(-dilaton_sum(dgeneric,ell)/2)
    h2=sp.factor((dilaton_sum(egeneric+(n-1)*dgeneric,ell)
                  +(P/3)*low1-(P**2/30)*low2)/4)
    assert sp.factor(h1-(c1(n)-c1(n+1)))==0
    difference=sp.factor(-h2-c1(n+1)*h1)
    j=sp.Symbol("j",integer=True,nonnegative=True)
    c2diff=sp.factor(sp.summation(difference.subs(n,j),(j,0,n-1)))
    assert c2diff.subs(n,0)==0
    return h1,h2,difference,c2diff


@lru_cache(None)
def degree_cumulant(k):
    # L(z)=S(z)/z, S'(z)=sin(pi*sqrt(z))**2/z.
    deriv=sp.series(sp.sin(angle)**2/(1+eps),eps,0,k+1).removeO().expand()
    Sint=S+sum(deriv.coeff(eps,j)*eps**(j+1)/sp.Integer(j+1) for j in range(k))
    L=sp.series(Sint/(1+eps),eps,0,k+1).removeO().expand()
    return sp.factor(euler_value(L,k))


def sine_integral_even(j,x):
    if j==0:return 1-sp.cos(x)
    m=2*j
    return -x**m*sp.cos(x)+m*x**(m-1)*sp.sin(x)-m*(m-1)*sine_integral_even(j-1,x)


@lru_cache(None)
def side_moment(j,k):
    x=sp.Symbol("x")
    expr=sine_integral_even(j,x)
    expr=expr.subs({sp.cos(x):-sp.cos(angle),sp.sin(x):-sp.sin(angle),
                    x:sp.sqrt(P)*root},simultaneous=True)
    expr*=sp.Rational(2*(-1)**j,factorial(2*j+1))/(1+eps)
    series=sp.series(expr,eps,0,k+1).removeO().expand()
    return sp.factor(euler_value(series,k))


def loop_weight(a,b):
    return sp.Rational((-1)**(a+b), (a+b+1)*factorial(2*a+1)*factorial(2*b+1))*P**(a+b+1)


@lru_cache(None)
def cumulant(powers):
    """One-loop moment for p,D,N0,N1,N2; loop p contributes the scalar one."""
    _,kd,*lows=powers
    active=[j for j,r in enumerate(lows) if r]
    if not active:return degree_cumulant(kd)
    if len(active)>2:return sp.Integer(0)
    if len(active)==2:
        j,k=active
        return 2*loop_weight(j,k)*sp.Integer(j+k)**kd
    j=active[0];r=lows[j]
    return sp.factor(2*side_moment(j,kd)+(2**r-2)*loop_weight(j,j)*sp.Integer(2*j)**kd)


@lru_cache(None)
def moment(powers):
    """Multivariate exponential/Bell recurrence for the normalized loop EGF."""
    if not any(powers):return sp.Integer(1)
    i=next(i for i,r in enumerate(powers) if r)
    rest=list(powers);rest[i]-=1
    ans=0
    for b in product(*(range(r+1) for r in rest)):
        kap=list(b);kap[i]+=1
        left=tuple(r-v for r,v in zip(rest,b))
        factor=1
        for r,v in zip(rest,b):factor*=comb(r,v)
        ans+=factor*cumulant(tuple(kap))*moment(left)
    return sp.expand(ans)


def signed_sum(poly):
    poly=sp.Poly(sp.expand(poly),p,D,z0,z1,z2)
    return sp.factor(sum(coef*moment(powers) for powers,coef in poly.terms()))


def pure_loop_coefficients():
    c2diff=cusp_and_c2_difference()[3]
    eh=profile_potential()[0]
    sub={n:2*p,Q:2*p-z0,m1:z1,sp.Symbol("m2",integer=True):z2}
    d=delta(n,D,Q).subs(sub,simultaneous=True)
    e=eh.subs(sub,simultaneous=True)
    v1=p/2+c1(2*p)
    v2=sp.Rational(3,8)*p**2+sp.Rational(3,2)*p*c1(2*p)+C20+c2diff.subs(n,2*p)
    first=signed_sum(v1-d/2)
    second=signed_sum(v2-(1+v1)*d/2+e/4)
    assert not first.has(S) and not second.has(S)
    return first,second


if __name__=="__main__":
    h1,h2,diff,c2diff=cusp_and_c2_difference()
    print('dilaton moments:',[dilaton_moment(k) for k in range(5)])
    print('A3 first:',h1)
    print('A3 second:',h2)
    print('c2(n+1)-c2(n):',diff)
    print('c2(n)-c2(0):',c2diff)
    print('loop D cumulants:',[degree_cumulant(k) for k in range(5)])
    print('one-sided low-degree moments:',[[side_moment(j,k) for k in range(3)] for j in range(3)])
    first,second=pure_loop_coefficients()
    print('q0 absolute first:',first)
    print('q0 absolute second with c2(0) unknown:',second)
    results={'A3_first':str(h1),'A3_second':str(h2),'c2_difference':str(c2diff),
             'q0_absolute_first':str(first),'q0_absolute_second_unknown_base':str(second),
             'profile_eH':str(profile_potential()[0]),
             'notes':'P=pi**2,S=Cin(2*pi),C20=c2(0); constructed without EGGLS or old-table values.'}
    (OUTPUT / 'loop_moments.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
