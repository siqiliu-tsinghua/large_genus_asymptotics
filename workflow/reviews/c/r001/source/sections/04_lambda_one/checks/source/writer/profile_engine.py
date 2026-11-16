"""Finite exact normalized descendant profiles; no proposed Hodge targets.

All series use k=2G-2+n. increment(r,t) is e_r(d+unit)-e_r(d),
the NEGATIVE of the coefficient in the exact adjacent difference.
The coefficients are constructed from lower profiles and lower volume
ratios, not fitted to tuples. Only this ignored writer directory is output.
"""
from pathlib import Path
from functools import lru_cache
from itertools import combinations_with_replacement
from collections import Counter
import argparse
import json
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "build/s04-higher-check/root"))
import asymptotic_inputs as ai
import separating

s, n, D, P, M, ell = ai.s, ai.n, ai.D, ai.P, ai.M, ai.ell
T = s.Symbol("pivot", integer=True, nonnegative=True)
I = s.Symbol("construction_index", integer=True, nonnegative=True)
profiles = dict(ai.ff.canonical_profiles())
_ENGINES = {}


def fixed(t):
    t = s.sympify(t)
    return int(t) if t.is_Integer else None


def tag(t, a):
    return int(fixed(t) == a)


def clean(expr):
    return s.expand(expr)


def evaluate(expr, nn, dd, counts):
    """Simultaneous sparse substitution in a profile polynomial."""
    values = {n: s.sympify(nn), D: s.sympify(dd)}
    values.update({m: s.sympify(counts.get(a, 0))
                   for a, m in enumerate(M) if expr.has(m)})
    return clean(expr.xreplace(values))


def coordinate_difference(expr, t):
    """Profile potential difference when one coordinate t becomes t+1."""
    values = {D: D + 1}
    tt = fixed(t)
    if tt is not None:
        if tt < len(M):
            values[M[tt]] = M[tt] - 1
        if tt + 1 < len(M):
            values[M[tt + 1]] = M[tt + 1] + 1
    return clean(expr.xreplace(values) - expr)


