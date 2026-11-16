"""Reproduce the two next normalized Hodge coefficients from exact inputs.

No proposed third/fourth coefficient is embedded, read, fitted or asserted.
The independent paired functional computes Q03,Q04,Q13; the other groups
were computed by higher_blocks.py from exact core integration.

Example:
  python -B build/s04-higher-check/math/compose_final.py --profiles PATH
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import finite_functional as f
s,P=f.s,f.P
NAMES={'P':P,'n':f.N,'D':f.DD,
       **{f'm{j}':s.Symbol(f'm{j}',integer=True) for j in range(25)}}


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def expression(value):
    return s.expand(s.sympify(value,locals=NAMES))


def read_profiles(path):
    record=read_json(path)
    profiles={int(k):expression(value) for k,value in record['profiles'].items()}
    assert all(j in profiles for j in range(5)), 'Full exact e0,...,e4 inputs are required'
    allowed={P,f.N,f.DD,*f.M}
    for j in range(5):
        assert profiles[j].free_symbols<=allowed,(j,profiles[j].free_symbols-allowed)
        assert not profiles[j].has(s.Float),('inexact profile input',j)
    for j,old in f.canonical_profiles().items():
        assert s.expand(profiles[j]-old)==0,('Changed admitted profile',j)
    for j in range(1,5):
        zero={f.DD:0,**{m:(f.N if a==0 else 0) for a,m in enumerate(f.M)}}
        assert s.expand(profiles[j].xreplace(zero))==0,('zero-tuple profile',j)
    return profiles


def read_volumes(paths):
    volumes=f.canonical_volumes()
    for order,path in paths.items():
        record=read_json(path)
        assert record['volume_order']==order
        volume=expression(record['volume_polynomial'])
        assert volume.free_symbols<={P,f.N}
        assert not volume.has(s.Float)
        assert s.expand(volume.subs(f.N,0)-expression(record['base_at_zero']))==0
        volumes[order]=volume
    return volumes


def scalar(expr):
    expr=s.expand(expr)
    assert expr.free_symbols<={P},('Uneliminated moment/statistic',expr.free_symbols)
    assert not expr.has(s.Float)
    numerator,denominator=s.fraction(s.cancel(expr))
    assert len(s.Poly(denominator,P).terms())==1,'Expected an exact Laurent polynomial in P'
    return expr


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--profiles',type=Path,default=HERE.parent/'writer/profiles.json')
    parser.add_argument('--volume3',type=Path,default=HERE.parent/'root/volume3.json')
    parser.add_argument('--volume4',type=Path,default=HERE.parent/'root/volume4.json')
    parser.add_argument('--blocks',type=Path,default=HERE/'higher_blocks.json')
    parser.add_argument('--output',type=Path,default=HERE/'computed_coefficients.json')
    parser.add_argument('--digits',type=int,default=60)
    args=parser.parse_args()
    # Preparation ownership: every generated artifact stays in this math directory.
    output=args.output.resolve()
    assert output.is_relative_to(HERE),'Preparation output must stay in the assigned math directory'
    profiles=read_profiles(args.profiles)
    volumes=read_volumes({3:args.volume3,4:args.volume4})
    source_blocks=read_json(args.blocks)['blocks']
    groups={key:scalar(expression(source_blocks[key]))
            for key in ('Q12','Q21','Q30','Q22','Q31','Q40')}
    for q,order in ((0,3),(0,4),(1,3)):
        print('Computing exact absolute group',q,order,flush=True)
        groups[f'Q{q}{order}']=scalar(f.absolute_group(q,order,profiles,volumes))
        print('Computed',f'Q{q}{order}',groups[f'Q{q}{order}'],flush=True)
    third=scalar(sum(groups[key] for key in ('Q03','Q12','Q21','Q30')))
    fourth=scalar(sum(groups[key] for key in ('Q04','Q13','Q22','Q31','Q40')))
    inputs={'profiles':args.profiles,'volume3':args.volume3,
            'volume4':args.volume4,'core_blocks':args.blocks}
    result={
      'normalization':'sqrt(pi)*exp(-Cin(2*pi))*a_g/N_g',
      'method':'Exact new normalized descendant/absolute volume inputs, paired signed moments, and rooted-core integrals; no Hodge target input or fitting',
      'human_blinding':'Reviewer saw USER-006 candidates; neither is consumed by this calculation',
      'inputs':{key:{'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
                for key,path in inputs.items()},
      'groups':{key:str(value) for key,value in sorted(groups.items())},
      'coefficients':{
        '3':{'expression':str(third),'decimal':str(s.N(third.subs(P,s.pi**2),args.digits))},
        '4':{'expression':str(fourth),'decimal':str(s.N(fourth.subs(P,s.pi**2),args.digits))}},
      'decimal_digits':args.digits,
      'precision_scope':'These are the next two coefficient values; this script does not modify the Introduction or the proved theorem precision'}
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    for order,expr in ((3,third),(4,fourth)):
        print('NORMALIZED COEFFICIENT',order,expr,flush=True)
        print('decimal',result['coefficients'][str(order)]['decimal'],flush=True)
    print('Wrote',output,flush=True)


if __name__=='__main__':main()
