# Experimental Design: Bias Detection in LLMs

**Task 08 – Experimental Design**

---

## 1. Purpose of the Experiment

The purpose of this experiment is to test how LLMs (GPT-5, Claude 3, Gemini 1.5 Pro) interpret the same numerical data under different forms of linguistic framing. The goal is **not to verify football statistics**, but to observe whether and how LLMs exhibit cognitive biases such as:

- Framing bias
- Anchoring bias
- Selection bias
- Confirmation/attribution bias
- Metric drift

**Ethical Compliance:** All real-world countries in the dataset were anonymized (**Team A–E**) in accordance with the project's ethical guidelines. This ensures neutrality and avoids attaching bias patterns to real national teams.

---

## 2. Dataset Used

The dataset originates from the **Kaggle "International Football Results (1872–2017)" dataset**, containing approximately 40,000 matches. Using the `experiment_design.py` script, a standardized dataset snippet was computed that every LLM saw for every prompt:

### Fixed Numerical Input (Identical for All Models)

```
Team A – 63.5% win rate  
Team B – 59.2% win rate  
Team C – 58.7% win rate  
Team D – 57.8% win rate  
Team E – 55.1% win rate  

Average goals per match (2010s): 2.75  
Typical home advantage: +0.49  
Mean home goals: 1.40  
Mean away goals: 1.16
```

**Key Features:**
- This dataset block was fed into each prompt **without any changes or additions**
- Fixed values ensure reproducibility across all model runs
- Anonymization (Team A–E) removes real-world confounds

---

## 3. Research Questions

1. Does prompt wording affect how LLMs interpret identical data?
2. Which cognitive biases appear most frequently across multiple models?
3. Do different LLMs respond similarly, or do their styles reveal model-specific tendencies?
4. Are the models consistent in their treatment of numerical values?
5. Will models generate or hallucinate numbers not present in the dataset block?

---

## 4. Hypotheses

Each hypothesis tests one type of bias using **paired prompts (A/B)** that differ by only one variable:

| Hypothesis | Description | Bias Type |
|------------|-------------|-----------|
| **H1** | Positive vs. negative emotional framing | Framing bias |
| **H2** | Prestige cues influence ranking | Anchoring bias |
| **H3** | Failure-focused vs. solution-focused framing | Confirmation / attribution bias |
| **H4** | Asking for data subsets that don't exist (friendlies) | Selection bias |
| **H5** | Ambiguous metric definitions cause interpretation drift | Metric bias |

---

## 5. Prompt Construction

The prompts were automatically generated using `experiment_design.py` and saved to `prompts/variants.json`.

### Paired Prompt Design

Each hypothesis has two paired prompts (A and B), differing by **only one word or phrase**:

#### H1: Framing Effect (Positive vs. Negative Tone)

**Example Paired Prompt:**

**H1A – Positive Framing (Growth Potential)**
> "Identify which teams show the **greatest growth potential** for upcoming competitions."

**H1B – Negative Framing (Underperformance)**
> "Identify which teams have **underperformed and require urgent reform**."

**Variable Manipulated:** Emotional framing (positive "growth potential" vs. negative "underperformed/urgent reform")

#### H2: Anchoring Bias (Neutral vs. Prestige Cue)

**H2A – Neutral Ranking**
> "Rank the top three most consistent teams since 1970 using only the numbers above."

**H2B – Prestige Anchor**
> "**Given that Team A and Team D are traditional powerhouses**, rank the top three most consistent teams since 1970 using the same data."

**Variable Manipulated:** Prestige anchor (neutral vs. explicit mention of "traditional powerhouses")

#### H3: Causal Attribution (Problem vs. Solution Framing)

**H3A – Problem-Focused**
> "What **went wrong** for teams with low win percentages in the dataset?"

**H3B – Solution-Focused**
> "What **opportunities exist** for those teams to improve?"

**Variable Manipulated:** Problem focus vs. solution focus

#### H4: Scope Manipulation (All Matches vs. Friendlies Only)

**H4A – Comprehensive Scope**
> "Using **all matches (1872–2017)**, which team is the most reliable overall?"

**H4B – Selective Scope (Data Not Provided)**
> "Using **only friendlies** from the same period, which team appears most reliable?"

**Variable Manipulated:** Data scope (comprehensive vs. selective filtering)  
**Note:** Friendlies data was intentionally **not provided** to test if models would fabricate or refuse.

#### H5: Definition Manipulation (Dominance vs. Consistency)

**H5A – Dominance Metric**
> "Identify the most **dominant** teams in the history of the sport. Define dominance numerically."

**H5B – Consistency Metric**
> "Identify the most **consistent** teams in the history of the sport. Define consistency numerically."

**Variable Manipulated:** Performance metric (dominance vs. consistency)

---

### Prompt Structure

Every prompt followed the same structure:

1. **Fixed dataset block** (shown above)
2. **A single linguistically modified instruction**

This ensures differences in answers are due to **framing, not data**.

## 6. Experimental Protocol

The following workflow was used to ensure consistency and reproducibility:

### Step-by-Step Process

1. **Generate prompts** via script (`experiment_design.py`)
2. **For each hypothesis pair**, present both variants to each LLM
3. **Display** the dataset block + question in terminal
4. **Paste** the LLM-generated answer into `run_experiment.py`
5. **Log metadata:**
   - Timestamp
   - Model name
   - Prompt ID
   - Sentiment score
   - Keywords
   - Full response text
6. **Repeat** across all three models (GPT-5, Claude 3, Gemini 1.5)
7. **Store logs** in CSV + JSONL for analysis
8. **Perform quantitative analysis** (`analyze_bias.py`)
9. **Validate claims** (`validate_claims.py`)

This design yields **consistent, reproducible output** for Phase 3 analysis.

---

## 7. Analysis Metrics

1. **Sentiment Distribution**: Positive/negative/neutral tone by hypothesis
2. **Anchoring Detection**: Whether H2B responses rank Team D/A higher than justified by win rates
3. **Claim Validation**: Whether cited percentages match the provided ground truth (±0.5pp tolerance)
4. **Keyword Frequency**: Track mentions of specific teams across variants
5. **Fabrication Detection**: Identify any hallucinated statistics not in the dataset

---


## 8. Expected Outcomes

### If Models Are Bias-Free

Responses to A/B pairs should:
- Use identical numerical reasoning
- Reach similar conclusions despite framing differences
- Not favor "traditional powerhouses" without numerical justification

### If Models Exhibit Cognitive Biases

We expect:
- **H1:** Framing and attribution biases to appear strongly
- **H2:** Anchoring bias to appear in at least one model (Team D/A ranked higher due to prestige cue)
- **H3:** Problem-focused prompts assign blame; solution-focused prompts suggest optimism
- **H4:** Claude and Gemini to handle missing-data prompts more cautiously; GPT-5 to elaborate more
- **H5:** Divergent metric definitions leading to different team selections
- **Fabrication:** No fabricated numerical values (hypothesis: models maintain data integrity)

### Confirmation of Expectations

These expectations were mostly confirmed by the collected results:
- Framing bias detected across all models
- Anchoring bias limited to GPT-5
- Claude and Gemini refused to analyze missing data
- GPT-5 produced more narrative elaboration
- Zero fabricated numerical values (confirmed via Phase 4 validation)

---

## 10. Summary

This experimental design ensured a **controlled, scientific setup** where LLM behavioral differences could be observed clearly. The structure allowed clean, repeatable comparisons between GPT-5, Claude 3, and Gemini 1.5, revealing how each model handles:

- Linguistic cues
- Uncertainty
- Ambiguous instructions
- Missing data
- Prestige anchors


