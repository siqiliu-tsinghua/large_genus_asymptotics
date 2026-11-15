"""Reproduce the supplementary coefficient check without changing paper inputs."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,subprocess,sys
sys.dont_write_bytecode=True
BUNDLE=Path(__file__).resolve().parent
# Installed destination: sections/04_lambda_one/checks/run.py.
ROOT=BUNDLE.parents[2]
STAGE=ROOT/"build/s04-higher-check"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprints():
    files=sorted((BUNDLE/"source").rglob("*.py"))
    assert files,"The calculation source bundle is missing."
    files += sorted((ROOT/"sections/a_coefficients/calculations").glob("*.py"))
    files.append(Path(__file__).resolve())
    return {p.relative_to(ROOT).as_posix():sha(p) for p in files}


def assert_staged():
    for source in sorted((BUNDLE/"source").rglob("*.py")):
        staged=STAGE/source.relative_to(BUNDLE/"source")
        assert staged.is_file() and sha(staged)==sha(source),"Staged source changed."


def run():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-existing",action="store_true",
                        help="Verify the saved execution receipt and exact result.")
    args=parser.parse_args()
    assert (ROOT/"main.tex").is_file(),"Run the installed repository bundle."
    assert STAGE.resolve().is_relative_to((ROOT/"build").resolve())
    before=fingerprints()
    receipt_path=STAGE/"verification_receipt.json"
    output=STAGE/"math/computed_coefficients.json"
    if args.verify_existing:
        receipt=json.loads(receipt_path.read_text(encoding="utf-8"))
        assert receipt["source_sha256"]==before,"Calculation sources changed; recompute."
        assert sha(output)==receipt["result_sha256"],"Saved coefficient output changed."
        assert_staged()
    else:
        for source in sorted((BUNDLE/"source").rglob("*.py")):
            rel=source.relative_to(BUNDLE/"source")
            destination=STAGE/rel
            destination.parent.mkdir(parents=True,exist_ok=True)
            if not destination.exists() or destination.read_bytes()!=source.read_bytes():
                destination.write_bytes(source.read_bytes())
        assert_staged()
        env=dict(os.environ,PYTHONUTF8="1",PYTHONDONTWRITEBYTECODE="1")
        commands=[
            ["writer/profile_engine.py","--through","4"],
            ["root/reconstruct_volumes.py","--order","3"],
            ["root/reconstruct_volumes.py","--order","4"],
            ["math/higher_blocks.py"],
            ["math/compose_final.py"]]
        for command in commands:
            print("Recomputing "+command[0],flush=True)
            subprocess.run([sys.executable,"-B",str(STAGE/command[0]),*command[1:]],
                           cwd=ROOT,env=env,check=True)
    assert fingerprints()==before,"Calculation sources changed during checking."
    assert_staged()
    # Targets enter only HERE, after all independent reconstruction has finished.
    sys.path.insert(0,str(ROOT/"sections/a_coefficients/calculations"))
    import runtime
    runtime.require_symbolic()
    import sympy as s
    P=s.Symbol("P",positive=True)
    targets={
        "3":s.Rational(62909,15360)+s.Rational(251,192)/P-s.Rational(5,16)/P**2,
        "4":s.Rational(291371,32768)+s.Rational(129871,15360)/P
                  -s.Rational(277,64)/P**2+s.Rational(105,64)/P**3}
    result=json.loads(output.read_text(encoding="utf-8"))
    differences={}
    for order,target in targets.items():
        actual=s.sympify(result["coefficients"][order]["expression"],locals={"P":P})
        difference=s.factor(actual-target)
        assert difference==0,(order,difference)
        differences[order]=str(difference)
        print("Verified g^-"+order+": "+str(actual),flush=True)
    receipt={
        "schema_version":1,"passed":True,
        "normalization":"sqrt(pi)*exp(-Cin(2*pi))*a_g/N_g",
        "method":"Exact recursions, signed moments and complete rooted-core sums",
        "source_sha256":before,"result_sha256":sha(output),
        "target_comparison_after_reconstruction":differences,
        "versions":{"sympy":s.__version__},
        "time":datetime.now(timezone.utc).isoformat()}
    STAGE.mkdir(parents=True,exist_ok=True)
    if not args.verify_existing:
        receipt_path.write_text(json.dumps(receipt,indent=2)+"\n",
                                encoding="utf-8",newline="\n")
    print("Both higher coefficients agree exactly.",flush=True)


if __name__=="__main__":
    run()
