"""Independent exact q<=2 rooted-core audit; Python standard library only.

This is a reproducibility certificate, not a formal manuscript review.
All output is confined to the ignored build/a-calculations/results directory. P is a computational formal
indeterminate, substituted by pi**2 only for the separate numerical check.
No candidate asymptotic coefficient is an input to enumeration/integration.
"""

from __future__ import annotations

from functools import lru_cache
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial, pi, sin, sqrt, fsum
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from runtime import OUTPUT


HERE = OUTPUT


def clean(a):
    return {k: F(v) for k, v in a.items() if v}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(a, b):
    return clean({k: v * b for k, v in a.items()})


def mul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            out[k] = out.get(k, F(0)) + va * vb
    return clean(out)


def monomial(coefficient, powers):
    return clean({tuple(powers): F(coefficient)})


def univar(coefficient, power=0):
    return monomial(coefficient, (power,))


def poly_text(a, names=("P",)):
    if not a:
        return "0"
    chunks = []
    for powers, coef in sorted(a.items(), reverse=True):
        factors = [str(coef)]
        for name, power in zip(names, powers):
            if power:
                factors.append(name if power == 1 else f"{name}^{power}")
        chunks.append("*".join(factors))
    return " + ".join(chunks).replace("+ -", "- ")


def eval_poly(a, values):
    return fsum(float(coef) * __import__("math").prod(x**k for x, k in zip(values, powers))
                for powers, coef in a.items())


def set_partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for p in set_partitions(rest):
        yield ((first,),) + p
        for i in range(len(p)):
            yield p[:i] + ((first,) + p[i],) + p[i + 1:]


@lru_cache(None)
def psi(g, ds):
    """Only genus 0/1 is needed; exact string/dilaton, no WP table input."""
    n = len(ds)
    if any(d < 0 for d in ds) or sum(ds) != 3 * g - 3 + n:
        return F(0)
    if 2 * g - 2 + n <= 0:
        return F(0)
    if g == 0:
        return F(factorial(n - 3), __import__("math").prod(factorial(d) for d in ds))
    if g != 1:
        raise ValueError("This independent low-type audit needs only g=0,1")
    if ds == (1,):
        return F(1, 24)
    if 0 in ds:
        j = ds.index(0)
        rem = ds[:j] + ds[j + 1:]
        return sum((psi(g, tuple(sorted(rem[:i] + (d - 1,) + rem[i + 1:])))
                    for i, d in enumerate(rem) if d), F(0))
    if 1 in ds:
        j = ds.index(1)
        return (n - 1) * psi(g, tuple(sorted(ds[:j] + ds[j + 1:])))
    raise AssertionError("A dimension-valid genus-one tuple has a 0 or a 1")


@lru_cache(None)
def kappa_psi(g, ds, m):
    """s02 unordered partition inversion, a_i=1; each new psi power>=2."""
    result = F(0)
    for partition in set_partitions(tuple(range(m))):
        new_degrees = tuple(len(block) + 1 for block in partition)
        result += (-1)**(m - len(partition)) * psi(g, tuple(sorted(ds + new_degrees)))
    return result


def vertex_poly(g, flag_edges, number_edges):
    """Exact integral exp(2P*kappa_1 - sum t_flag*psi_flag)."""
    n = len(flag_edges)
    dimension = 3 * g - 3 + n
    out = {}
    for ds in product(range(dimension + 1), repeat=n):
        degree = sum(ds)
        if degree > dimension:
            continue
        m = dimension - degree
        intersection = kappa_psi(g, tuple(ds), m)
        coefficient = intersection * F((-1)**degree * 2**m,
                                       factorial(m) * __import__("math").prod(factorial(d) for d in ds))
        powers = [m] + [0] * number_edges
        for edge, d in zip(flag_edges, ds):
            powers[edge + 1] += d
        out = add(out, monomial(coefficient, powers))
    return out


def compositions(n, length):
    if length == 0:
        if n == 0:
            yield ()
    elif length == 1:
        if n >= 1:
            yield (n,)
    else:
        for first in range(1, n - length + 2):
            for rest in compositions(n - first, length - 1):
                yield (first,) + rest


