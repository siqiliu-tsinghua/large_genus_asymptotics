"""Exact all-order ratio helpers. No proposed Hodge coefficients are inputs."""
from pathlib import Path
from functools import lru_cache
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "build/s04-higher-check/math"))
import finite_functional as ff
s, P, n, D = ff.s, ff.P, ff.N, ff.DD
M = s.symbols("m0:25", integer=True)
h = ff.h
ell = s.Symbol("ell", integer=True, nonnegative=True)
z = s.Symbol("z")


def clean(x):
    return s.expand(x)


def add(a, b, order):
    return [clean((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) for i in range(order + 1)]


def mul(a, b, order):
    return [clean(sum(a[j] * b[i-j] for j in range(i+1)
                      if j < len(a) and i-j < len(b))) for i in range(order+1)]


def shift(a, offset, order):
    """Change a series at k to k+offset; entries are coefficients of k^-j."""
    ans = [s.sympify(a[0])] + [s.Integer(0)] * order
    for r in range(1, min(len(a), order+1)):
        for j in range(r, order+1):
            ans[j] += a[r] * s.binomial(-r, j-r) * offset**(j-r)
    return [clean(x) for x in ans]


def inverse(a, order):
    assert a[0] == 1
    ans = [s.Integer(1)]
    for j in range(1, order+1):
        ans.append(clean(-sum(a[k] * ans[j-k] for k in range(1, j+1))))
    return ans


def binom(x, k):
    return s.prod(x-i for i in range(k)) / s.factorial(k)


@lru_cache(None)
def stirling(j, k):
    if j == k == 0:
        return 1
    if j == 0 or k == 0:
        return 0
    return k * stirling(j-1, k) + stirling(j-1, k-1)


@lru_cache(None)
def theta_values(order):
    ans = [s.Integer(1)]
    for j in range(1, order+1):
        ans.append(clean(-sum((-P)**k / s.factorial(2*k+1) * ans[j-k]
                              for k in range(1, j+1))))
    return tuple(ans)


def mu_value(j):
    if j < 0:
        return s.Integer(0)
    vals = theta_values(j)
    return clean(vals[j] - (vals[j-1] if j else 0))


def nu_value(d):
    return (2 * (-1)**(d-1) * d * P**d / s.factorial(2*d+1)
            if d >= 1 else s.Integer(0))


@lru_cache(None)
def moments(order=12):
    """Euler moments of mu and nu, using Taylor series at z=1."""
    one = [s.Integer(1)] + [s.Integer(0)]*order
    rr = [s.Integer(0)] + [s.binomial(s.Rational(1, 2), j)
                           for j in range(1, order+1)]
    rp = [one]
    for j in range(1, order+2):
        rp.append(mul(rp[-1], rr, order))
    th = theta_values(order//2+1)
    sinc_inv = [s.Integer(0)]*(order+1)
    cosine = [s.Integer(0)]*(order+1)
    sinc = [s.Integer(0)]*(order+1)
    for j in range(order//2+1):
        sinc_inv = add(sinc_inv, [th[j]*a for a in rp[2*j]], order)
        cosine = add(cosine, [(-P)**j/s.factorial(2*j)*a for a in rp[2*j]], order)
        sinc = add(sinc, [(-P)**j/s.factorial(2*j+1)*a for a in rp[2*j]], order)
    pref = add(add([2*a for a in one], [3*a for a in rr], order), rp[2], order)
    ww = mul(pref, sinc_inv, order)
    inv1r = [s.Integer(0)]*(order+1)
    for j in range(order+1):
        inv1r = add(inv1r, [(-1)**j*a for a in rp[j]], order)
    bb = add(cosine, [-a for a in mul(mul(rr, sinc, order), inv1r, order)], order)
    def euler_moments(coeffs):
        return tuple(clean(sum(stirling(j,k)*s.factorial(k)*coeffs[k]
                               for k in range(j+1))) for j in range(order+1))
    return euler_moments(ww), euler_moments(bb)


def average(poly, var, table):
    q = s.Poly(s.expand(poly), var)
    if q.is_zero:
        return s.Integer(0)
    assert q.degree() < len(table), (q.degree(), len(table))
    return clean(sum(c * table[powers[0]] for powers,c in q.terms()))


def kernel_sum(poly, var=ell, actual=None, low_end=-1):
    """Infinite mu average of a polynomial, optionally correcting l=0..low_end."""
    q = s.Poly(s.expand(poly), var)
    deg = max(0, q.degree()) if not q.is_zero else 0
    ans = average(poly, var, moments(max(12, deg))[0])
    if actual is not None:
        for j in range(low_end+1):
            ans += mu_value(j) * (actual(j) - poly.subs(var, j))
    return clean(ans)


def poly_sum(poly, var, upper):
    """Sum a polynomial over integer var=0,...,upper-1, polynomially continued."""
    q = s.Poly(s.expand(poly), var)
    ans = s.Integer(0)
    for powers,c in q.terms():
        k = powers[0]
        ans += c * (s.bernoulli(k+1, upper)-s.bernoulli(k+1, 0))/(k+1)
    return clean(ans)


def max_low(expr):
    active = [j for j,m in enumerate(M) if expr.has(m)]
    return max(active, default=0)


def profile_value(expr, nn, dd, counts):
    vals = {n:nn, D:dd}
    vals.update({m:counts.get(j,0) for j,m in enumerate(M) if expr.has(m)})
    return clean(expr.xreplace(vals))


def dilaton_average(expr, parent_n=n):
    """Average one positive degree on a tuple of length parent_n+1."""
    a = max_low(expr)
    generic = profile_value(expr, parent_n+1, D, {0:parent_n})
    ans = average(generic, D, moments(max(12,s.degree(generic,D) or 0))[1])
    for d in range(1,a+1):
        actual = profile_value(expr, parent_n+1, d, {0:parent_n,d:1})
        ans += nu_value(d)*(actual-generic.subs(D,d))
    return clean(ans)


class InputRegistry:
    def __init__(self, profiles=None):
        self.profiles = dict(ff.canonical_profiles() if profiles is None else profiles)
        self.C = {0:s.Integer(1)}
        self.B = {0:s.Integer(1)}
        self.volumes = dict(ff.canonical_volumes())
        self._ratio_cache = {}

    def register_profile(self, order, expr):
        self.profiles[order] = clean(expr)

    def c_series(self, nn, order):
        assert all(r in self.C for r in range(order+1))
        return [clean(self.C[r].xreplace({n:nn})) for r in range(order+1)]

    def b_series(self, nn, order):
        assert all(r in self.B for r in range(order+1))
        return [clean(self.B[r].xreplace({n:nn})) for r in range(order+1)]

    def volume_ratio(self, j, selected, order, nn=n):
        """V_(G-j,n-selected)/V_(G,n); list [coeff k^0,...,coeff k^-order].

        j >= 0 and d=2j+selected >=0. Supports selected=-1 for nonseparating.
        """
        d = 2*j+selected
        assert j >= 0 and d >= 0
        if d > order:
            return [s.Integer(0)]*(order+1)
        depth = order-d
        key = (j,selected,order,nn)
        if key in self._ratio_cache:
            return self._ratio_cache[key]
        ans = [s.Integer(1)]+[s.Integer(0)]*depth
        for i in range(j):
            ans = mul(ans,self.b_series(nn+2*i,depth),depth)
        for t in range(1,d+1):
            ans = mul(ans,shift(self.c_series(nn+2*j-t,depth),-t,depth),depth)
            ans = mul(ans,[s.Integer(t)**r for r in range(depth+1)],depth)
        result = tuple([s.Integer(0)]*d+
                       [clean(x/(4*P)**d) for x in ans])
        self._ratio_cache[key] = result
        return result

    def compute_ratios(self, order):
        assert all(r in self.profiles for r in range(order+1))
        if order not in self.C:
            self.C[order] = clean(sum((-1)**(order-r)*s.binomial(order-1,r-1)
                                     *dilaton_average(self.profiles[r])
                                     for r in range(1,order+1)))
        if order not in self.B:
            ans = profile_value(self.profiles[order],n,1,{0:n-1,1:1})
            for j in range(order//2+1):
                for selected in range(order-2*j+1):
                    d = 2*j+selected
                    if not d or 2*j-2+(selected+2) <= 0:
                        continue
                    ans -= (12*binom(n-2,selected)*h.volume(j,selected+2) *
                            self.volume_ratio(j,selected,order)[order])
            self.B[order] = clean(ans)
        return self.C[order],self.B[order]


def initial_registry():
    ans = InputRegistry()
    for r in (1,2):
        ans.compute_ratios(r)
    return ans


def self_check():
    v = initial_registry()
    assert s.factor(v.C[1]-(s.Rational(1,2)+(2*n-4)/P)) == 0
    assert s.factor(v.B[1]+(4*n-6)/P) == 0
    target2 = (5*P**2+36*P-48)/(48*P**2)
    assert s.factor(v.C[2].subs(n,2)-target2)==0
    assert s.factor(v.B[2].subs(n,2)+(3*P**2+80*P-96)/(24*P**2))==0
    for r in (1,2):
        # Exact cusp/genus compatibility also validates continuation to n=0,1.
        rhs = mul(shift(v.b_series(n+1,r),1,r),v.c_series(n+2,r),r)
        rhs = mul(rhs,inverse(v.c_series(n,r),r),r)
        assert all(s.factor(rhs[k]-v.B[k])==0 for k in range(r+1))
    m,w = moments(12)
    assert m[:4] == (s.Integer(2),s.Rational(3,2),P/6+s.Rational(5,4),
                     5*P/8+s.Rational(9,8))
    assert w[:4] == (s.Integer(1),-s.Rational(1,2),(1-P)/4,-P/4-s.Rational(1,8))
    print("Exact helper self-checks passed.",flush=True)
    print("C2(n)=",s.factor(v.C[2]),flush=True)
    print("B2(n)=",s.factor(v.B[2]),flush=True)


if __name__=="__main__":
    self_check()
