"""Exact specialization of W26 (7.5), (7.7), (C.1)--(C.4) at Y=0.

P is an internal formal variable representing pi**2.  No manuscript
notation is proposed.  The trailing -1/2 in beta is OUTSIDE A's braces.
"""
from pathlib import Path
from functools import lru_cache
import sys
sys.dont_write_bytecode = True
from runtime import OUTPUT, require_symbolic
require_symbolic()
import sympy as sp

P = sp.Symbol("P", positive=True)
A = 1 / P
ell = sp.Symbol("ell", integer=True, nonnegative=True)
n, D, Q, t, m1 = sp.symbols("n D Q t m1", integer=True)
moments = [sp.Integer(2), sp.Rational(3, 2),
           sp.Rational(5, 4) + P / 6,
           sp.Rational(9, 8) + 5 * P / 8]
w = [sp.Integer(1), P / 6 - 1, 7 * P**2 / 360 - P / 6]
theta1 = P / 6


def beta(n):
    return (4 - 2*n)/P - sp.Rational(1, 2)


def alpha(n):
    return (4*n - 6)/P


def F(n, Q):
    return sp.Rational(1,2)*sp.sympify(Q)*(Q + 5 - 2*n)


def delta(n, D, Q):
    return (2*D**2 + (2*n - 5)*D + F(n, Q))/P


def kernel_sum(poly, start=0):
    """sum_{ell >= start} w_ell poly(ell), with start <= 3."""
    poly = sp.Poly(sp.expand(poly), ell)
    assert poly.degree() <= 3
    ans = sum(coef*moments[pow_[0]] for pow_,coef in poly.terms())
    for k in range(start):
        ans -= w[k]*poly.as_expr().subs(ell, k)
    return sp.expand(ans)


def tail(start):
    return moments[0] - sum(w[:max(0, start)])


@lru_cache(None)
def B_positive(t_value):
    """Pivot t>=1; symbolic t represents t>=3."""
    z = n-Q
    base = 1-beta(n-1)
    merge = z*kernel_sum(base-delta(n-1, D+ell-1, Q))
    merge += (2*(D-t)+Q-1)*kernel_sum(base-delta(n-1, D+ell-1, Q-1))
    if t_value == 1:
        merge += z*(F(n-1,Q)-F(n-1,Q-1))/P

    split_degree = t+ell-2
    X = D+ell-2
    qgeneric = Q+1
    split_delta = ((split_degree+1)*(2*X**2+(2*n-3)*X+F(n+1,qgeneric))
                   +2*(F(n+1,qgeneric-1)-F(n+1,qgeneric)))/P
    start = max(0, 2-t_value) if isinstance(t_value,int) else 0
    nonsep_poly = (split_degree+1)*(1-beta(n+1)-alpha(n))-split_delta
    nonsep = kernel_sum(nonsep_poly, start)
    if t_value in (1,2):
        nonsep -= w[2-t_value]/P
    sep = ((z*(z-1)/2+theta1/2)*tail(2-t_value)
           +tail(3-t_value)/2) if isinstance(t_value,int) else (z*(z-1)/2+theta1/2+sp.Rational(1,2))*2
    ans=A*merge+2*A*nonsep+A**2*sep
    return sp.factor(ans.subs(t,t_value)) if isinstance(t_value,int) else sp.factor(ans)


@lru_cache(None)
def B_zero():
    z=n-1-Q
    base=1-beta(n-1)
    merge=(2*D+Q)*kernel_sum(base-delta(n-1,D+ell-1,Q))
    merge+=3*m1*(F(n-1,Q)-F(n-1,Q-1))/P
    merge+=z*kernel_sum(base-delta(n-1,D+ell-1,Q+1),1)
    merge+=z*w[1]*(F(n-1,Q+1)-F(n-1,Q))/P
    X=D+ell-2; N=ell-2; qgeneric=Q+2
    split_delta=((N+1)*(2*X**2+(2*n-3)*X+F(n+1,qgeneric))
                 +2*(F(n+1,qgeneric-1)-F(n+1,qgeneric)))/P
    nonsep=kernel_sum((N+1)*(1-beta(n+1)-alpha(n))-split_delta,2)-w[2]/P
    sep=(z*(z-1)/2+theta1/2)*tail(2)+tail(3)/2
    return sp.factor(A*merge+2*A*nonsep+A**2*sep)


