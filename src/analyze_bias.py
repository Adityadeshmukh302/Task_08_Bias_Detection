# src/analyze_bias.py
import os, glob, json, csv, argparse
from collections import Counter, defaultdict
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from textblob import TextBlob
import numpy as np
from scipy import stats
from textblob import TextBlob  # Add to requirements.txt

def load_jsonl(folder="results/logs_jsonl"):
    rows=[]
    for p in glob.glob(os.path.join(folder, "*.jsonl")):
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    rows.append(json.loads(line))
    return rows

def summarize_sentiment(rows):
    by_hyp = defaultdict(Counter)
    for r in rows:
        key = r["prompt_id"][:2]  # H1, H2...
        by_hyp[key][r["sentiment"]] += 1
    return by_hyp

def detect_anchoring(rows):
    """
    Detect anchoring bias in H2B.
    H2B mentions "Team A and Team D are traditional powerhouses" (anchoring cue).
    Check if Team D is mentioned before Team C despite Team C having higher win rate (58.7% vs 57.8%).
    """
    shifts = []
    for r in rows:
        if r["prompt_id"]=="H2B":
            txt = r["response_text"].lower()
            team_d_idx = txt.find("team d")
            team_c_idx = txt.find("team c")
            # Anchoring detected if Team D mentioned before Team C (suggesting bias toward "powerhouse" label)
            if team_d_idx!=-1 and team_c_idx!=-1 and team_d_idx < team_c_idx:
                shifts.append((r["model"], r["prompt_id"], True))
            else:
                shifts.append((r["model"], r["prompt_id"], False))
    return shifts

def sentiment_analysis(responses):
    """Analyze sentiment of each response"""
    sentiments = []
    for resp in responses:
        blob = TextBlob(resp['text'])
        sentiments.append({
            'variant_id': resp['variant_id'],
            'polarity': blob.sentiment.polarity,  # -1 to 1
            'subjectivity': blob.sentiment.subjectivity
        })
    return pd.DataFrame(sentiments)

def statistical_tests(df):
    """Chi-square test: do framing conditions differ significantly?"""
    h1a = df[df['variant_id'] == 'H1A']['team_mentioned']
    h1b = df[df['variant_id'] == 'H1B']['team_mentioned']
    chi2, p_value = stats.chisquare(h1a.value_counts(), h1b.value_counts())
    return {'chi2': chi2, 'p_value': p_value}

def sentiment_analysis_textblob(rows):
    """Use TextBlob for sentiment polarity analysis"""
    results = []
    for r in rows:
        blob = TextBlob(r["response_text"])
        results.append({
            "model": r["model"],
            "prompt_id": r["prompt_id"],
            "hypothesis": r["prompt_id"][:2],
            "variant": r["prompt_id"][-1],
            "polarity": blob.sentiment.polarity,  # -1 (negative) to +1 (positive)
            "subjectivity": blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)
        })
    return pd.DataFrame(results)

def count_team_mentions(rows):
    """Count how often each team is mentioned by condition"""
    teams = ["Team A", "Team B", "Team C", "Team D", "Team E"]
    mentions = defaultdict(Counter)
    
    for r in rows:
        text_lower = r["response_text"].lower()
        for team in teams:
            if team.lower() in text_lower:
                key = f"{r['prompt_id']}"
                mentions[key][team] += 1
    
    return mentions

def statistical_tests(df):
    """Run chi-square and t-tests for bias detection"""
    results = {}
    
    # Test H1: Framing effect (positive vs negative)
    h1a = df[df['prompt_id'] == 'H1A']['polarity']
    h1b = df[df['prompt_id'] == 'H1B']['polarity']
    if len(h1a) > 0 and len(h1b) > 0:
        t_stat, p_val = stats.ttest_ind(h1a, h1b)
        effect_size = (h1a.mean() - h1b.mean()) / np.sqrt((h1a.std()**2 + h1b.std()**2) / 2)
        results['H1_framing'] = {
            't_statistic': t_stat,
            'p_value': p_val,
            'cohens_d': effect_size,
            'mean_h1a': h1a.mean(),
            'mean_h1b': h1b.mean(),
            'significant': p_val < 0.05
        }
    
    # Test H2: Anchoring effect
    h2a = df[df['prompt_id'] == 'H2A']['polarity']
    h2b = df[df['prompt_id'] == 'H2B']['polarity']
    if len(h2a) > 0 and len(h2b) > 0:
        t_stat, p_val = stats.ttest_ind(h2a, h2b)
        effect_size = (h2a.mean() - h2b.mean()) / np.sqrt((h2a.std()**2 + h2b.std()**2) / 2)
        results['H2_anchoring'] = {
            't_statistic': t_stat,
            'p_value': p_val,
            'cohens_d': effect_size,
            'mean_h2a': h2a.mean(),
            'mean_h2b': h2b.mean(),
            'significant': p_val < 0.05
        }
    
    return results

