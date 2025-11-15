# src/validate_claims.py
import re, os, json, argparse
import pandas as pd
from pathlib import Path

TEAM_PATTERNS = {
    "Team A": r"team\s*a[^0-9]*(\d{1,2}\.?\d*)\s*%",
    "Team B": r"team\s*b[^0-9]*(\d{1,2}\.?\d*)\s*%",
    "Team C": r"team\s*c[^0-9]*(\d{1,2}\.?\d*)\s*%",
    "Team D": r"team\s*d[^0-9]*(\d{1,2}\.?\d*)\s*%",
    "Team E": r"team\s*e[^0-9]*(\d{1,2}\.?\d*)\s*%"
}

def compute_true_winrates(df: pd.DataFrame, teams):
    # FIXED ground truth values matching the experimental design.
    # All models received these exact values, so validation compares against them.
    # ANONYMIZED: Team A/B/C/D/E per assignment requirements
    truth = {
        "Team A": 63.5,  # Originally Brazil
        "Team B": 59.2,  # Originally Argentina
        "Team C": 58.7,  # Originally Spain
        "Team D": 57.8,  # Originally Germany
        "Team E": 55.1   # Originally England
    }
    return {t: truth.get(t) for t in teams if t in truth}

def extract_claims(text: str):
    claims={}
    lt = text.lower()
    for team, pat in TEAM_PATTERNS.items():
        m = re.search(pat, lt, flags=re.I)
        if m:
            try:
                claims[team] = float(m.group(1))
            except:
                pass
    return claims

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="data/results.csv")
    ap.add_argument("--jsonl_folder", default="results/logs_jsonl")
    ap.add_argument("--tolerance", type=float, default=0.5, help="percentage points tolerance")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    df['date'] = df['date'].astype(str)
    truth = compute_true_winrates(df, list(TEAM_PATTERNS.keys()))

    mismatches=[]
    for p in Path(args.jsonl_folder).glob("*.jsonl"):
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            record = json.loads(line)
            claims = extract_claims(record["response_text"])
            for team, v in claims.items():
                tv = truth.get(team)
                if tv is None: continue
                if abs(v - tv) > args.tolerance:
                    mismatches.append({
                        "file": p.name,
                        "model": record["model"],
                        "prompt_id": record["prompt_id"],
                        "team": team,
                        "claimed": v,
                        "truth": tv,
                        "delta_pp": round(v-tv, 2)
                    })

    out = "results/summaries/claim_validation_report.json"
    Path("results/summaries").mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps({"truth": truth, "mismatches": mismatches}, indent=2), encoding="utf-8")
    print(f"[OK] Wrote {out}")
    if mismatches:
        print(f"Found {len(mismatches)} mismatches beyond ±{args.tolerance} pp")
    else:
        print("No mismatches beyond tolerance.")

if __name__ == "__main__":
    main()
