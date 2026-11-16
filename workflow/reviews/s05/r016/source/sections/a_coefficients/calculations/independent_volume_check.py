"""Independent finite exact c2 audit, using only the admitted W26 e2 potential.

Unlike volume_coefficients.py, this builds child pair sums by literal degree enumeration,
and obtains the tail polynomial before the kernel convolution. All auxiliary
formulas below were rederived from the exact MZ/HMT recursions. The only
third-party package is the pinned workspace-local SymPy target. No file is
written by this script; run with python -B to suppress bytecode caches.
"""

from pathlib import Path
from functools import lru_cache
from math import factorial, prod
import sys
sys.dont_write_bytecode = True
from runtime import OUTPUT, require_symbolic
require_symbolic()

import wp_profiles as pf
import enumerate_cores as low
import sympy as s

P = pf.P
r, z, ell, t, d = s.symbols("r z ell t d")
m2 = s.Symbol("m2", integer=True)
potential = pf.profile_potential()[0]
potential_terms = s.Poly(s.cancel(P**2 * potential),
                         P, pf.n, pf.D, pf.Q, pf.m1, m2).terms()


def factor(x):
    return s.factor(s.expand(x))


def polynomial_average(poly, variable, moments):
    poly = s.Poly(s.expand(poly), variable)
    assert poly.degree() < len(moments)
    return factor(sum(c * moments[powers[0]] for powers, c in poly.terms()))


# Independent moments: apply the Euler operator directly in sqrt(z)-1,
# instead of using Taylor coefficients in z-1 and Stirling numbers.
wr = s.series((2 + 3*r + r**2) * s.sqrt(P)*r/s.sin(s.sqrt(P)*r), r, 0, 7).removeO()
br = s.series(s.cos(s.sqrt(P)*r) - s.sin(s.sqrt(P)*r)/(s.sqrt(P)*(1+r)),
              r, 0, 7).removeO()


def euler_moments(expression, degree):
    out = []
    for _ in range(degree + 1):
        out.append(factor(expression.subs(r, 0)))
        expression = s.expand((1+r) * s.diff(expression, r) / 2)
    return out


wmom = euler_moments(wr, 5)
bmom = euler_moments(br, 6)


@lru_cache(None)
def theta(k):
    if k == 0:
        return s.Integer(1)
    return s.expand(2 * (1 - s.Rational(2)**(1-2*k)) * s.zeta(2*k)).subs(s.pi, s.sqrt(P))


def w(k):
    return s.Integer(0) if k < 0 else theta(k) - (theta(k-1) if k else 0)


def signed_dilaton(k):
    return s.Integer(0) if k == 0 else 2*(-1)**(k-1)*k*P**k/s.factorial(2*k+1)


def degree_stats(ds):
    return len(ds), sum(ds), sum(x > 0 for x in ds), ds.count(1), ds.count(2)


def deficit(ds):
    n, D, Q, _, _ = degree_stats(ds)
    return (2*D**2 + (2*n-5)*D + s.Rational(Q*(Q+5-2*n), 2))/P


@lru_cache(None)
def e_stats(n, D, Q, m1, m2_value):
    # Evaluate the admitted W26 polynomial by exact integer statistics; no
    # imported single/pair shortcuts or low-mode patch routines are used.
    coefficients = {}
    for powers, coefficient in potential_terms:
        pp, *other_powers = powers
        value = coefficient * prod(x**power for x, power in
                                   zip((n, D, Q, m1, m2_value), other_powers))
        coefficients[pp] = coefficients.get(pp, 0) + value
    return s.Add(*(value * P**(power-2) for power, value in coefficients.items()))


def second(ds):
    return e_stats(*degree_stats(ds))


def single(n, k):
    assert n >= 1 and k >= 0
    return (k,) + (0,)*(n-1)


def pair(n, a, b):
    assert n >= 2 and a >= 0 and b >= 0
    return (a, b) + (0,)*(n-2)


@lru_cache(None)
def pair_coefficients(n, total):
    if total < 0:
        return 0, s.Integer(0), s.Integer(0)
    # Literal ordered pairs, retaining every 0,1,2 mode individually.
    profiles = [pair(n, a, total-a) for a in range(total+1)]
    return total+1, factor(sum(deficit(ds) for ds in profiles)), factor(sum(second(ds) for ds in profiles))


def interpolate_tail(values, variable, degree, start):
    result = s.interpolate([(j, values(j)) for j in range(start, start+degree+1)], variable)
    result = s.expand(result)
    assert s.degree(result, variable) <= degree
    # The degree bound is proved from W26's degree-four potential and its
    # linear m1,m2 terms; two extra exact points diagnose implementation bugs.
    for j in [start+degree+1, start+degree+2]:
        assert factor(result.subs(variable, j)-values(j)) == 0
    return result