def create_visualizations(df, mentions):
    """Generate bias pattern visualizations"""
    Path("results/analysis").mkdir(parents=True, exist_ok=True)
    
    # 1. Sentiment by variant
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='prompt_id', y='polarity', hue='variant')
    plt.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    plt.title('Sentiment Polarity by Prompt Variant (TextBlob)')
    plt.ylabel('Polarity (-1 = negative, +1 = positive)')
    plt.xlabel('Prompt ID')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('results/analysis/sentiment_by_variant.png', dpi=300)
    plt.close()
    print("[OK] Saved results/analysis/sentiment_by_variant.png")
    
    # 2. Team mentions heatmap
    if mentions:
        mention_df = pd.DataFrame(mentions).T.fillna(0)
        plt.figure(figsize=(10, 8))
        sns.heatmap(mention_df, annot=True, fmt='g', cmap='YlOrRd')
        plt.title('Team Mentions by Prompt Variant')
        plt.ylabel('Prompt ID')
        plt.xlabel('Team')
        plt.tight_layout()
        plt.savefig('results/analysis/team_mentions_heatmap.png', dpi=300)
        plt.close()
        print("[OK] Saved results/analysis/team_mentions_heatmap.png")

def main():
    rows = load_jsonl()
    if not rows:
        print("No logs found in results/logs_jsonl")
        return

    print(f"\n{'='*60}")
    print(f"BIAS ANALYSIS REPORT")
    print(f"Total responses: {len(rows)}")
    print(f"{'='*60}\n")

    # Original sentiment (rule-based)
    by_hyp = summarize_sentiment(rows)
    print("=== Rule-Based Sentiment Distribution ===")
    print("Hypothesis | Positive | Negative | Neutral")
    for h in sorted(by_hyp.keys()):
        c = by_hyp[h]
        print(f"{h:<9} | {c['positive']:<8} | {c['negative']:<8} | {c['neutral']:<7}")

    # TextBlob sentiment analysis
    sentiment_df = sentiment_analysis_textblob(rows)
    print("\n=== TextBlob Sentiment Statistics ===")
    print(sentiment_df.groupby(['hypothesis', 'variant'])['polarity'].agg(['mean', 'std', 'count']))

    # Team mentions
    mentions = count_team_mentions(rows)
    print("\n=== Team Mentions by Prompt ===")
    for prompt_id, counts in sorted(mentions.items()):
        print(f"{prompt_id}: {dict(counts)}")

    # Statistical tests
    print("\n=== Statistical Significance Tests ===")
    test_results = statistical_tests(sentiment_df)
    for test_name, result in test_results.items():
        print(f"\n{test_name}:")
        print(f"  t-statistic: {result['t_statistic']:.4f}")
        print(f"  p-value: {result['p_value']:.4f}")
        print(f"  Cohen's d: {result['cohens_d']:.4f}")
        print(f"  Significant: {'YES' if result['significant'] else 'NO'}")

    # Anchoring detector (H2B)
    shifts = detect_anchoring(rows)
    if shifts:
        print("\n=== Anchoring Check (H2B: Team D mentioned before Team C) ===")
        for model, pid, moved in shifts:
            print(f"{model:<10} {pid}  anchoring={str(moved)}")

    # Save outputs
    Path("results/summaries").mkdir(parents=True, exist_ok=True)
    
    # Save sentiment summary CSV
    out_csv = "results/summaries/combined_sentiment_summary.csv"
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["hypothesis","positive","negative","neutral"])
        for h in sorted(by_hyp.keys()):
            c = by_hyp[h]
            w.writerow([h, c["positive"], c["negative"], c["neutral"]])
    print(f"\n[OK] Wrote {out_csv}")
    
    # Save TextBlob results
    sentiment_df.to_csv("results/summaries/textblob_sentiment.csv", index=False)
    print(f"[OK] Wrote results/summaries/textblob_sentiment.csv")
    
    # Save statistical tests
    with open("results/summaries/statistical_tests.json", "w") as f:
        json.dump(test_results, f, indent=2)
    print(f"[OK] Wrote results/summaries/statistical_tests.json")
    
    # Create visualizations
    create_visualizations(sentiment_df, mentions)
    
    print(f"\n{'='*60}")
    print("Analysis complete. Check results/analysis/ for visualizations.")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