def connected(matrix):
    seen, todo = {0}, [0]
    while todo:
        i = todo.pop()
        for j in range(len(matrix)):
            if i != j and matrix[i][j] and j not in seen:
                seen.add(j)
                todo.append(j)
    return len(seen) == len(matrix)


def encode(gs, matrix, order):
    return (len(gs), tuple(gs[i - 1] for i in order[1:]),
            tuple(matrix[order[i]][order[j]]
                  for i in range(len(order)) for j in range(i, len(order))))


def canonical(gs, matrix):
    return min(encode(gs, matrix, (0,) + p)
               for p in permutations(range(1, len(matrix))))


def enumerate_cores(q):
    found = {}
    if q == 0:
        return [((), ((0,),))]
    for v in range(1, q + 1):
        for ks in compositions(q, v):
            genus_ranges = [range((k + 2) // 2 + 1) for k in ks]
            for gs in product(*genus_ranges):
                ns = [k + 2 - 2 * g for k, g in zip(ks, gs)]
                if any(n <= 0 for n in ns):
                    continue  # a small vertex must connect to the root component
                small_pairs = [(i, j) for i in range(1, v + 1) for j in range(i + 1, v + 1)]
                edge_ranges = [range(min(ns[i - 1], ns[j - 1]) + 1) for i, j in small_pairs]
                for loops in product(*(range(n // 2 + 1) for n in ns)):
                    for internal in product(*edge_ranges):
                        matrix = [[0] * (v + 1) for _ in range(v + 1)]
                        for i, l in enumerate(loops, 1):
                            matrix[i][i] = l
                        for (i, j), multiplicity in zip(small_pairs, internal):
                            matrix[i][j] = matrix[j][i] = multiplicity
                        roots = [ns[i - 1] - 2 * matrix[i][i]
                                 - sum(matrix[i][j] for j in range(1, v + 1) if j != i)
                                 for i in range(1, v + 1)]
                        if any(m < 0 for m in roots):
                            continue
                        for i, m in enumerate(roots, 1):
                            matrix[0][i] = matrix[i][0] = m
                        if not connected(matrix):
                            continue
                        key = canonical(gs, matrix)
                        found.setdefault(key, (tuple(gs), tuple(tuple(row) for row in matrix)))
    return [found[k] for k in sorted(found)]


def edge_list(matrix):
    return [(i, j) for i in range(len(matrix)) for j in range(i, len(matrix))
            for _ in range(matrix[i][j])]


def automorphism_formula(gs, matrix):
    v = len(matrix)
    vertex_count = sum(encode(gs, matrix, (0,) + p) == encode(gs, matrix, tuple(range(v)))
                       for p in permutations(range(1, v)))
    edge_count = 1
    for i in range(v):
        edge_count *= 2**matrix[i][i] * factorial(matrix[i][i])
        for j in range(i + 1, v):
            edge_count *= factorial(matrix[i][j])
    return vertex_count * edge_count


def automorphism_flags(gs, matrix):
    """Independent literal flag-bijection count preserving the edge involution."""
    edges = edge_list(matrix)
    flags = [[] for _ in matrix]
    partner = []
    for e, (i, j) in enumerate(edges):
        flags[i].append(2 * e)
        flags[j].append(2 * e + 1)
        partner.extend([2 * e + 1, 2 * e])
    count = 0
    for p in permutations(range(1, len(matrix))):
        order = (0,) + p
        if any(gs[i - 1] != gs[order[i] - 1] or len(flags[i]) != len(flags[order[i]])
               for i in range(1, len(matrix))):
            continue
        for choices in product(*(permutations(flags[order[i]]) for i in range(len(matrix)))):
            mapping = [0] * len(partner)
            for i, targets in enumerate(choices):
                for source, target in zip(flags[i], targets):
                    mapping[source] = target
            if all(mapping[partner[f]] == partner[mapping[f]] for f in range(len(partner))):
                count += 1
    return count


@lru_cache(None)
def f_moment(d):
    """Integral_0^(2*pi^2) t^d f(t)dt from exact integration by parts."""
    # I_0=int_0^pi sin x dx=2; I_{2d}=P^d-(2d)(2d-1)I_{2d-2}.
    moment = univar(2)
    for j in range(1, d + 1):
        moment = add(univar(1, j), scale(moment, -(2 * j) * (2 * j - 1)))
    return scale(moment, 2**(d + 2))


def plain_moment(d):
    return univar(F(2**(d + 1), d + 1), d + 1)


def core_integrand(gs, matrix):
    edges = edge_list(matrix)
    result = monomial(1, (0,) * (len(edges) + 1))
    for i, g in enumerate(gs, 1):
        flag_edges = [e for e, (a, b) in enumerate(edges) for vertex in (a, b) if vertex == i]
        result = mul(result, vertex_poly(g, flag_edges, len(edges)))
    return edges, result


def integrate_core(gs, matrix):
    edges, integrand = core_integrand(gs, matrix)
    total = {}
    for powers, coefficient in integrand.items():
        term = univar(coefficient, powers[0])
        for (a, b), d in zip(edges, powers[1:]):
            term = mul(term, f_moment(d) if a == 0 or b == 0 else plain_moment(d))
        total = add(total, term)
    return scale(total, F(1, automorphism_formula(gs, matrix)))


def integrate_core_general(gs, matrix):
    """Formal polynomial in (P,z,J0,J1,J2), Jd=int_0^z t^d f(t)dt."""
    edges, integrand = core_integrand(gs, matrix)
    total = {}
    for powers, coefficient in integrand.items():
        term = monomial(coefficient, (powers[0], 0, 0, 0, 0))
        for (a, b), d in zip(edges, powers[1:]):
            if a == 0 or b == 0:
                assert d <= 2
                exponent = [0] * 5
                exponent[d + 2] = 1
                factor = monomial(1, exponent)
            else:
                factor = monomial(F(1, d + 1), (0, d + 1, 0, 0, 0))
            term = mul(term, factor)
        total = add(total, term)
    return scale(total, F(1, automorphism_formula(gs, matrix)))


def specialize_general(a):
    replacements = [univar(1, 1), univar(2, 1)] + [f_moment(d) for d in range(3)]
    out = {}
    for powers, coefficient in a.items():
        term = univar(coefficient)
        for replacement, exponent in zip(replacements, powers):
            for _ in range(exponent):
                term = mul(term, replacement)
        out = add(out, term)
    return out


def simpson_f_moment(d, steps=8192):
    upper = 2 * pi**2
    def integrand(t):
        value = 1.0 if t == 0 else sin(sqrt(t / 2)) / sqrt(t / 2)
        return t**d * value
    h = upper / steps
    return h / 3 * (integrand(0) + integrand(upper)
                    + 4 * fsum(integrand(h * j) for j in range(1, steps, 2))
                    + 2 * fsum(integrand(h * j) for j in range(2, steps, 2)))


def main():
    low = {}
    for g, n in [(0, 3), (1, 1), (0, 4), (1, 2)]:
        low[f"{g},{n}"] = poly_text(vertex_poly(g, list(range(n)), n),
                                      ("P",) + tuple(f"t{i}" for i in range(1, n + 1)))
    data = {"method": "exact enumeration + flag automorphisms + string/dilaton + s02 inversion + separable edge moments",
            "low_vertex_polynomials": low,
            "intersections": {"kappa_1^2 on M_1,2": str(kappa_psi(1, (0, 0), 2)),
                              "kappa_1 psi_1 on M_1,2": str(kappa_psi(1, (0, 1), 1)),
                              "psi_1^2 on M_1,2": str(psi(1, (0, 2))),
                              "psi_1 psi_2 on M_1,2": str(psi(1, (1, 1)))},
            "counts": {}, "cores": [], "sums": {}, "moment_quadrature_check": {}}
    lines = ["# Independent exact rooted-core audit", "", "Computational P=pi^2. The root is vertex 0; it has no core self-loop.", ""]
    for q in range(3):
        cores = enumerate_cores(q)
        data["counts"][str(q)] = len(cores)
        total = {}
        total_general = {}
        lines += [f"## q={q}", "",
                  "| ID | small (genus,valence) | nonzero edge multiplicities | root (genus,valence) | Aut formula/flags | integrated core / Aut |",
                  "|---|---|---|---|---|---|"]
        for number, (gs, matrix) in enumerate(cores, 1):
            edges = edge_list(matrix)
            ns = [2 * matrix[i][i] + sum(matrix[i][j] for j in range(len(matrix)) if j != i)
                  for i in range(len(matrix))]
            c = sum(gs) + len(edges) - len(gs)
            assert 2 * c == q + ns[0]
            assert sum(2 * g - 2 + n for g, n in zip(gs, ns[1:])) == q
            aut, direct = automorphism_formula(gs, matrix), automorphism_flags(gs, matrix)
            assert aut == direct
            value = integrate_core(gs, matrix)
            general = integrate_core_general(gs, matrix)
            assert specialize_general(general) == value
            total = add(total, value)
            total_general = add(total_general, general)
            display_edges = "; ".join(f"{i}-{j}:{matrix[i][j]}" for i in range(len(matrix))
                                      for j in range(i, len(matrix)) if matrix[i][j]) or "none"
            identifier = f"q{q}.{number}"
            row = {"id": identifier, "q": q, "small_genera": gs, "valences": ns,
                   "small_complexities": [2 * g - 2 + n for g, n in zip(gs, ns[1:])],
                   "edge_matrix": matrix, "edges": edges, "root_genus_loss": c,
                   "root_type_with_p_loops": {"genus": f"g-{c}-p", "valence": f"{ns[0]}+2p"},
                   "automorphism_formula": aut, "automorphism_literal_flags": direct,
                   "integrated_core_general_z_divided_by_Aut": poly_text(general, ("P", "z", "J0", "J1", "J2")),
                   "integrated_core_divided_by_Aut": poly_text(value),
                   "leading_coefficient_divided_by_eS": poly_text(mul(value, univar(F(1, 8**q), -q)))}
            data["cores"].append(row)
            lines.append(f"| {identifier} | {list(zip(gs, ns[1:]))} | {display_edges} | (g-{c},{ns[0]}) | {aut}/{direct} | {poly_text(value)} |")
        normalized = mul(total, univar(F(1, 8**q), -q))
        data["sums"][str(q)] = {"integral_sum_general_z": poly_text(total_general, ("P", "z", "J0", "J1", "J2")),
                                "integral_sum": poly_text(total),
                                "coefficient_divided_by_eS": poly_text(normalized),
                                "numeric": eval_poly(normalized, (pi**2,))}
        lines += ["", f"q={q}: integral sum `{poly_text(total)}`; normalized coefficient `{poly_text(normalized)}`.", ""]
    for d in range(3):
        exact = eval_poly(f_moment(d), (pi**2,))
        numerical = simpson_f_moment(d)
        assert abs(exact - numerical) <= 1e-9 * (1 + abs(exact))
        data["moment_quadrature_check"][str(d)] = {"exact_polynomial": poly_text(f_moment(d)),
                                                   "exact_evaluated": exact,
                                                   "independent_simpson": numerical,
                                                   "difference": numerical - exact}
    # These are outputs of the independent hand classification/integration,
    # not inputs to enumeration, automorphisms, intersection numbers or moments.
    assert data["counts"] == {"0": 1, "1": 3, "2": 13}
    assert data["sums"]["1"]["coefficient_divided_by_eS"] == "25/24 + 65/6*P^-1"
    assert data["sums"]["2"]["coefficient_divided_by_eS"] == "1849/1152 + 3737/144*P^-1 + 7465/72*P^-2"
    (HERE / "math_core_data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    (HERE / "math_core_table.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"counts": data["counts"], "low_vertex_polynomials": low,
                      "sums": data["sums"], "literal_flag_aut_checks": len(data["cores"]),
                      "outputs": ["math_core_data.json", "math_core_table.md"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
