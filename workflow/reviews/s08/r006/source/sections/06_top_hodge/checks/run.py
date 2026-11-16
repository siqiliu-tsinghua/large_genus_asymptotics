"""Exact finite checks for the supplementary Section 6 coefficients.

Self-contained writer algorithm; no preparation code or data is imported.
"""

import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "build" / "a-calculations" / "python-packages"))

import json
from hashlib import sha256
import sympy as sp
import mpmath as mp
from itertools import permutations, product
from heapq import heapify, heappop, heappush
from math import factorial

if sp.__version__ != "1.14.0" or mp.__version__ != "1.3.0":
    raise RuntimeError("Use SymPy 1.14.0 and mpmath 1.3.0; see checks/README.md")

X = sp.Symbol("X", positive=True)
L = sp.Symbol("L", real=True)
t = sp.Symbol("t", real=True)
z = sp.Symbol("z")
N = 9


def mul(a, b, degree):
    return [
        sp.expand(sum(a[j] * b[n - j] for j in range(n + 1)))
        for n in range(degree + 1)
    ]


def ode_coefficients(degree):
    # F(q)=w(X(1+q))/R: (1+q)F''+X F=0, F(0)=1,F'(0)=0.
    a = [sp.S.One, sp.S.Zero]
    for j in range(degree - 1):
        a.append(
            sp.expand(-(j * (j + 1) * a[j + 1] + X * a[j]) / ((j + 1) * (j + 2)))
        )
    return a


def phase_coefficients(degree):
    a = ode_coefficients(degree)
    circle_increment = [sp.S.Zero] + [
        sp.I ** j / sp.factorial(j) for j in range(1, degree + 1)
    ]
    power = [sp.S.One] + [sp.S.Zero] * degree
    W = [sp.S.Zero] * (degree + 1)
    for j, coefficient in enumerate(a):
        W = [sp.expand(x + coefficient * y) for x, y in zip(W, power)]
        power = mul(power, circle_increment, degree)
    # H=log W. Coefficients follow from W H'=W'.
    h = [sp.S.Zero]
    for n in range(1, degree + 1):
        h.append(
            sp.expand(
                W[n] - sum(j * h[j] * W[n - j] for j in range(1, n)) / n
            )
        )
    return h


