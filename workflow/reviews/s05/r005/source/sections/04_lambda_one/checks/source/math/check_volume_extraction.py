"""Independent literal-source/dilaton/genus guards of absolute c3 or c4.

No high Hodge coefficient is read. The high order is a source order, not
a fitted final asymptotic coefficient. P remains a symbolic indeterminate.
"""
from pathlib import Path
import argparse,sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import literal_input_check as lit
s,P=lit.s,lit.P


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--volume-order',type=int,choices=(3,4),default=4)
    parser.add_argument('--profiles',type=Path,default=HERE.parent/'writer/e4-fast.json')
    args=parser.parse_args()
    root=json.loads((HERE.parent/f'root/volume{args.volume_order}.json').read_text(encoding='utf-8'))
    records=root['one_positive_records']
    order=args.volume_order+1
    engine=lit.Literal(lit.pe.load_profiles(args.profiles),order,P)
    rows=[]
    for rec in records:
        nn=int(rec['length'])
        polynomial=s.sympify(rec['generic_adjacent'],locals={'P':P})
        variables=polynomial.free_symbols-{P}
        assert len(variables)<=1
        corrections=s.sympify(rec['low_corrections'],locals={'P':P})
        for t in range(int(rec['cutoff'])+1):
            got=engine.increment((t,)+(0,)*(nn-1))
            expected=-polynomial.subs({v:t for v in variables})
            if t<len(corrections):expected-=corrections[t]
            difference=s.factor(got-expected)
            assert difference==0,(nn,t,difference)
            rows.append({'source_order':order,'length':nn,'pivot':t,'symbolic_P_difference':'0'})
            print('literal source verified',order,nn,t,flush=True)

    def nu_average(poly,d):
        return s.expand(sum(c*lit.f.lm.dilaton_moment(powers[0])
                            for powers,c in s.Poly(s.expand(poly),d).terms()))

    def lower_average(expr,nn):
        d=s.Symbol('d',integer=True)
        substitute={lit.ai.n:nn,lit.ai.D:d,**{m:(nn-1 if j==0 else 0)
                           for j,m in enumerate(lit.ai.M)}}
        generic=expr.xreplace(substitute)
        out=nu_average(generic,d)
        for a in range(1,lit.ai.max_low(expr)+1):
            actual=expr.xreplace({lit.ai.n:nn,lit.ai.D:a,**{m:(nn-1 if j==0 else int(j==a))
                                   for j,m in enumerate(lit.ai.M)}})
            out+=lit.ai.nu_value(a)*(actual-generic.subs(d,a))
        return s.expand(out)

    for index,rec in enumerate(records):
        nn=int(rec['length'])
        d=s.Symbol('d',integer=True)
        t=s.Symbol('t',integer=True)
        generic=s.sympify(rec['generic_adjacent'],locals={'P':P})
        variable=next(iter(generic.free_symbols-{P}))
        correction=s.sympify(rec['low_corrections'],locals={'P':P})
        potential=-lit.ai.poly_sum(generic.subs(variable,t),t,d)-sum(correction)
        highest_average=nu_average(potential,d)
        for a in range(1,len(correction)):
            highest_average+=lit.ai.nu_value(a)*sum(correction[a:])
        cusp=s.expand(highest_average+sum((-1)**(order-j)*s.binomial(order-1,j-1)*
                            lower_average(engine.profiles[j],nn) for j in range(1,order)))
        expected=s.sympify(root['extra_ratio_rows'][index][order],locals={'P':P})
        assert s.factor(cusp-expected)==0,(nn,s.factor(cusp-expected))
        rows.append({'cusp_source_order':order,'parent_length':nn-1,'independent_dilaton_difference':'0'})
        print('independent cusp row verified',order,nn-1,flush=True)

    genus_row=engine.increment((0,0))
    for genus in range(1,order//2+1):
        ratio=engine.registry.volume_ratio(genus,0,order,nn=2)
        genus_row-=12*lit.f.h.volume(genus,2)*ratio[order]
    expected=s.sympify(root['extra_ratio_rows'][2][order],locals={'P':P})
    assert s.factor(genus_row-expected)==0
    rows.append({'genus_source_order':order,'parent_length':2,'independent_genus_difference':'0'})
    print('independent genus row verified',order,flush=True)
    output=HERE/f'c{args.volume_order}_extraction_checks.json'
    output.write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')


if __name__=='__main__':main()
