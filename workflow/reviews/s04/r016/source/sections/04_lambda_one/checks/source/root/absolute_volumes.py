"""Identify absolute c_r without a proposed high Hodge or volume coefficient."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent))
import asymptotic_inputs as a
s,P,n,D,M=a.s,a.P,a.n,a.D,a.M


def cusp_increment(registry,order):
    """c_order(n+1)-c_order(n), using only C_order and lower absolute volumes."""
    # Inverse genus = 2/(k+2-n); coefficients in z=1/k.
    inv_genus=[s.Integer(0)]+[2*(-(2-n))**(j-1) for j in range(1,order+1)]
    powers=[[s.Integer(1)]+[s.Integer(0)]*order]
    for j in range(1,order+1):
        powers.append(a.mul(powers[-1],inv_genus,order))
    left=[s.Integer(1)]+[s.Integer(0)]*order
    right=left[:]
    for j in range(1,order):
        left=a.add(left,[x*registry.volumes[j] for x in powers[j]],order)
        right=a.add(right,[x*registry.volumes[j].subs(n,n+1)
                           for x in powers[j]],order)
    lower=a.mul(left,a.inverse(right,order),order)[order]
    return s.expand((lower-registry.C[order])/2**order)


def adjacent_genus_series(c2,c3,b2,order):
    """Exact 1/[C2(k)*C3(k+1)*B2(k+2)]."""
    den=a.mul(c2,a.shift(c3,1,order),order)
    den=a.mul(den,a.shift(b2,2,order),order)
    return a.inverse(den,order)


def identify_absolute(registry,order,ratios_at_two=None):
    """Identify c_order(2) at order+1 and sum the exact cusp increment."""
    depth=order+1
    if ratios_at_two is None:
        ratios_at_two=(
            registry.c_series(2,depth),registry.c_series(3,depth),
            registry.b_series(2,depth))
    exact=adjacent_genus_series(*ratios_at_two,depth)[depth]
    # Set c_order(2)=0 to find the known part. An order+1 coefficient
    # cancels identically, so it need not be introduced.
    ca=[s.Integer(1)]+[
        registry.volumes[j].subs(n,2)*2**j if j<order else s.Integer(0)
        for j in range(1,depth+1)]
    root=[s.binomial(-s.Rational(1,2),j)*2**j for j in range(depth+1)]
    model=a.mul(root,a.mul(a.shift(ca,2,depth),a.inverse(ca,depth),depth),depth)
    c_at_two=s.expand((model[depth]-exact)/(order*2**(order+1)))
    inc=cusp_increment(registry,order)
    accumulated=a.poly_sum(inc,n,n)
    base=s.expand(c_at_two-accumulated.subs(n,2))
    result=s.expand(base+accumulated)
    registry.volumes[order]=result
    return result,inc,c_at_two


def baseline_check():
    reg=a.initial_registry()
    c2=reg.c_series(2,2)+[
        -(11*P**3-138*P**2+792*P-2016)/(96*P**3)]
    c3=reg.c_series(3,2)+[
        -(41*P**3-324*P**2-336*P-4608)/(288*P**3)]
    b2=reg.b_series(2,2)+[
        -(86*P**3+663*P**2-2052*P+6192)/(144*P**3)]
    before=reg.volumes[2]
    got,inc,c22=identify_absolute(reg,2,(c2,c3,b2))
    assert s.factor(got-before)==0,s.factor(got-before)
    print("General absolute-volume elimination reproduces c2(n).",flush=True)
    print("c2(0)=",s.factor(got.subs(n,0)),flush=True)


if __name__=="__main__":
    baseline_check()
