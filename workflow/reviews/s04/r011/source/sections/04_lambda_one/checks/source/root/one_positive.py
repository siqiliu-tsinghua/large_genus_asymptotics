"""Finite one-positive extraction at the extra order needed for absolute c4."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent))
import asymptotic_inputs as a
s,P,n,D,M=a.s,a.P,a.n,a.D,a.M
T=s.Symbol("pivot_degree",integer=True)


def one_positive_value(callback,registry,order,length,pivot):
    """callback gives the positive adjacent-difference coefficient, early specialized."""
    actual=isinstance(pivot,int) or isinstance(pivot,s.Integer)
    if actual:
        pivot=int(pivot)
        counts={0:length-int(pivot>0)}
        if pivot:
            counts[pivot]=1
    else:
        counts={0:length-1}
    return callback(order,pivot,registry,parent_n=length,
                    parent_degree=pivot,parent_counts=counts)


def one_positive_average(callback,registry,order,length,cutoff=None):
    """nu-average of e_order(d,zeros), using polynomial primitive plus low patches."""
    if cutoff is None:
        previous=a.max_low(registry.profiles[order-1])
        cutoff=2*previous+3
    generic=s.expand(one_positive_value(callback,registry,order,length,T))
    assert not (generic.free_symbols-{P,T}), generic.free_symbols
    assert s.degree(generic,T)<=2*order-1,(order,s.degree(generic,T))
    low=[]
    for tv in range(cutoff):
        actual=one_positive_value(callback,registry,order,length,tv)
        low.append(s.expand(actual-generic.subs(T,tv)))
    for tv in (cutoff,cutoff+1):
        actual=one_positive_value(callback,registry,order,length,tv)
        assert s.expand(actual-generic.subs(T,tv))==0,("bad cutoff",tv)
    primitive=-a.poly_sum(generic,T,D)
    ans=a.average(primitive,D,a.moments(max(12,2*order))[1])
    for j,correction in enumerate(low):
        tail=1-sum(a.nu_value(d) for d in range(1,j+1))
        ans-=correction*tail
    return s.expand(ans),{
        "length":length,"order":order,"cutoff":cutoff,
        "generic_adjacent":generic,"low_corrections":low,"primitive":primitive}


def cusp_coefficient_from_extra_profile(registry,order,markings,average):
    """C_order at a fixed n; lower profiles use full signed averages."""
    ans=average
    for r in range(1,order):
        ans+=((-1)**(order-r)*s.binomial(order-1,r-1)*
              a.dilaton_average(registry.profiles[r],parent_n=markings))
    return s.expand(ans)


def genus_two_extra_coefficient(callback,registry,order):
    """B_order(2), using only one new adjacent coefficient at the zero tuple."""
    ans=-one_positive_value(callback,registry,order,2,0)
    for genus in range(1,order//2+1):
        # At n=2 the separating label set is empty: selected=0.
        ans-=12*a.h.volume(genus,2)*registry.volume_ratio(
                 genus,0,order,nn=s.Integer(2))[order]
    return s.expand(ans)


def extra_ratio_rows(callback,registry,order):
    """Three rows C2,C3,B2, with only one-positive order-extra profiles."""
    records=[]
    extra=[]
    for markings in (2,3):
        avg,record=one_positive_average(callback,registry,order,markings+1)
        records.append(record)
        extra.append(cusp_coefficient_from_extra_profile(registry,order,markings,avg))
    b2=genus_two_extra_coefficient(callback,registry,order)
    rows=(registry.c_series(2,order-1)+[extra[0]],
          registry.c_series(3,order-1)+[extra[1]],
          registry.b_series(2,order-1)+[b2])
    return rows,records
