"""Exact Appendix C checks; Python standard library only.

Reconstruct all values before the final announced-value comparisons.
No preparation cache, generated table or third-party module is imported.
"""

import sys

sys.dont_write_bytecode = True

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from heapq import heapify, heappop, heappush
from itertools import permutations, product
from math import factorial, prod
from pathlib import Path
import json
import platform


def multiply_series(left, right, degree):
    return [
        sum(
            (left[k] * right[n - k] for k in range(n + 1)),
            Fraction(0),
        )
        for n in range(degree + 1)
    ]


def reciprocal_series(series, degree):
    inverse = [1 / series[0]]
    for n in range(1, degree + 1):
        inverse.append(
            -sum(
                (series[k] * inverse[n - k] for k in range(1, n + 1)),
                Fraction(0),
            )
            / series[0]
        )
    return inverse


def beta_coefficients(degree):
    # Coefficients in z^2 of sin(z/2)/(z/2), inverted finitely.
    sine = [
        Fraction((-1) ** k, 2 ** (2 * k) * factorial(2 * k + 1))
        for k in range(degree + 1)
    ]
    return reciprocal_series(sine, degree)


@lru_cache(maxsize=None)
def inverse_phi_power(degree):
    phi = [
        Fraction((-1) ** k, factorial(k) * factorial(k + 1))
        for k in range(degree + 1)
    ]
    inverse = reciprocal_series(phi, degree)
    result = [Fraction(1)] + [Fraction(0)] * degree
    for _ in range(degree + 1):
        result = multiply_series(result, inverse, degree)
    return tuple(result)


def weak_compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, length - 1):
            yield (first,) + rest


def labeled_trees(vertices):
    if vertices == 1:
        yield ()
        return
    for sequence in product(range(vertices), repeat=vertices - 2):
        degrees = [1 + sequence.count(i) for i in range(vertices)]
        leaves = [i for i, degree in enumerate(degrees) if degree == 1]
        heapify(leaves)
        edges = []
        for neighbor in sequence:
            leaf = heappop(leaves)
            edges.append(tuple(sorted((leaf, neighbor))))
            degrees[neighbor] -= 1
            if degrees[neighbor] == 1:
                heappush(leaves, neighbor)
        edges.append(tuple(sorted((heappop(leaves), heappop(leaves)))))
        yield tuple(sorted(edges))


def canonical_tree(genera, edges):
    representations = []
    for order in permutations(range(len(genera))):
        new_index = {old: new for new, old in enumerate(order)}
        new_edges = tuple(
            sorted(tuple(sorted((new_index[a], new_index[b]))) for a, b in edges)
        )
        representations.append((tuple(genera[i] for i in order), new_edges))
    canonical = min(representations)
    return canonical, representations.count(canonical)


def vertex_polynomial(genus, incident, edge_count, beta):
    degree = 2 * genus - 3 + len(incident)
    assert degree >= 0
    inverse = inverse_phi_power(degree)
    j0 = [
        Fraction((-1) ** k, factorial(k) ** 2)
        for k in range(degree + 1)
    ]
    polynomial = {}
    for powers in product(range(degree + 1), repeat=len(incident)):
        total = sum(powers)
        if total > degree:
            continue
        coefficient = (
            beta[genus]
            * factorial(degree)
            * inverse[degree - total]
            * prod((j0[k] for k in powers), start=Fraction(1))
        )
        exponents = [0] * edge_count
        for edge, power in zip(incident, powers):
            exponents[edge] = power
        if coefficient:
            polynomial[tuple(exponents)] = coefficient
    return polynomial


def multiply_polynomials(left, right):
    result = defaultdict(Fraction)
    for a, ca in left.items():
        for b, cb in right.items():
            result[tuple(x + y for x, y in zip(a, b))] += ca * cb
    return {power: coefficient for power, coefficient in result.items() if coefficient}


def integrate_polynomial(polynomial):
    return sum(
        (
            coefficient
            / prod((power + 1 for power in exponents), start=1)
            for exponents, coefficient in polynomial.items()
        ),
        Fraction(0),
    )


