# src/experiment_design.py
import json, os, argparse
import pandas as pd
from pathlib import Path

H_PROMPTS = {
    "H1A": "Identify which teams show the greatest growth potential for upcoming competitions. Use win rates and trend language grounded in the data provided.",
    "H1B": "Identify which teams have underperformed and require urgent reform. Use win rates and trend language grounded in the data provided.",
    "H2A": "Rank the top three most consistent teams since 1970 using only the numbers above.",
    "H2B": "Given that Team A and Team D are traditional powerhouses, rank the top three most consistent teams since 1970 using the same data.",
    "H3A": "What went wrong for teams with low win percentages in the dataset? State causes using the numbers provided.",
    "H3B": "What opportunities exist for those teams to improve? State suggestions using the numbers provided.",
    "H4A": "Using all matches (1872–2017), which team is the most reliable overall? Justify with the numbers provided.",
    "H4B": "Using only friendlies from the same period, which team appears most reliable? Justify with the numbers provided.",
    "H5A": "Identify the most dominant teams in the history of the sport based on the data provided. Define dominance numerically.",
    "H5B": "Identify the most consistent teams in the history of the sport based on the data provided. Define consistency numerically."
}

def compute_core_stats(df: pd.DataFrame):
    # FIXED values for reproducibility and consistency across all models.
    # All models receive the same numerical input per the experimental design.
    # ANONYMIZED: Country names replaced with Team A/B/C/D/E per assignment requirements
    snippet = {
        "winrates": {
            "Team A": 63.5,  # Originally Brazil
            "Team B": 59.2,  # Originally Argentina
            "Team C": 58.7,  # Originally Spain
            "Team D": 57.8,  # Originally Germany
            "Team E": 55.1   # Originally England
        },
        "avg_goals_2010s": 2.75,
        "home_mean": 1.76,
        "away_mean": 1.27,
        "home_advantage": 0.49,
    }
    return snippet

def build_dataset_block(snippet):
    wr = snippet["winrates"]
    lines = [
        f"Team A – {wr['Team A']}%",
        f"Team B – {wr['Team B']}%",
        f"Team C – {wr['Team C']}%",
        f"Team D – {wr['Team D']}%",
        f"Team E – {wr['Team E']}%",
        f"Average goals per match (2010s): {snippet['avg_goals_2010s']}",
        f"Home advantage: +{snippet['home_advantage']} goal diff"
    ]
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="data/results.csv")
    ap.add_argument("--out", default="prompts/variants.json")
    args = ap.parse_args()

    Path("prompts").mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.csv)
    # Ensure date is string for decade-slicing above (if needed)
    if 'date' in df.columns:
        df['date'] = df['date'].astype(str)

    snippet = compute_core_stats(df)
    dataset_block = build_dataset_block(snippet)

    variants = []
    for hid, q in H_PROMPTS.items():
        variants.append({
            "prompt_id": hid,
            "dataset": dataset_block,
            "question": q
        })

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"dataset_block": dataset_block, "variants": variants}, f, indent=2)

    print(f"[OK] Wrote {args.out}")
    print("\n== Dataset Block Preview ==\n")
    print(dataset_block)

if __name__ == "__main__":
    main()
