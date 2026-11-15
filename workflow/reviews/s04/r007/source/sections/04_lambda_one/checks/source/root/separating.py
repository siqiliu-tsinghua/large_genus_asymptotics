"""Independent whole small-component contribution to adjacent differences."""
from functools import lru_cache
from itertools import combinations_with_replacement
from collections import Counter
from pathlib import Path
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent))
import asymptotic_inputs as a
s,P,n,D,M,ell=a.s,a.P,a.n,a.D,a.M,a.ell


def separating_coefficient(order,pivot,registry,parent_n=n,parent_degree=D,
                           parent_counts=None):
    """Coefficient k^-order of (profile(d)-profile(d+unit)), positive convention.

    pivot is a nonnegative Python int or a symbolic sufficiently large pivot.
    """
    actual=isinstance(pivot,int) or isinstance(pivot,s.Integer)
    if actual:
        pivot=int(pivot)
    def parent_count(j):
        return M[j] if parent_counts is None else s.sympify(parent_counts.get(j,0))
    ans=s.Integer(0)
    for genus in range(order//2+1):
        for selected in range(order-2*genus+1):
            loss=2*genus+selected
            if loss<2 or 2*genus-2+(selected+1)<=0:
                continue
            dim=3*genus+selected-2
            depth=order-loss
            ratio=registry.volume_ratio(genus,selected,order,nn=parent_n)
            weights=[ratio[order]]
            for r in range(1,depth+1):
                weights.append(a.clean(sum(ratio[order-j]*
                    s.binomial(j-1,r-1)*loss**(j-r) for j in range(r,depth+1))))
            low=max((a.max_low(registry.profiles[r]) for r in range(1,depth+1)),default=0)
            for ds in combinations_with_replacement(range(dim+1),selected):
                total=sum(ds)
                if total>dim:
                    continue
                removed=Counter(ds)
                selector=s.Integer(1)
                for degree,cnt in removed.items():
                    available=parent_count(degree)-(int(pivot==degree) if actual else 0)
                    selector*=a.binom(available,cnt)
                if selector==0:
                    continue
                basecounts={j:parent_count(j)-removed.get(j,0)-
                               (int(pivot==j) if actual else 0)
                            for j in range(low+1)}
                for u in range(dim-total+1):
                    small=a.h.bracket(genus,(u,)+ds)
                    if small==0:
                        continue
                    def expression(node,degree):
                        counts=dict(basecounts)
                        if node is not None and 0<=node<=low:
                            counts[node]=counts.get(node,parent_count(node))+1
                        z=weights[0]
                        for r in range(1,depth+1):
                            z+=weights[r]*a.profile_value(registry.profiles[r],
                                    parent_n-selected,degree,counts)
                        return a.clean(z)
                    generic=expression(None,parent_degree+ell-2-u-total)
                    if actual:
                        def actual_at(lv):
                            node=pivot+lv-2-u
                            return (s.Integer(0) if node<0 else
                                    expression(node,parent_degree+lv-2-u-total))
                        summed=a.kernel_sum(generic,ell,actual_at,
                                           max(-1,low+u+2-pivot))
                    else:
                        summed=a.kernel_sum(generic,ell)
                    ans+=16*selector*small*summed
    return a.clean(ans)


def self_check():
    reg=a.initial_registry()
    tv=s.Symbol("t",integer=True)
    for pivot in (0,1,2,3,tv):
        got=separating_coefficient(2,pivot,reg)
        z0=M[0]-(int(pivot==0) if isinstance(pivot,int) else 0)
        def tail(j):
            if not isinstance(pivot,int):
                return s.Integer(2)
            return 2-sum(a.mu_value(l) for l in range(max(0,j-pivot)))
        expected=((a.binom(z0,2)+P/12)*tail(2)+s.Rational(1,2)*tail(3))/P**2
        assert s.factor(got-expected)==0,(pivot,s.factor(got-expected))
    print("Independent separating coefficients reproduce every order-two mode.",
          flush=True)


if __name__=="__main__":
    self_check()
