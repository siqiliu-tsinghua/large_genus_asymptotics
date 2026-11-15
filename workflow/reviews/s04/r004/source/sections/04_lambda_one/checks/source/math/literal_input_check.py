"""Different-implementation exact rational guards of high profile increments.

Enumerate actual labels, node pairs and old-label subsets. Polynomial tail
degree comes from the already known lower-profile polynomial degree; only
this finite kernel polynomial is interpolated, never the Hodge coefficients.
"""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
from collections import Counter
from math import comb,factorial
import argparse,json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import finite_functional as f
sys.path.insert(0,str(HERE.parent/'writer'))
import profile_engine as pe
ai=pe.ai
s,P=f.s,f.P


class Literal:
    def __init__(self, profiles, order, pvalue):
        self.profiles=profiles
        self.order=order
        self.pvalue=s.sympify(pvalue)
        self.registry=ai.InputRegistry(profiles)
        for j in range(1,order):
            self.registry.compute_ratios(j)
        self.moments=[s.expand(x.subs(P,self.pvalue)) for x in ai.moments(2*order-1)[0]]
        self.terms={}
        for j,expr in profiles.items():
            self.terms[j]=s.Poly(s.expand(expr*P**j),P,ai.n,ai.D,*ai.M).terms()

    @lru_cache(None)
    def profile(self,order,ds):
        n=len(ds)
        counts=Counter(ds)
        values=(self.pvalue,n,sum(ds),*(counts.get(j,0) for j in range(len(ai.M))))
        value=0
        for powers,coefficient in self.terms[order]:
            term=coefficient
            for x,k in zip(values,powers):
                if k: term*=x**k
            value+=term
        return value/self.pvalue**order

    def weights(self,j,selected,n):
        ratio=self.registry.volume_ratio(j,selected,self.order,nn=n)
        ratio=[s.expand(x.subs(P,self.pvalue)) for x in ratio]
        loss=2*j+selected
        out=[ratio[self.order]]
        for h in range(1,self.order-loss+1):
            out.append(sum(ratio[self.order-r]*comb(r-1,h-1)*loss**(r-h)
                           for r in range(h,self.order-loss+1)))
        return tuple(out)

    def child(self,weights,ds):
        ds=tuple(sorted(ds))
        if any(x<0 for x in ds):return s.Integer(0)
        return sum(w*self.profile(j,ds) for j,w in enumerate(weights))

    def kernel(self,parent):
        pivot,*others=parent
        n=len(parent)
        merge=self.weights(0,1,n)
        nonsep=self.weights(1,-1,n)
        small=[]
        for j in range(self.order//2+1):
            for selected in range(self.order-2*j+1):
                loss=2*j+selected
                if loss<2 or 2*j-2+selected+1<=0:continue
                weights=self.weights(j,selected,n)
                dimension=3*j+selected-2
                for subset in combinations(range(len(others)),selected):
                    ds=tuple(others[i] for i in subset)
                    complement=tuple(others[i] for i in range(len(others)) if i not in subset)
                    for u in range(dimension-sum(ds)+1):
                        amplitude=f.h.bracket(j,(u,)+ds).subs(P,self.pvalue)
                        if amplitude:small.append((u,complement,weights,amplitude))
        @lru_cache(None)
        def at(ell):
            result=0
            for j,d in enumerate(others):
                rest=tuple(others[:j]+others[j+1:])
                result+=4*(2*d+1)*self.child(merge,(pivot+d+ell-1,)+rest)
            total=pivot+ell-2
            for u in range(total+1):
                result+=8*self.child(nonsep,(u,total-u)+tuple(others))
            for u,complement,weights,amplitude in small:
                node=pivot+ell-2-u
                if node>=0:
                    result+=16*amplitude*self.child(weights,(node,)+complement)
            return s.expand(result)
        return at

    def increment(self,parent):
        at=self.kernel(parent)
        degree=2*self.order-1
        cutoff=2*self.order+8
        values=[at(cutoff+j) for j in range(degree+3)]
        finite=[]
        for j in range(degree+3):
            finite.append(values[0])
            values=[values[k+1]-values[k] for k in range(len(values)-1)]
        assert finite[degree+1]==finite[degree+2]==0
        ell=ai.ell
        poly=s.expand(sum(finite[j]*s.prod(ell-cutoff-i for i in range(j))/factorial(j)
                          for j in range(degree+1)))
        averaged=sum(c*self.moments[powers[0]] for powers,c in s.Poly(poly,ell).terms())
        for j in range(cutoff):
            averaged+=ai.mu_value(j).subs(P,self.pvalue)*(at(j)-poly.subs(ell,j))
        return -s.expand(averaged)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--order',type=int,default=3)
    parser.add_argument('--profiles',type=Path,default=HERE.parent/'writer/profiles.json')
    args=parser.parse_args()
    profiles=pe.load_profiles(args.profiles)
    assert args.order in profiles
    cases=[(0,0,0),(1,0),(2,1,0),(3,2,1,0),(4,0,0),(0,0,0,0),(1,1,1,0,0)]
    if args.order>=4:
        cases.extend([(4,1,0),(5,0,0),(5,4,0),(6,1,0)])
    out=[]
    for pvalue in (5,7):
        engine=Literal(profiles,args.order,pvalue)
        for parent in cases:
            new=(parent[0]+1,)+parent[1:]
            expected=engine.profile(args.order,new)-engine.profile(args.order,parent)
            got=engine.increment(parent)
            assert got==expected,(args.order,pvalue,parent,got,expected)
            out.append({'order':args.order,'P':pvalue,'parent':parent,'increment':str(got),'difference':'0'})
            print('literal increment verified',args.order,pvalue,parent,flush=True)
    (HERE/f'literal_e{args.order}_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')


if __name__=='__main__':main()
