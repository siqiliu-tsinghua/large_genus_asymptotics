"""Finite exact reconstruction of c_2(0), not using a predicted c_2 value.

Use W26's proved second normalized profile, then one further coefficient
of the exact MZ adjacent-degree recursion.  Finally use dilaton and the
genus recursion to identify the absolute volume coefficient.
All algebra is rational in the internal variable P=pi**2.
"""
from pathlib import Path
from functools import lru_cache
import sys
sys.dont_write_bytecode = True
from runtime import OUTPUT, require_symbolic
require_symbolic()
import wp_profiles as pf
import sympy as s
P=pf.P
ell=s.Symbol('ell',integer=True,nonnegative=True)
t=s.Symbol('t',integer=True,nonnegative=True)
d=s.Symbol('d',integer=True,nonnegative=True)
eps=s.Symbol('eps')
pot,bulk,qpart,onecoef,twocoef=pf.profile_potential()
m2=s.Symbol('m2',integer=True)

def trunc(expr,k=7):
    return s.Add(*(c*eps**power[0] for power,c in s.Poly(s.expand(expr),eps).terms() if power[0]<k))

rp=[s.Integer(1)]
r=s.Add(*(s.binomial(s.Rational(1,2),j)*eps**j for j in range(1,7)))
for j in range(1,7): rp.append(trunc(rp[-1]*r))
ww=trunc((2+3*r+rp[2])*(1+P*rp[2]/6+7*P**2*rp[4]/360+31*P**3*rp[6]/15120))
bb=trunc(1-P*rp[2]/2+P**2*rp[4]/24-P**3*rp[6]/720
         -trunc(sum((-1)**(j-1)*rp[j] for j in range(1,7))*(1-P*rp[2]/6+P**2*rp[4]/120-P**3*rp[6]/5040)))

@lru_cache(None)
def stirling(j,k):
    if j==k==0:return 1
    if j==0 or k==0:return 0
    return k*stirling(j-1,k)+stirling(j-1,k-1)

def moment_list(expr,n):
    return [s.expand(sum(stirling(j,k)*s.factorial(k)*expr.coeff(eps,k) for k in range(j+1))) for j in range(n+1)]

wmom=moment_list(ww,5)
bmom=moment_list(bb,6)
theta=[s.Integer(1)]
for j in range(1,8):
    theta.append(s.expand(-sum((-P)**k/s.factorial(2*k+1)*theta[j-k] for k in range(1,j+1))))
w=[theta[j]-(theta[j-1] if j else 0) for j in range(len(theta))]
bd=[s.Integer(0)]+[2*(-1)**(j-1)*j*P**j/s.factorial(2*j+1) for j in range(1,8)]

def avg(poly,var,moments):
    poly=s.Poly(s.expand(poly),var)
    assert poly.degree()<len(moments),(poly.degree(),poly.as_expr())
    return s.expand(sum(c*moments[pow_[0]] for pow_,c in poly.terms()))

def subst(expr,nv,Dv,Qv,m1v=0,m2v=0):
    return s.expand(expr.subs({pf.n:nv,pf.D:Dv,pf.Q:Qv,pf.m1:m1v,m2:m2v}))

def dg(nv,x,exact=False):
    if exact and x==0:return s.Integer(0)
    return s.expand(pf.delta(nv,x,1))

def eg(nv,x,exact=False):
    if exact and x==0:return s.Integer(0)
    return subst(pot,nv,x,1,int(x==1) if exact else 0,int(x==2) if exact else 0)

def dpair(nv,x,exact=False):
    if exact and x<=0:return s.Integer(0)
    return s.expand(2*dg(nv,x)+(x-1)*pf.delta(nv,x,2))