class ProfileEngine:
    def __init__(self, registry=None, parent_values=None):
        self.registry = registry if registry is not None else ai.initial_registry()
        for r, expr in list(self.registry.profiles.items()):
            self.registry.profiles[r] = clean(expr)
        self.timings = {}
        self.parent_values = parent_values
        self._specialized = {}

    def parent(self, expr):
        expr = s.sympify(expr)
        return clean(expr.xreplace(self.parent_values)) if self.parent_values else expr

    @lru_cache(None)
    def value(self, order, nn, dd, counts):
        return evaluate(self.registry.profiles[order], nn, dd,
                        dict(enumerate(counts)))

    def _value(self, order, nn, dd, counts):
        a = ai.max_low(self.registry.profiles[order])
        return self.value(order, self.parent(nn), self.parent(dd),
                          tuple(self.parent(counts.get(j, 0)) for j in range(a + 1)))

    @lru_cache(None)
    def merge_kernel(self, order, pivot):
        """Unscaled sum (2d_j+1) mu_l times the child e_order."""
        t = s.sympify(pivot)
        tt = fixed(t)
        a = ai.max_low(self.registry.profiles[order])
        base = {j: M[j] - tag(t, j) for j in range(a + 1)}
        child_d = D + ell - 1
        # Explicit other degrees 0,...,a+1 cover all possible low mergers.
        other = {j: M[j] - tag(t, j) for j in range(a + 2)}
        high_count = n - 1 - sum(other.values())
        high_degree = D - t - sum(j * c for j, c in other.items())
        high_weight = self.parent(2 * high_degree + high_count)
        result = (high_weight * ai.kernel_sum(
            self._value(order, n - 1, child_d, base)) if high_weight != 0 else s.Integer(0))
        for b in range(a + 2):
            multiplicity = self.parent((2 * b + 1) * other[b])
            if multiplicity == 0:
                continue
            counts = dict(base)
            if b <= a:
                counts[b] -= 1
            poly = self._value(order, n - 1, child_d, counts)

            def actual(l, b=b, counts=counts):
                degree = tt + b + l - 1
                if degree < 0:
                    return s.Integer(0)
                state = dict(counts)
                if degree <= a:
                    state[degree] = state.get(degree, 0) + 1
                return self._value(order, n - 1, D + l - 1, state)

            low_end = a + 1 - tt - b if tt is not None else -1
            value = ai.kernel_sum(poly, actual=actual if low_end >= 0 else None,
                                  low_end=low_end)
            result += multiplicity * value
        return clean(result)

    @lru_cache(None)
    def nonseparating_kernel(self, order, pivot):
        """Unscaled ordered node-pair sum, with all low-total corrections."""
        t = s.sympify(pivot)
        tt = fixed(t)
        a = ai.max_low(self.registry.profiles[order])
        counts = {j: M[j] - tag(t, j) for j in range(a + 1)}
        total = t + ell - 2
        child_d = D + ell - 2
        poly = (total - 2 * a - 1) * self._value(order, n + 1, child_d, counts)
        for b in range(a + 1):
            state = dict(counts)
            state[b] += 1
            poly += 2 * self._value(order, n + 1, child_d, state)

        def actual(l):
            degree = tt + l - 2
            if degree < 0:
                return s.Integer(0)
            ans = 0
            for u in range(degree + 1):
                v = degree - u
                state = dict(counts)
                if u <= a:
                    state[u] += 1
                if v <= a:
                    state[v] += 1
                ans += self._value(order, n + 1, D + l - 2, state)
            return clean(ans)

        low_end = 2 * a + 2 - tt if tt is not None else -1
        return ai.kernel_sum(poly, actual=actual if low_end >= 0 else None,
                             low_end=low_end)

    @staticmethod
    def shifted_weights(prefactor, order, shift):
        """Weights on e_h for a child of complexity k-shift."""
        weights = {0: prefactor[order]}
        for h in range(1, order):
            weights[h] = clean(sum(
                prefactor[j] * s.binomial(order - j - 1, h - 1)
                * shift ** (order - j - h)
                for j in range(1, order - h + 1)))
        return weights

    @lru_cache(None)
    def adjacent_coefficient(self, order, pivot=T):
        """Positive source coefficient of profile(d)-profile(d+unit)."""
        assert all(h in self.registry.profiles for h in range(order))
        start = time.monotonic()
        parent_n = self.parent(n)
        merge = [4 * x for x in self.registry.volume_ratio(0, 1, order, nn=parent_n)]
        nonsep = [8 * x for x in self.registry.volume_ratio(1, -1, order, nn=parent_n)]
        ans = 0
        for h, weight in self.shifted_weights(merge, order, 1).items():
            if weight != 0:
                ans += weight * self.merge_kernel(h, pivot)
        for h, weight in self.shifted_weights(nonsep, order, 1).items():
            if weight != 0:
                ans += weight * self.nonseparating_kernel(h, pivot)
        if order >= 2:
            ans += (self.specialized_separating(order, pivot) if self.parent_values else
                    separating.separating_coefficient(order, pivot, self.registry))
        ans = clean(ans)
        self.timings[f"adjacent_{order}_{pivot}"] = time.monotonic() - start
        return ans

    def increment(self, order, pivot=T):
        """Signed coordinate increment Delta e_order; Python int or generic T."""
        return -self.adjacent_coefficient(order, s.sympify(pivot))

    def specialized_separating(self, order, pivot):
        """Same finite subsets as the root helper, with early parent reduction."""
        t = s.sympify(pivot)
        tt = fixed(t)
        ans = s.Integer(0)
        for genus in range(order // 2 + 1):
            for selected in range(order - 2 * genus + 1):
                loss = 2 * genus + selected
                if loss < 2 or loss - 1 <= 0:
                    continue
                dim = 3 * genus + selected - 2
                depth = order - loss
                ratio = self.registry.volume_ratio(genus, selected, order, nn=self.parent(n))
                weights = {0: ratio[order]}
                for r in range(1, depth + 1):
                    weights[r] = clean(sum(ratio[order - j] * s.binomial(j - 1, r - 1)
                                           * loss ** (j - r) for j in range(r, depth + 1)))
                low = max((ai.max_low(self.registry.profiles[r])
                           for r in range(1, depth + 1)), default=0)
                for ds in combinations_with_replacement(range(dim + 1), selected):
                    total = sum(ds)
                    if total > dim:
                        continue
                    removed = Counter(ds)
                    selector = s.Integer(1)
                    for degree, count in removed.items():
                        selector *= ai.binom(self.parent(M[degree] - tag(t, degree)), count)
                    selector = clean(selector)
                    if selector == 0:
                        continue
                    base = {j: M[j] - removed.get(j, 0) - tag(t, j)
                            for j in range(low + 1)}
                    for u in range(dim - total + 1):
                        small = ai.h.bracket(genus, (u,) + ds)
                        if small == 0:
                            continue

                        def expression(node, degree):
                            counts = dict(base)
                            if node is not None and 0 <= node <= low:
                                counts[node] += 1
                            value = weights[0]
                            for r in range(1, depth + 1):
                                if weights[r] != 0:
                                    value += weights[r] * self._value(r, n - selected, degree, counts)
                            return clean(value)

                        generic = expression(None, D + ell - 2 - u - total)

                        def actual(l, u=u):
                            node = tt + l - 2 - u
                            return (s.Integer(0) if node < 0 else
                                    expression(node, D + l - 2 - u - total))

                        end = max(-1, low + u + 2 - tt) if tt is not None else -1
                        value = ai.kernel_sum(generic, actual=actual if end >= 0 else None,
                                              low_end=end)
                        ans += 16 * selector * small * value
        return clean(ans)

    def adjacent_at(self, order, pivot, parent_n, parent_D, parent_counts):
        """Early-specialized positive adjacent coefficient, before child eval."""
        nn = s.sympify(parent_n)
        dd = s.sympify(parent_D)
        counts = tuple(s.sympify(parent_counts.get(j, 0)).subs(n, nn) for j in range(len(M)))
        key = (nn, dd, counts)
        if key not in self._specialized:
            values = {n: nn, D: dd, **dict(zip(M, counts))}
            self._specialized[key] = ProfileEngine(self.registry, parent_values=values)
        return self._specialized[key].adjacent_coefficient(order, s.sympify(pivot))

    def one_positive_adjacent(self, order, pivot, parent_n):
        """Positive adjacent coefficient at (pivot,0,...,0), exact low/high."""
        tt = fixed(pivot)
        counts = {0: s.sympify(parent_n) - (int(tt > 0) if tt is not None else 1)}
        if tt is not None and tt > 0:
            counts[tt] = 1
        return self.adjacent_at(order, pivot, parent_n, pivot, counts)

    def build_profile(self, order, verify=True, verbose=True):
        """Construct the complete potential by exact discrete integration.

        First integrate the generic D increment to B(D,counts). For every
        low pivot subtract the FULL coordinate difference of B, including
        its count shifts. These residuals must be D-independent. Sum them
        along the canonical zero -> low classes -> safe high class path.
        This is algebraically the canonical full potential construction,
        with its generic antiderivative canceled early for efficiency.
        """
        start = time.monotonic()
        assert self.parent_values is None, "Full potential requires an unspecialized engine"
        a = max(ai.max_low(self.registry.profiles[h]) for h in range(order))
        limit = 2 * a + 3
        if verbose:
            print(f"order {order}: previous low cut {a}, safe pivot {limit}", flush=True)
        generic = clean(self.increment(order, T))
        assert not generic.has(T), ("Generic increment depends on pivot", order)
        bulk = ai.poly_sum(generic.xreplace({D: I}), I, D)
        residual = []
        for t in range(limit):
            rr = clean(self.increment(order, t) - coordinate_difference(bulk, t))
            assert not rr.has(D), ("Residual still depends on total degree", order, t)
            residual.append(rr)
            if verbose:
                print(f"  residual {t}: {0 if rr == 0 else len(s.Add.make_args(rr))} terms", flush=True)

        # Zero source residuals prove that these higher low-count classes
        # can be coalesced, before constructing any temporary variables.
        support = max((t for t, rr in enumerate(residual) if rr != 0), default=-1)
        integration_limit = max(1, support + 1)
        if verbose:
            print(f"  residual support {support}; canonical high class {integration_limit}", flush=True)

        # Build each supported low class, then the high class just above it.
        constant = s.Integer(0)
        previous_count = s.Integer(0)
        for degree in range(1, integration_limit + 1):
            multiplicity = (M[degree] if degree < integration_limit else
                            n - M[0] - previous_count)
            one_entry = s.Integer(0)
            for t in range(degree):
                state = {0: n - previous_count - I - int(t > 0)}
                for b in range(1, len(M)):
                    value = M[b] if b < degree else (I if b == degree else 0)
                    state[b] = value + int(t == b and t > 0)
                substitutions = {m: state[j] for j, m in enumerate(M)
                                 if residual[t].has(m)}
                one_entry += residual[t].xreplace(substitutions)
            constant += ai.poly_sum(clean(one_entry), I, multiplicity)
            constant = clean(constant)
            if verbose:
                print(f"  class {degree}: {len(s.Add.make_args(constant))} constant terms", flush=True)
            if degree < integration_limit:
                previous_count += M[degree]
        result = clean(bulk + constant)
        assert result.free_symbols <= {n, D, P, *M}
        assert clean(evaluate(result, n, 0, {0: n})) == 0
        if verify:
            for t in [*range(limit), T]:
                discrepancy = clean(coordinate_difference(result, t) - self.increment(order, t))
                assert discrepancy == 0, ("Potential increment mismatch", order, t)
            # Check the edge of the generic range using literal integer pivots.
            for t in (limit, limit + 1):
                assert clean(self.increment(order, t) - generic) == 0, (order, t)
        self.timings[f"potential_{order}"] = time.monotonic() - start
        if verbose:
            print(f"order {order} complete: {len(s.Add.make_args(result))} terms, "
                  f"actual low cut {ai.max_low(result)}", flush=True)
        return result


def save_profiles(values, path=HERE / "profiles.json", metadata=None):
    record = {"normalization": "k=2G-2+n; signed e_r coefficients",
              "method": "Exact adjacent increments + canonical Faulhaber potential; no high Hodge target input",
              "profiles": {str(r): str(clean(e)) for r, e in values.items()},
              "actual_max_low": {str(r): ai.max_low(e) for r, e in values.items()},
              "metadata": metadata or {}}
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8", newline="\n")
    temporary.replace(path)


def load_profiles(path=HERE / "profiles.json"):
    record = json.loads(Path(path).read_text(encoding="utf-8"))
    names = {"n": n, "D": D, "P": P, **{str(m): m for m in M}}
    values = {int(r): s.sympify(e, locals=names) for r, e in record["profiles"].items()}
    profiles.update(values)
    return values


def adjacent_coefficient(order, pivot, registry, parent_n=None,
                         parent_degree=None, parent_counts=None):
    """Module callback matching root/one_positive.py, positive convention."""
    key = id(registry)
    if key not in _ENGINES:
        _ENGINES[key] = ProfileEngine(registry)
    engine = _ENGINES[key]
    if parent_counts is None:
        return engine.adjacent_coefficient(order, pivot)
    assert parent_n is not None and parent_degree is not None
    return engine.adjacent_at(order, pivot, parent_n, parent_degree, parent_counts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--through", type=int, default=3)
    parser.add_argument("--verify-known", action="store_true")
    args = parser.parse_args()
    engine = ProfileEngine()
    if args.verify_known:
        for r in (1, 2):
            got = engine.build_profile(r)
            assert clean(got - engine.registry.profiles[r]) == 0, r
            print(f"Complete existing profile e{r} reproduced exactly", flush=True)
    for r in range(3, args.through + 1):
        expr = engine.build_profile(r)
        engine.registry.register_profile(r, expr)
        profiles[r] = expr
        save_profiles(engine.registry.profiles, metadata=engine.timings)
        engine.registry.compute_ratios(r)
        print(f"Registered profile and ratio order {r}", flush=True)
    save_profiles(engine.registry.profiles, metadata=engine.timings)


if __name__ == "__main__":
    main()