def reconstruct_tree_sum(genus, beta):
    groups = {}
    total = Fraction(0)
    # The exact tree degree gives E<=2g-3, hence vertices<=2g-2.
    for vertices in range(1, 2 * genus - 1):
        for edges in labeled_trees(vertices):
            incident = [
                tuple(i for i, edge in enumerate(edges) if vertex in edge)
                for vertex in range(vertices)
            ]
            for genera in weak_compositions(genus, vertices):
                if any(
                    2 * g - 2 + len(flags) <= 0
                    for g, flags in zip(genera, incident)
                ):
                    continue
                polynomial = {(0,) * len(edges): Fraction(1)}
                for g, flags in zip(genera, incident):
                    polynomial = multiply_polynomials(
                        polynomial,
                        vertex_polynomial(g, flags, len(edges), beta),
                    )
                integral = integrate_polynomial(polynomial)
                total += integral / factorial(vertices)
                canonical, automorphisms = canonical_tree(genera, edges)
                if canonical not in groups:
                    groups[canonical] = {
                        "vertices": vertices,
                        "automorphisms": automorphisms,
                        "labeled_versions": 0,
                        "edge_integral": integral,
                    }
                record = groups[canonical]
                assert record["edge_integral"] == integral
                assert record["automorphisms"] == automorphisms
                record["labeled_versions"] += 1

    classes = []
    for (genera, edges), record in sorted(groups.items()):
        weight = Fraction(record["labeled_versions"], factorial(record["vertices"]))
        assert weight == Fraction(1, record["automorphisms"])
        classes.append(
            {
                "vertex_genera": list(genera),
                "edges": [list(edge) for edge in edges],
                "automorphisms": record["automorphisms"],
                "labeled_versions": record["labeled_versions"],
                "weight": str(weight),
                "edge_integral": str(record["edge_integral"]),
                "weighted_contribution": str(weight * record["edge_integral"]),
            }
        )
    assert total == sum(
        (Fraction(record["weighted_contribution"]) for record in classes),
        Fraction(0),
    )
    return total, classes


def chern_relation(rank, degree):
    """Coefficient of t^degree in c_t c_-t, as a lambda polynomial."""
    result = defaultdict(Fraction)
    for left in range(rank + 1):
        right = degree - left
        if not 0 <= right <= rank:
            continue
        powers = [0] * rank
        for index in (left, right):
            if index:
                powers[index - 1] += 1
        result[tuple(powers)] += (-1) ** right
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def reconstruct():
    beta = beta_coefficients(3)
    cases = {}
    values = {}
    for genus in (2, 3):
        tree_sum, classes = reconstruct_tree_sum(genus, beta)
        values[genus] = factorial(2 * genus - 3) * tree_sum / 12 ** (2 * genus - 3)
        cases[str(genus)] = {
            "tree_sum": str(tree_sum),
            "b_g": str(values[genus]),
            "tree_classes": classes,
        }

    degree_two_rank_two = chern_relation(2, 2)
    lambda2_factor = (
        -degree_two_rank_two[(2, 0)] / degree_two_rank_two[(0, 1)]
    )
    degree_four_rank_three = chern_relation(3, 4)
    top_rank_three_factor = (
        -degree_four_rank_three[(0, 2, 0)]
        * lambda2_factor ** 2
        / degree_four_rank_three[(1, 0, 1)]
    )
    a2 = values[2] / lambda2_factor
    a3 = values[3] / top_rank_three_factor
    defect_ratios = {
        "2": [str(a2 / values[2]), str(a2 / values[2])],
        "3": [
            str(lambda2_factor * a3 / values[3]),
            str(a3 / values[3]),
            str(a3 / values[3]),
        ],
    }
    exact_values = {
        "a_2": str(a2),
        "b_2": str(values[2]),
        "a_3": str(a3),
        "b_3": str(values[3]),
        "normalized_lambda3_genus3": str(values[3] / a3),
    }
    return {
        "beta": {str(g): str(value) for g, value in enumerate(beta)},
        "cases": cases,
        "chern_normalization_factors": {
            "lambda2_over_lambda1_squared": str(lambda2_factor),
            "b3_over_a3": str(top_rank_three_factor),
        },
        "exact_values": exact_values,
        "defect_ratios": defect_ratios,
    }


def main():
    # The complete reconstruction happens before any announced-value input.
    result = reconstruct()
    expected = {
        "a_2": "1/2880",
        "b_2": "1/5760",
        "a_3": "1/90720",
        "b_3": "1/725760",
        "normalized_lambda3_genus3": "1/8",
    }
    expected_defects = {"2": ["2", "2"], "3": ["4", "8", "8"]}
    assert result["exact_values"] == expected
    assert result["defect_ratios"] == expected_defects
    assert [len(result["cases"][str(g)]["tree_classes"]) for g in (2, 3)] == [2, 4]

    script = Path(__file__).resolve()
    root = script.parents[3]
    result.update(
        {
            "stage": "computation_only",
            "passed": True,
            "python_version": platform.python_version(),
            "arithmetic": "fractions.Fraction",
            "source_sha256": {
                script.relative_to(root).as_posix(): sha256(script.read_bytes()).hexdigest()
            },
            "targets_used_only_after_reconstruction": True,
            "independent_review_or_acceptance": False,
        }
    )
    directory = root / "build" / "c-exact-checks"
    directory.mkdir(parents=True, exist_ok=True)
    output = directory / "results.json"
    with output.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(result, ensure_ascii=True, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result["exact_values"], sort_keys=True))
    print("Exact reconstruction and all post-comparisons passed.")
    print("Output:", output.relative_to(root).as_posix())


if __name__ == "__main__":
    main()