def signed_average_single(values, degree):
    polynomial = interpolate_tail(values, d, degree, 3)
    answer = polynomial_average(polynomial, d, bmom)
    for j in range(3):
        answer += signed_dilaton(j) * (values(j)-polynomial.subs(d,j))
    return factor(answer)


@lru_cache(None)
def cusp_two(n):
    beta = signed_average_single(lambda k: deficit(single(n+1,k)), 2)
    ebar = signed_average_single(lambda k: second(single(n+1,k)), 4)
    return -beta, factor(beta+ebar)


@lru_cache(None)
def low_bracket(g, n, u):
    dimension = 3*g-3+n
    if u > dimension:
        return s.Integer(0)
    m = dimension-u
    intersection = low.kappa_psi(g, (u,)+(0,)*(n-1), m)
    double_fact = prod(range(1,2*u+2,2))
    return s.Rational(intersection.numerator,intersection.denominator) * 4**u * double_fact * (2*P)**m/s.factorial(m)


@lru_cache(None)
def genus_two(n):
    assert n >= 2
    # Exact HMT (4.2): retained small components (0,3),(0,4),(1,2).
    first_sep = 3*(n-2)/P
    second_sep = first_sep * (1+cusp_two(n-1)[0])
    second_sep += 12*s.binomial(n-2,2)*low_bracket(0,4,0)/(4*P)**2
    second_sep += 12*low_bracket(1,2,0)/(4*P)**2
    return factor(-deficit(single(n,1))-first_sep), factor(second(single(n,1))-second_sep)


def c1(n):
    return -s.Rational(n*n,2)/P-(s.Rational(1,4)-s.Rational(5,2)/P)*n+s.Rational(7,12)-s.Rational(17,6)/P


def kernel_average_literal(values, degree=3, start=3):
    polynomial = interpolate_tail(values,ell,degree,start)
    answer = polynomial_average(polynomial,ell,wmom)
    for j in range(start):
        answer += w(j)*(values(j)-polynomial.subs(ell,j))
    return factor(answer)


def source_second_difference(ds, pivot):
    """Independent literal W26(C.2) children, no B_zero/B_positive shortcut."""
    n, tv = len(ds), ds[pivot]
    others = ds[:pivot]+ds[pivot+1:]
    def raw(j):
        answer = 0
        if n >= 2:
            for position, degree in enumerate(others):
                merged_degree = tv+degree+j-1
                if merged_degree < 0:
                    continue
                child = (merged_degree,)+others[:position]+others[position+1:]
                answer += (2*degree+1)/P * (1+cusp_two(n-1)[0]-deficit(child))
        split_total = tv+j-2
        if split_total >= 0:
            for a in range(split_total+1):
                child = (a,split_total-a)+others
                answer += 2/P*(1+cusp_two(n+1)[0]-(4*n-6)/P-deficit(child))
        return factor(answer)
    result = kernel_average_literal(raw)
    tail = lambda start: s.Integer(2)-sum((w(j) for j in range(max(0,start))),s.Integer(0))
    zeros = others.count(0)
    result += ((s.binomial(zeros,2)+P/12)*tail(2-tv)+tail(3-tv)/2)/P**2
    return factor(result)


def check_profile_potential():
    samples = [(0,),(1,),(2,),(3,),(4,),
               (0,0),(1,0),(2,0),(3,0),(1,1),(2,1),(2,2),(3,2),
               (0,0,0),(1,0,0),(2,0,0),(3,0,0),(1,1,0),(2,1,0),(2,2,0),
               (3,1,1),(3,2,1),(3,3,3),
               (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0),(1,1,1,0),
               (2,2,1,0),(3,2,1,0),(3,2,1,1)]
    count = 0
    for ds in samples:
        for value in set(ds):
            pivot = ds.index(value)
            child = ds[:pivot]+(value+1,)+ds[pivot+1:]
            assert factor(second(child)-second(ds)+source_second_difference(ds,pivot)) == 0,(ds,pivot)
            count += 1
    return count