def epair(nv,x,exact=False):
    if exact and x==0:return s.Integer(0)
    if exact and x==1:return 2*eg(nv,1,True)
    if exact and x==2:return 2*eg(nv,2,True)+subst(pot,nv,2,2,2,0)
    return s.expand(2*eg(nv,x)+(x-1)*subst(pot,nv,x,2)
                    +2*onecoef.subs({pf.n:nv,pf.Q:2})+2*twocoef.subs({pf.n:nv,pf.Q:2}))

def baverage_one(poly, actual):
    out=avg(poly,d,bmom)
    for k in range(3):out+=bd[k]*(actual(k)-poly.subs(d,k))
    return s.factor(out)

@lru_cache(None)
def cusp12(nv):
    beta=baverage_one(dg(nv+1,d),lambda k:dg(nv+1,k,True))
    assert s.factor(beta-pf.beta(nv))==0,(nv,beta)
    eb=baverage_one(eg(nv+1,d),lambda k:eg(nv+1,k,True))
    return -beta,s.factor(beta+eb)

@lru_cache(None)
def genus12(nv):
    assert nv>=2
    split2=(3/P*(nv-2)*(1-pf.beta(nv-1))
            +s.Rational(3,2)/P*s.binomial(nv-2,2)+s.Rational(3,16))
    return -pf.alpha(nv),s.factor(eg(nv,1,True)-split2)

def weighted_patched(poly,actual_low,limit):
    out=avg(poly,ell,wmom)
    for k in range(limit+1):out+=w[k]*(actual_low(k)-poly.subs(ell,k))
    return s.expand(out)

def tail(start):return s.expand(2-sum(w[:max(0,start)]))

def sep_loss2(nv,tv,u,small,cnt,loss1):
    """Third-order contribution of a complexity-one smaller component."""
    v=tv+ell-2-u
    pol=loss1-dg(nv if u in (0,1) and small=='torus' else nv-2,v)
    childn=nv if small=='torus' else nv-2
    out=avg(pol,ell,wmom)
    if isinstance(tv,int):
        for k in range(max(0,3+u-tv)):
            vk=tv+k-2-u
            actual=0 if vk<0 else loss1-dg(childn,vk,True)
            out+=w[k]*(actual-pol.subs(ell,k))
    return s.expand(cnt*out)

@lru_cache(None)
def third_difference(nv,tv):
    """Coefficient h^-3 in profile(t)-profile(t+1), other degrees zero."""
    actual=isinstance(tv,int)
    if nv>1:
        am1,am2=cusp12(nv-1)
        cm1=1+am1; cm2=1+2*am1+am2
        k=tv+ell-1
        mpoly=cm2-(cm1+1)*dg(nv-1,k)+eg(nv-1,k)
        def ma(j):
            kk=tv+j-1
            return s.Integer(0) if kk<0 else cm2-(cm1+1)*dg(nv-1,kk,True)+eg(nv-1,kk,True)
        merge=weighted_patched(mpoly,ma, max(-1,3-tv)) if actual else avg(mpoly,ell,wmom)
        merge=(nv-1)/P*merge
    else:merge=0
    ap1,ap2=cusp12(nv+1);bn1,bn2=genus12(nv)
    cn1=1+ap1+bn1
    cn2=1+2*ap1+ap2+bn2+bn1*(1+ap1)
    k=tv+ell-2
    npoly=(k+1)*cn2-(cn1+1)*dpair(nv+1,k)+epair(nv+1,k)
    def na(j):
        kk=tv+j-2
        return s.Integer(0) if kk<0 else (kk+1)*cn2-(cn1+1)*dpair(nv+1,kk,True)+epair(nv+1,kk,True)
    nonsep=weighted_patched(npoly,na,max(-1,4-tv)) if actual else avg(npoly,ell,wmom)
    nonsep=2/P*nonsep
    # Smaller types of loss 2: (0,3) and (1,1), both orientations.
    sep=0
    if nv>=3:
        sep+=sep_loss2(nv,tv,0,'sphere',s.binomial(nv-1,2)/P**2,4+(4*nv-14)/P)
    sep+=sep_loss2(nv,tv,0,'torus',s.Rational(1,12)/P,4)
    sep+=sep_loss2(nv,tv,1,'torus',s.Rational(1,2)/P**2,4)
    # Smaller types of loss 3: (0,4) and (1,2).
    T=lambda shift:tail(shift-tv) if actual else s.Integer(2)
    sep+=s.binomial(nv-1,3)*(T(2)/(2*P**2)+3*T(3)/P**3)
    sep+=(nv-1)*(T(2)/(16*P)+T(3)/(2*P**2)+s.Rational(5,2)*T(4)/P**3)
    return s.factor(merge+nonsep+sep)

