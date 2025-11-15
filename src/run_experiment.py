# src/run_experiment.py
import os, json, csv, argparse, time
from pathlib import Path
try:
    from dotenv import load_dotenv
except Exception:
    # Make dotenv optional so the script fails more gracefully when the package
    # isn't installed (common when running with a system python that lacks deps).
    def load_dotenv(*a, **k):
        return None
    print("[WARN] python-dotenv not available; skipping .env load. Install with `pip install python-dotenv` if needed.")

load_dotenv()

def load_variants(path="prompts/variants.json"):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Variants file not found: {path}. Run `python src/experiment_design.py` to generate prompts/variants.json or provide --variants.")
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def ensure_dirs():
    Path("results/logs_csv").mkdir(parents=True, exist_ok=True)
    Path("results/logs_jsonl").mkdir(parents=True, exist_ok=True)

def rule_based_sentiment(text: str) -> str:
    neg = ["underperform","urgent","poor","failure","weak","struggling","declined","worrying"]
    pos = ["growth","improve","opportunity","potential","reliable","strong","excel","promising"]
    score = 0
    lt = text.lower()
    for w in neg:  score -= lt.count(w)
    for w in pos:  score += lt.count(w)
    return "positive" if score>0 else "negative" if score<0 else "neutral"

def log_row_csv(csv_path, row, header=None):
    write_header = not Path(csv_path).exists()
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header or list(row.keys()))
        if write_header: w.writeheader()
        w.writerow(row)

def log_row_jsonl(jsonl_path, row):
    with open(jsonl_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

def interactive_collect(model_name, variants, samples=3, runs_per_prompt=1, model_version="unknown"):
    """
    Interactive data collection supporting multiple runs per prompt.
    
    Args:
        model_name: Model label (e.g., 'Claude3', 'GPT4', 'Gemini')
        variants: List of prompt variants from variants.json
        samples: Number of samples (deprecated - use runs_per_prompt)
        runs_per_prompt: Number of independent runs per prompt (3-5 recommended)
        model_version: Exact model version string for reproducibility
    """
    ensure_dirs()
    csv_path  = f"results/logs_csv/{model_name}_outputs.csv"
    jsonl_path= f"results/logs_jsonl/{model_name}_outputs.jsonl"

    for v in variants:
        for run in range(1, runs_per_prompt+1):
            print("\n========================================")
            print(f"Model: {model_name} | Version: {model_version}")
            print(f"Prompt: {v['prompt_id']} | Run: {run}/{runs_per_prompt}")
            print("----- DATASET -----")
            print(v["dataset"])
            print("----- QUESTION ----")
            print(v["question"])
            print("\nPaste the model's response below. Finish with a blank line:\n")
            lines=[]
            while True:
                line=input()
                if line.strip()=="":
                    break
                lines.append(line)
            response="\n".join(lines).strip()
            ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            sentiment = rule_based_sentiment(response)
            row = {
                "timestamp": ts,
                "model": model_name,
                "model_version": model_version,
                "prompt_id": v["prompt_id"],
                "variant": v["prompt_id"][-1],  # A or B
                "run_id": run,
                "prompt_text": f"DATA:\n{v['dataset']}\nTASK:\n{v['question']}",
                "response_text": response,
                "sentiment": sentiment,
                "keywords": ",".join([k for k in ["Team A","Team B","Team C","Team D","Team E","friendlies","consistency","dominance","reliable","powerhouse"]
                                      if k.lower() in response.lower()])
            }
            log_row_csv(csv_path, row)
            log_row_jsonl(jsonl_path, row)
            print(f"[OK] Logged to {csv_path} and {jsonl_path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variants", default="prompts/variants.json")
    ap.add_argument("--model", default="Claude3", help="Name label for logs (e.g., GPT4 / Claude3 / Gemini)")
    ap.add_argument("--runs", type=int, default=3, help="Number of independent runs per prompt (3-5 recommended)")
    ap.add_argument("--model-version", default="unknown", help="Exact model version for reproducibility (e.g., gpt-4-0125-preview)")
    args = ap.parse_args()

    data = load_variants(args.variants)
    variants = data["variants"]

    print(f"\n{'='*60}")
    print(f"BIAS DETECTION EXPERIMENT")
    print(f"Model: {args.model} | Version: {args.model_version}")
    print(f"Prompts: {len(variants)} | Runs per prompt: {args.runs}")
    print(f"Total responses needed: {len(variants) * args.runs}")
    print(f"{'='*60}\n")

    # Manual interactive (web UI copy/paste)
    interactive_collect(args.model, variants, runs_per_prompt=args.runs, model_version=args.model_version)

if __name__ == "__main__":
    main()
