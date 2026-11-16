"""Independent absolute-volume bases from one extra order of exact recursions."""
from pathlib import Path
import sys,json,argparse
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(HERE))
sys.path.insert(0,str(ROOT/"build/s04-higher-check/writer"))
import asymptotic_inputs as a
import profile_engine as pe
import one_positive as op
from absolute_volumes import identify_absolute


def reconstruct(order,profile_path=None):
    reg=a.initial_registry()
    vals=pe.load_profiles(profile_path) if profile_path else pe.load_profiles()
    for r in range(3,order+1):
        assert r in vals,("Missing full profile",r)
        reg.register_profile(r,vals[r])
        reg.compute_ratios(r)
    if order>=4:
        previous=json.loads((HERE/"volume3.json").read_text(encoding="utf-8"))
        reg.volumes[3]=a.s.sympify(previous["volume_polynomial"],
                                 locals={"n":a.n,"P":a.P})
    engine=pe.ProfileEngine(reg)
    def callback(r,pivot,registry,**kwargs):
        assert registry is reg
        return engine.adjacent_at(r,pivot,kwargs["parent_n"],
                                  kwargs["parent_degree"],kwargs["parent_counts"])
    rows,records=op.extra_ratio_rows(callback,reg,order+1)
    result,increment,at_two=identify_absolute(reg,order,rows)
    report={"volume_order":order,
            "normalization":"genus G^-r in fixed-marking absolute WP expansion",
            "method":"Exact adjacent/dilaton/genus rows at r+1; unknown next absolute coefficient cancels",
            "no_high_hodge_target_input":True,
            "volume_polynomial":str(result),
            "base_at_zero":str(a.s.factor(result.subs(a.n,0))),
            "at_two":str(a.s.factor(at_two)),
            "increment":str(increment),
            "extra_ratio_rows":[[str(x) for x in row] for row in rows],
            "one_positive_records":[{k:str(v) for k,v in x.items()} for x in records]}
    dest=HERE/f"volume{order}.json"
    dest.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8",newline="\n")
    print("Reconstructed absolute volume order",order,flush=True)
    print("Base at zero:",report["base_at_zero"],flush=True)
    print("Saved",dest.as_posix(),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--order",type=int,required=True)
    parser.add_argument("--profiles")
    args=parser.parse_args()
    reconstruct(args.order,args.profiles)