@lru_cache(None)
def profile_potential():
    """Recover e_n(d) by discrete integration, checking every pivot case."""
    m2=sp.Symbol("m2",integer=True)
    j=sp.Symbol("j",integer=True,nonnegative=True)
    bg=B_positive(t)
    assert sp.diff(bg,t)==0
    bulk=sp.summation(-bg.subs(D,j),(j,0,D-1)).expand()
    corr1=sp.factor(B_positive(1)-bg)
    corr2=sp.factor(B_positive(2)-bg)
    a2=corr2
    a1=sp.factor(a2+corr1)
    shift0=sp.expand(bulk.subs({D:D+1,Q:Q+1},simultaneous=True)-bulk
                     +(a1.subs(Q,Q+1)-a1)*m1+a1.subs(Q,Q+1))
    need=sp.factor(-B_zero()-shift0)
    assert not need.has(D,m1), need
    constant=sp.summation(need.subs(Q,j),(j,0,Q-1)).expand()
    ans=sp.factor(bulk+constant+a1*m1+a2*m2)
    for tv in [0,1,2,3]:
        changes={D:D+1}
        if tv==0: changes.update({Q:Q+1,m1:m1+1})
        if tv==1: changes.update({m1:m1-1,m2:m2+1})
        if tv==2: changes.update({m2:m2-1})
        diff=sp.expand(ans.subs(changes,simultaneous=True)-ans)
        assert sp.factor(diff+(B_zero() if tv==0 else B_positive(tv)))==0,tv
    return ans,sp.factor(bulk),sp.factor(constant),a1,a2


def stats(degrees):
    degrees=tuple(degrees)
    assert degrees and all(isinstance(d,int) and d>=0 for d in degrees)
    return {n:len(degrees),D:sum(degrees),Q:sum(d>0 for d in degrees),
            m1:degrees.count(1),sp.Symbol("m2",integer=True):degrees.count(2)}


def delta_h_tuple(degrees):
    """Positive first correction: profile = 1-delta/h+e/h**2, h=2G-2+n."""
    ss=stats(degrees)
    return sp.factor(delta(n,D,Q).subs(ss))


def e_h_tuple(degrees):
    """W26 (C.4) coefficient of h**-2, with all low-degree exceptions."""
    return sp.factor(profile_potential()[0].subs(stats(degrees)))


def e_g_tuple(degrees):
    """Coefficient of G**-2 in normalized descendant at vertex genus G."""
    return sp.factor((e_h_tuple(degrees)+(len(degrees)-2)*delta_h_tuple(degrees))/4)


def B_h_tuple(degrees,pivot):
    """W26 (C.2): e(d+unit_pivot)-e(d)=-B, NOT the negative increment."""
    degrees=tuple(degrees)
    tv=degrees[pivot]
    expr=B_zero() if tv==0 else B_positive(tv)
    return sp.factor(expr.subs(stats(degrees)))


if __name__ == "__main__":
    bg=B_positive(t)
    print("generic B (t>=3):",bg)
    print("t dependence:",sp.factor(sp.diff(bg,t)))
    for j in (0,1,2):
        bj=B_zero() if j==0 else B_positive(j)
        print("B"+str(j)+":",bj)
        print("correction"+str(j)+":",sp.factor(bj-bg.subs(t,j)))
    potential,bulk,constant,a1,a2=profile_potential()
    print("bulk:",bulk)
    print("Q integration:",constant)
    print("coefficient m1:",a1)
    print("coefficient m2:",a2)
    print("e_n:",potential)