@lru_cache(None)
def third_one_potential(nv):
    generic=third_difference(nv,t)
    pol=s.Poly(generic,t)
    assert pol.degree()<=5
    base=-s.summation(generic,(t,0,d-1))
    corrections=[s.factor(third_difference(nv,j)-generic.subs(t,j)) for j in range(5)]
    # Show directly that the generic expression is already exact beyond cuts.
    assert s.factor(third_difference(nv,5)-generic.subs(t,5))==0
    assert s.factor(third_difference(nv,6)-generic.subs(t,6))==0
    return s.expand(base),corrections

@lru_cache(None)
def cusp123(nv):
    base,corr=third_one_potential(nv+1)
    fb=avg(base,d,bmom)-sum(corr[j]*(1-sum(bd[1:j+1])) for j in range(5))
    a1,a2=cusp12(nv)
    beta=-a1; eb=a2-beta
    return a1,a2,s.factor(-beta-2*eb+fb)

def series_shift(coeffs,shift,z):
    return 1+coeffs[0]*z+(coeffs[1]-shift*coeffs[0])*z**2+(coeffs[2]-2*shift*coeffs[1]+shift**2*coeffs[0])*z**3

def c1(nv):return -nv**2/(2*P)-(s.Rational(1,4)-s.Rational(5,2)/P)*nv+s.Rational(7,12)-s.Rational(17,6)/P

def main():
    print('w moments:',wmom,flush=True);print('b moments:',bmom,flush=True)
    print('cusp a1/a2:',{j:cusp12(j) for j in range(6)},flush=True)
    a2=cusp123(2);print('A2:',a2,flush=True)
    a3=cusp123(3);print('A3:',a3,flush=True)
    base,corr=third_one_potential(2)
    f_at_1=s.factor(base.subs(d,1)-corr[0])
    b2=genus12(2)+(s.factor(f_at_1-s.Rational(3,4)),)
    print('B2:',b2,flush=True)
    z=s.Symbol('z')
    den=series_shift(a2,0,z)*series_shift(a3,1,z)*series_shift(b2,2,z)
    den=s.series(den,z,0,4).removeO()
    coeff=s.series(1/den,z,0,4).removeO().expand()
    check1=s.factor(coeff.coeff(z,1)+1)
    check2=s.factor(coeff.coeff(z,2)-(s.Rational(3,2)-4*c1(2)))
    print('genus lower-order checks:',check1,check2,flush=True)
    assert check1==check2==0
    c22=s.factor((-s.Rational(5,2)+12*c1(2)+8*c1(2)**2-coeff.coeff(z,3))/16)
    diff=[]
    for nv in range(2):
        dc=c1(nv)-c1(nv+1)
        diff.append(s.factor(-cusp12(nv)[1]/4-(s.Rational(2-nv,2)+c1(nv+1))*dc))
    c20=s.factor(c22-sum(diff))
    print('c2(2):',c22,flush=True);print('c2(0):',c20,flush=True)
    expected=s.Rational(145,288)-s.Rational(395,72)/P+s.Rational(1513,72)/P**2
    print('Post-reconstruction cross-check:',s.factor(c20-expected),flush=True)

if __name__=='__main__':main()
