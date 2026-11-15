"""Independent guards for the exact preparation calculations.

Symbolic identities are the proof calculations.  The direct finite-kernel
numerical sum is an additional transcription/aggregation check, not a proof
or a source of any coefficient.
"""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from runtime import OUTPUT, require_symbolic
require_symbolic()
import sympy as sp
import mpmath as mp
from wp_profiles import (P,n,D,Q,m1,moments,delta,profile_potential,
                     e_h_tuple,e_g_tuple,B_h_tuple)
from loop_moments import p,z0,S,signed_sum,cusp_and_c2_difference


def kernel_guard():
    x=sp.Symbol('x')
    h=sp.sqrt(P)*(sp.sqrt(1+x)-1)
    wseries=sp.series(x*sp.sqrt(P)*sp.sqrt(1+x)/sp.sin(h),x,0,4).removeO().expand()
    from sympy.functions.combinatorial.numbers import stirling
    for r in range(4):
        value=sum(stirling(r,j,kind=2)*sp.factorial(j)*wseries.coeff(x,j) for j in range(r+1))
        assert sp.factor(value-moments[r])==0


def direct_B(degrees,i,cutoff=80):
    """Direct W26 C.2, retaining actual child tuples and all split pairs."""
    pp=mp.pi**2;aa=1/pp
    def th(l):return 2*(1-mp.power(2,1-2*l))*mp.zeta(2*l) if l else mp.mpf(1)
    ww=[mp.mpf(1)]+[th(l)-th(l-1) for l in range(1,cutoff+1)]
    def tail(j):return mp.fsum(ww[max(0,j):])
    def de(ds):
        nn=len(ds);dd=sum(ds);qq=sum(d>0 for d in ds)
        return (2*dd**2+(2*nn-5)*dd+mp.mpf(qq*(qq+5-2*nn))/2)/pp
    def be(nn):return (4-2*nn)/pp-mp.mpf(1)/2
    def al(nn):return (4*nn-6)/pp
    nn=len(degrees);tt=degrees[i];rest=[d for j,d in enumerate(degrees) if j!=i]
    ans=mp.mpf(0)
    for j,dj in enumerate(rest):
        for l in range(max(0,1-tt-dj),cutoff+1):
            child=rest[:j]+rest[j+1:]+[tt+dj+l-1]
            ans+=aa*(2*dj+1)*ww[l]*(1-be(nn-1)-de(child))
    for l in range(max(0,2-tt),cutoff+1):
        degree=tt+l-2
        for u in range(degree+1):
            child=rest+[u,degree-u]
            ans+=2*aa*ww[l]*(1-be(nn+1)-al(nn)-de(child))
    zz=rest.count(0)
    ans+=aa**2*((mp.mpf(zz*(zz-1))/2+(pp/6)/2)*tail(2-tt)+tail(3-tt)/2)
    return ans


if __name__=='__main__':
    kernel_guard()
    profile_potential() # Verifies all four exact symbolic pivot identities.
    ds=sp.Symbol('degree',integer=True,positive=True)
    # MZ's printed one-positive polynomial, only used as a check.
    printed=(ds**4/(2*P**2)-13*ds**3/(6*P**2)
             -(1/(2*P)-sp.Rational(27,8)/P**2)*ds**2
             +(1/(24*P)-sp.Rational(59,24)/P**2)*ds
             +sp.Rational(1,64)-1/(4*P)+sp.Rational(19,8)/P**2)
    for d in range(3,9):assert sp.factor(e_g_tuple((0,d))-printed.subs(ds,d))==0
    assert sp.factor(e_g_tuple((0,1))-printed.subs(ds,1)+(P+5)/(8*P**2))==0
    assert sp.factor(e_g_tuple((0,2))-printed.subs(ds,2)+5/(8*P**2))==0
    for k,value in [(1,0),(2,0),(3,P/2),(4,3*P/4)]:
        assert sp.factor(signed_sum((D+p)**k)-value)==0
    assert sp.factor(signed_sum(z0)-8)==0
    assert sp.factor(signed_sum(z0**2)-(72+2*P))==0
    mp.mp.dps=100
    cases=[(0,),(1,),(2,),(4,),(0,0),(0,3),(1,1),(1,2),(2,2),
           (0,1,2),(0,2,4),(0,0,1,2,5)]
    maxerr=mp.mpf(0);count=0
    for ds0 in cases:
        for i in range(len(ds0)):
            exact=mp.mpf(str(sp.N(B_h_tuple(ds0,i).subs(P,sp.pi**2),95)))
            err=abs(direct_B(list(ds0),i)-exact)
            assert err<mp.mpf('1e-35'),(ds0,i,mp.nstr(err,10))
            maxerr=max(maxerr,err);count+=1
            nxt=list(ds0);nxt[i]+=1
            assert sp.factor(e_h_tuple(tuple(nxt))-e_h_tuple(ds0)+B_h_tuple(ds0,i))==0
    out={'symbolic_kernel_moments':'passed','symbolic_profile_pivots':'passed',
         'MZ_one_positive_and_low_exceptions':'passed','signed_loop_marginals':'passed',
         'direct_C2_numeric_cases':count,'direct_C2_cutoff':80,
         'direct_C2_max_abs_error':mp.nstr(maxerr,12),
         'warning':'Numerical guard is not used to prove or determine coefficients.'}
    (OUTPUT / 'profile_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out,indent=2))