@lru_cache(None)
def raw_third(n, total):
    """Coefficient before multiplying w_ell, total=t+ell. Direct children."""
    a1m,a2m = cusp_two(n-1)
    M1 = 1+a1m
    M2 = 1+2*a1m+a2m
    a1p,a2p = cusp_two(n+1)
    b1,b2 = genus_two(n)
    N1 = 1+a1p+b1
    N2 = 1+2*a1p+a2p+b2+b1*(1+a1p)
    answer = 0
    if total >= 1:
        ds = single(n-1,total-1)
        answer += (n-1)/P * (M2-(M1+1)*deficit(ds)+second(ds))
    count, delta_sum, e_sum = pair_coefficients(n+1,total-2)
    answer += 2/P * (count*N2-(N1+1)*delta_sum+e_sum)
    # Small type: genus a, s assigned old zeros, node degree u.
    # Both orientations give 16. Enumerate the low types and their actual
    # brackets; derive L from c1 differences instead of supplying a formula.
    for a, assigned in [(0,2),(1,0),(0,3),(1,1)]:
        if assigned > n-1:
            continue
        loss = 2*a+assigned
        small_n = assigned+1
        dimension = 3*a-3+small_n
        for u in range(dimension+1):
            v = total-2-u
            if v < 0:
                continue
            coefficient = 16*s.binomial(n-1,assigned)*low_bracket(a,small_n,u)/(4*P)**loss
            if loss == 2:
                L = 3+a+2*(c1(n-assigned)-c1(n))
                answer += coefficient*(L-deficit(single(n-assigned,v)))
            else:
                assert loss == 3
                answer += coefficient
    return factor(answer)


@lru_cache(None)
def third_difference_polynomial(n):
    raw = interpolate_tail(lambda k: raw_third(n,k), z, 5, 5)
    J = polynomial_average(raw.subs(z,t+ell), ell, wmom)
    low_raw = [factor(raw_third(n,j)-raw.subs(z,j)) for j in range(5)]
    corrections = [factor(sum(w(j-tv)*low_raw[j] for j in range(tv,5))) for tv in range(5)]
    return raw, J, corrections


def third_difference_at(n, tv):
    _,J,corrections = third_difference_polynomial(n)
    return factor(J.subs(t,tv)+(corrections[tv] if tv<5 else 0))


def third_profile_average(n):
    _,J,corrections = third_difference_polynomial(n)
    primitive = -s.summation(J,(t,0,d-1))
    average = polynomial_average(primitive,d,bmom)
    for j,correction in enumerate(corrections):
        average -= correction*(1-sum(signed_dilaton(i) for i in range(1,j+1)))
    return factor(average)


def cusp_three(n):
    a1,a2 = cusp_two(n)
    beta = -a1
    ebar = a2-beta
    return (a1,a2,factor(-beta-2*ebar+third_profile_average(n+1)))


def shifted(coefficients, shift):
    a,b,c = coefficients
    return [s.Integer(1),a,b-shift*a,c-2*shift*b+shift**2*a]


def multiply(a,b):
    return [factor(sum(a[j]*b[k-j] for j in range(k+1))) for k in range(4)]


def main():
    for n in range(1,6):
        assert deficit(single(n,0)) == second(single(n,0)) == 0
    profile_check_count = check_profile_potential()
    ratios = {"A2":cusp_three(2),"A3":cusp_three(3)}
    b1,b2 = genus_two(2)
    ratios["B2"] = (b1,b2,factor(-third_difference_at(2,0)-s.Rational(3,4)))
    den = multiply(multiply(shifted(ratios["A2"],0),shifted(ratios["A3"],1)),shifted(ratios["B2"],2))
    reciprocal = [s.Integer(1)]
    for k in range(1,4):
        reciprocal.append(factor(-sum(den[j]*reciprocal[k-j] for j in range(1,k+1))))
    assert factor(reciprocal[1]+1) == 0
    assert factor(reciprocal[2]-(s.Rational(3,2)-4*c1(2))) == 0
    c22 = factor((-s.Rational(5,2)+12*c1(2)+8*c1(2)**2-reciprocal[3])/16)
    increments = []
    for n in range(2):
        difference = c1(n)-c1(n+1)
        increments.append(factor(-cusp_two(n)[1]/4-((2-n)/s.Integer(2)+c1(n+1))*difference))
    c20 = factor(c22-sum(increments))
    print("Independent Euler moments w:",wmom)
    print("Independent Euler moments b:",bmom)
    print("Literal low brackets:",{(g,n):[low_bracket(g,n,u) for u in range(3*g-3+n+1)] for g,n in [(0,3),(1,1),(0,4),(1,2)]})
    print("Literal W26(C.2) profile increment checks:",profile_check_count)
    print("Independent ratio rows:",ratios)
    print("Adjacent normalized genus coefficients:",reciprocal)
    print("c2 increments n0,n1:",increments)
    print("Independent c2(2):",c22)
    print("Independent c2(0):",c20)
    # Post-computation comparison with the coordinator's output, not an input.
    assert factor(c20-(145*P**2-1580*P+6052)/(288*P**2)) == 0
    print("All exact independent checks passed.")


if __name__ == "__main__":
    main()