def gaussian_average(poly):
    result = sp.S.Zero
    for (degree,), coefficient in sp.Poly(sp.expand(poly), t).terms():
        if degree % 2 == 0:
            result += coefficient * sp.factorial2(degree - 1) / X ** (degree // 2)
    return sp.factor(result)


def saddle_coefficients(k, h, order=3):
    # Divide amplitude by Phi(X)^k:
    # exp(-mH(theta)) A_{Phi^k}/Phi(X)^k
    # =exp(-mH+(1-k)(i theta-H)).
    delta = 1 - k
    exponent = [sp.S.Zero]
    for j in range(1, 2 * order + 2):
        value = -h[j + 2] * t ** (j + 2) - delta * h[j] * t ** j
        if j == 1:
            value += delta * sp.I * t
        exponent.append(sp.expand(value))
    exponential = [sp.S.One]
    for n in range(1, 2 * order + 2):
        exponential.append(
            sp.expand(
                sum(j * exponent[j] * exponential[n - j] for j in range(1, n + 1))
                / n
            )
        )
    for n in range(1, 2 * order + 2, 2):
        assert gaussian_average(exponential[n]) == 0
    return [gaussian_average(exponential[2 * r]) for r in range(order + 1)]


def shifted_star_series(coefficients, leaves, automorphisms, order=3):
    # m=g_2-leaves; loop weights L already contain beta_1*(2pi)^2*R*Phi(X).
    ratio = z ** leaves
    for j in range(leaves):
        ratio /= 1 - j * z
    ratio *= (1 - leaves * z) ** sp.Rational(-1, 2)
    saddle = sum(
        coefficients[r] * (z / (1 - leaves * z)) ** r
        for r in range(order - leaves + 1)
    )
    return sp.series(
        L ** leaves / automorphisms * ratio * saddle, z, 0, order + 1
    ).removeO().expand()


def labeled_trees(vertices):
    if vertices == 1:
        yield ()
        return
    for sequence in product(range(vertices), repeat=vertices - 2):
        degree = [1 + sequence.count(i) for i in range(vertices)]
        leaves = [i for i, n in enumerate(degree) if n == 1]
        heapify(leaves)
        edges = []
        for neighbor in sequence:
            leaf = heappop(leaves)
            edges.append(tuple(sorted((leaf, neighbor))))
            degree[neighbor] -= 1
            if degree[neighbor] == 1:
                heappush(leaves, neighbor)
        edges.append(tuple(sorted((heappop(leaves), heappop(leaves)))))
        yield tuple(sorted(edges))


def rooted_canonical(genera, edges):
    # Vertex zero represents the unique large-genus vertex.
    representations = []
    for rest in permutations(range(1, len(genera))):
        order = (0,) + rest
        index = {old: new for new, old in enumerate(order)}
        representations.append(
            (
                tuple(genera[i] for i in order),
                tuple(sorted(tuple(sorted((index[a], index[b]))) for a, b in edges)),
            )
        )
    canonical = min(representations)
    return canonical, representations.count(canonical)


def enumerate_cores():
    classes = {}
    # E<=3 suffices for loss<=3. A small genus>=3 already has loss>=5.
    for vertices in range(1, 5):
        for edges in labeled_trees(vertices):
            degrees = [sum(v in edge for edge in edges) for v in range(vertices)]
            for small in product(range(3), repeat=vertices - 1):
                if any(2 * g - 2 + n <= 0 for g, n in zip(small, degrees[1:])):
                    continue
                loss = len(edges) + sum(
                    2 * g - 3 + n for g, n in zip(small, degrees[1:])
                )
                if loss > 3:
                    continue
                key, aut = rooted_canonical((-1,) + small, edges)
                classes[key] = aut
    return classes


def beta_coefficients(maximum):
    # Reciprocal sine series, indexed by the even degree.
    sine = [
        sp.Rational((-1) ** j, 2 ** (2 * j) * factorial(2 * j + 1))
        for j in range(maximum + 1)
    ]
    values = [sp.S.One]
    for n in range(1, maximum + 1):
        values.append(-sum(sine[j] * values[n - j] for j in range(1, n + 1)))
    return values


def small_vertex(genus, edge_parameters, beta):
    degree = 2 * genus - 3 + len(edge_parameters)
    assert 0 <= degree <= 2
    x = sp.Symbol("vertex_x")
    phi = sum(
        sp.Rational((-1) ** j, factorial(j) * factorial(j + 1)) * x ** j
        for j in range(degree + 1)
    )
    j0_product = sp.prod(
        sum(
            sp.Rational((-1) ** j, factorial(j) ** 2) * (parameter * x) ** j
            for j in range(degree + 1)
        )
        for parameter in edge_parameters
    )
    inverse = sp.series(phi ** (-degree - 1), x, 0, degree + 1).removeO()
    return sp.expand(beta[genus] * factorial(degree) * inverse * j0_product).coeff(x, degree)


def integrate_critical_j0(polynomial, parameter, phi_star):
    # I_0=Phi(X), I_j=Phi(X)-j^2 I_(j-1)/X at J_0(2sqrt(X))=0.
    p = sp.Poly(sp.expand(polynomial), parameter)
    moments = [phi_star]
    for j in range(1, p.degree() + 1):
        moments.append(sp.expand(phi_star - j ** 2 * moments[j - 1] / X))
    return sp.factor(
        sum(coefficient * moments[degree[0]] for degree, coefficient in p.terms())
    )


def classify(genera, edges, degrees):
    edge_count = len(edges)
    if edge_count == 0:
        return "no_edge"
    if all(g == 1 and n == 1 for g, n in zip(genera[1:], degrees[1:])):
        return {1: "one_elliptic_leaf", 2: "two_elliptic_leaves", 3: "three_elliptic_leaves"}[edge_count]
    if 2 in genera[1:]:
        return "genus_two_leaf"
    if 0 in genera[1:]:
        return "rational_center_two_elliptic_leaves"
    return "elliptic_middle_and_leaf"


def reconstruct_groups(saddle):
    beta = beta_coefficients(2)
    phi_star = sp.Symbol("PhiStar", positive=True)
    groups = {}
    records = []
    for (genera, edges), aut in sorted(enumerate_cores().items()):
        degrees = [sum(v in edge for edge in edges) for v in range(len(genera))]
        loss = len(edges) + sum(
            2 * g - 3 + n for g, n in zip(genera[1:], degrees[1:])
        )
        name = classify(genera, edges, degrees)
        assert name not in groups
        record = {
            "type": name,
            "vertex_genera": ["large", *genera[1:]],
            "edges": [list(edge) for edge in edges],
            "automorphisms": aut,
            "loss": loss,
            "small_genus_total": sum(genera[1:]),
            "large_valence": degrees[0],
        }
        if name in {
            "no_edge", "one_elliptic_leaf", "two_elliptic_leaves", "three_elliptic_leaves"
        }:
            groups[name] = shifted_star_series(saddle[len(edges)], len(edges), aut)
        else:
            assert loss == 3 and degrees[0] == 1 and sum(genera[1:]) == 2
            parameters = sp.symbols("s0:" + str(len(edges)), nonnegative=True)
            small_product = sp.S.One
            for v in range(1, len(genera)):
                incident = [parameters[i] for i, edge in enumerate(edges) if v in edge]
                small_product *= small_vertex(genera[v], incident, beta)
            root_edge = next(i for i, edge in enumerate(edges) if 0 in edge)
            for i, parameter in enumerate(parameters):
                if i != root_edge:
                    small_product = sp.integrate(small_product, (parameter, 0, 1))
            amplitude = integrate_critical_j0(
                sp.expand(small_product), parameters[root_edge], phi_star
            )
            # (2pi)^4 R^3 amplitude / Aut, with R/Phi(X)=X and
            # L=beta_1*(2pi)^2*R*Phi(X). No proposed coefficient enters.
            coefficient = sp.factor(L ** 2 * X * amplitude / (beta[1] ** 2 * phi_star * aut))
            groups[name] = coefficient * z ** 3
            record["small_edge_polynomial"] = str(sp.factor(small_product))
            record["critical_amplitude"] = str(amplitude)
        records.append(record)
    return groups, records, beta


def main():
    phase = phase_coefficients(N)
    saddle = {k: saddle_coefficients(k, phase) for k in range(4)}
    groups, cores, beta = reconstruct_groups(saddle)
    total = sp.expand(sum(groups.values()))
    coefficients = [sp.factor(total.coeff(z, r)) for r in range(4)]

    # The full coefficient calculation is complete before announced formulas
    # and class-count guards are introduced.
    assert len(cores) == 7
    assert sp.simplify(coefficients[1] - (L - sp.Rational(1, 4) + 1 / (24 * X))) == 0
    b = sp.Symbol("b", real=True)
    zero = sp.Symbol("z01", positive=True)
    substitution = {X: zero ** 2 / 4, L: b + sp.Rational(1, 4) - 1 / (6 * zero ** 2)}
    compact = [
        b ** 2 / 2 + b + sp.Rational(1, 4) - (2 * b + sp.Rational(2, 3)) / zero ** 2,
        b ** 3 / 6 + sp.Rational(16, 5) * b ** 2 + sp.Rational(47, 20) * b
        + sp.Rational(103, 240) + (192 * b ** 2 - 592 * b - 187) / (120 * zero ** 2)
        + sp.Rational(152, 45) * (3 * b + 1) / zero ** 4,
    ]
    differences = [
        sp.factor(coefficients[order].subs(substitution) - target)
        for order, target in zip((2, 3), compact)
    ]
    assert differences == [0, 0]

    mp.mp.dps = 70
    zero_value = mp.besseljzero(0, 1)
    xvalue = zero_value ** 2 / 4
    lvalue = mp.pi ** 2 * mp.besselj(1, zero_value) ** 2 / 6
    numeric = [
        str(sp.N(coefficient.subs(
            {X: sp.Float(str(xvalue), 65), L: sp.Float(str(lvalue), 65)}
        ), 50))
        for coefficient in coefficients
    ]
    script = Path(__file__).resolve()
    result = {
        "schema_version": 1,
        "stage": "computation_only",
        "independent_review_or_acceptance": False,
        "manuscript_scope": "Supplementary reported coefficients; paper details omitted; original theorem unchanged.",
        "sympy_version": sp.__version__,
        "mpmath_version": mp.__version__,
        "source_sha256": {script.relative_to(ROOT).as_posix(): sha256(script.read_bytes()).hexdigest()},
        "internal_symbols": {"X": "x_*", "L": "pi^2*J_1(z01)^2/6", "z": "1/g_2", "z01": "z_{0,1}"},
        "beta_from_sine": [str(value) for value in beta],
        "phase_coefficients": {str(j): str(phase[j]) for j in range(2, N + 1)},
        "saddle_for_Phi_power": {str(k): [str(v) for v in values] for k, values in saddle.items()},
        "cores": cores,
        "group_coefficients": {
            name: [str(sp.factor(poly.coeff(z, r))) for r in range(4)]
            for name, poly in groups.items()
        },
        "complete_coefficients": [str(value) for value in coefficients],
        "compact_reported_coefficients": [str(value) for value in compact],
        "postcomparison_differences": [str(value) for value in differences],
        "numeric_coefficients": numeric,
        "targets_used_only_after_reconstruction": True,
        "passed": True,
    }
    directory = ROOT / "build" / "s06-higher-check"
    directory.mkdir(parents=True, exist_ok=True)
    output = directory / "results.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print("Seven rooted tree classes reconstructed; both exact compact comparisons passed.")
    print("g_2^-2:", numeric[2])
    print("g_2^-3:", numeric[3])
    print("Output:", output.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
