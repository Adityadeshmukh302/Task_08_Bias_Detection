# Task 08: Bias Detection in LLM Data Narratives



## Project Overview



This research project investigates how subtle variations in data presentation can trigger cognitive biases in Large Language Models (LLMs), particularly when they interpret and summarize statistical information. Rather than testing explicit manipulation, we explore whether phenomena documented in human decision-making—such as **framing effects**, **anchoring bias**, **attribution bias**, **selection bias**, and **metric bias**—manifest in LLM-generated narratives about the same underlying dataset.**Author:** Aditya Deshmukh  ## Research Project Overview



The central question is: **Do LLMs exhibit systematic bias patterns when presented with identical data in different formats?** This matters because LLMs are increasingly used to summarize complex datasets in journalism, business intelligence, education, and policy contexts. If subtle presentation differences lead to systematically different interpretations, users may receive biased narratives without realizing the information source was identical.**Course:** Research Task 8 - Syracuse University  



## What This Project Does**Submission Date:** November 15, 2025This project investigates bias detection in Large Language Model (LLM) data narratives.



1. **Data Anonymization & Ground Truth Establishment**

   - Uses the International Football Results dataset (1872-2017, ~40,000 matches from Kaggle)

   - Anonymizes country names to Team A through Team E to remove cultural associations## Overview## Project Structure

   - Establishes **fixed ground truth values** for reproducibility:

     - Team A: 63.5% win rate

     - Team B: 59.2% win rate

     - Team C: 58.7% win rateThis project systematically evaluates cognitive biases in Large Language Model (LLM) data narratives through controlled experimental manipulation. Using identical numerical datasets, we test whether prompt framing causes LLMs to generate systematically different conclusions.```

     - Team D: 57.8% win rate

     - Team E: 55.1% win rateResearch_task08_Bias_detection/

     - Average goals per match: 2.75

     - Home advantage: 0.49 goals## Quick Start├── data/



2. **Hypothesis Testing Through Paired Prompts**│   └── results.csv          # Input dataset (manually populated)

   - Tests 5 specific cognitive biases with 10 total prompts (2 variants per hypothesis)

   - **H1 (Framing)**: Win percentages vs. loss percentages### 1. Setup Environment├── src/

   - **H2 (Anchoring)**: High-to-low vs. low-to-high team ordering

   - **H3 (Attribution)**: Home advantage emphasis vs. competitive balance emphasis│   ├── experiment_design.py # Generate experimental prompts

   - **H4 (Selection)**: Top 3 teams vs. bottom 2 teams prominence

   - **H5 (Metric)**: Goal-based vs. percentage-based analysis```bash│   ├── run_experiment.py    # Execute LLM experiments



3. **Multi-Model LLM Response Collection**# Create virtual environment│   ├── analyze_bias.py      # Analyze bias in results

   - Supports GPT-5, Claude 3 Opus (Syracuse Enterprise License), and Gemini 1.5 Pro

   - Interactive manual collection workflow (copy prompt → paste response)python3 -m venv .venv│   └── validate_claims.py   # Validate experimental claims

   - Multi-run capability for statistical robustness (3-10 responses per prompt recommended)

   - Dual logging format: CSV (quick analysis) and JSONL (detailed records)source .venv/bin/activate  # On Windows: .venv\Scripts\activate├── prompts/



4. **Comprehensive Bias Analysis**│   └── variants.json        # Generated prompt variants

   - **Sentiment Analysis**: Uses TextBlob to compute polarity (-1 to +1) and subjectivity (0 to 1)

   - **Statistical Testing**: Paired t-tests, chi-square tests, and Cohen's d effect sizes# Install dependencies├── results/

   - **Claim Validation**: Regex-based extraction and comparison against fixed ground truth

   - **Visualization**: Box plots, heatmaps, and distribution chartspip install -r requirements.txt│   ├── logs_csv/           # CSV format logs



5. **Professional Research Documentation**```│   ├── logs_jsonl/         # JSONL format logs

   - Full experimental design with IRB-ready methodology

   - Comprehensive research report with literature review, methods, and TBD results sections│   └── summaries/          # Result summaries

   - Reproducible analysis with pinned dependencies and fixed random seeds

### 2. Generate Prompt Variants├── .venv/                  # Virtual environment

## Repository Structure

├── requirements.txt

```

.```bash├── README.md

├── README.md                      # This file - comprehensive project guide

├── REPORT.md                      # 553-line research report (ready for submission)python src/experiment_design.py --csv data/results.csv --out prompts/variants.json└── REPORT.md

├── EXPERIMENTAL_DESIGN.md         # 251-line methodology documentation

├── COMPLETION_SUMMARY.md          # Project progress tracking``````

├── requirements.txt               # Pinned Python dependencies

│

├── data/

│   └── results.csv                # Kaggle dataset (International Football Results 1872-2017)### 3. Run Experiments## Setup

│

├── prompts/

│   └── variants.json              # Generated prompt pairs (H1A-H5B) with anonymized data

│```bash1. Create virtual environment:

├── results/

│   ├── logs_csv/                  # CSV logs for quick Excel/pandas analysis# Collect data for Claude 3 with 3 runs per prompt   ```bash

│   ├── logs_jsonl/                # JSONL logs for detailed structured data

│   ├── summaries/                 # JSON summaries and validation reportspython src/run_experiment.py --model Claude3 --runs 3 --model-version "claude-3-opus-20240229"   python3 -m venv .venv

│   │   └── claim_validation_report.json

│   └── analysis/                  # Generated visualizations and statistical outputs```   source .venv/bin/activate  # On macOS/Linux

│       └── README.md

│   ```

└── src/

    ├── experiment_design.py       # Generate prompts with fixed anonymized values**Process:** Copy each prompt to LLM web UI → Paste response → Repeat for all variants

    ├── run_experiment.py          # Interactive LLM response collection

    ├── analyze_bias.py            # Statistical analysis and visualization2. Install dependencies:

    └── validate_claims.py         # Extract and validate numerical claims

```### 4. Analyze Results   ```bash



## Getting Started   pip install -r requirements.txt



### Prerequisites```bash   ```



- **Python 3.10+** (tested on macOS ARM64 with Python 3.10)python src/analyze_bias.py

- **Virtual environment** recommended (avoids architecture conflicts on Apple Silicon)

- **LLM API access** for data collection:python src/validate_claims.py --csv data/results.csv --tolerance 0.5## Usage

  - OpenAI GPT-5 (requires API key)

  - Anthropic Claude 3 Opus via Syracuse Enterprise License (SU students/faculty)```

  - Google Gemini 1.5 Pro (requires API key)

1. Place your dataset in `data/results.csv`

### Installation

### 5. Review Report2. Run experiment design: `python src/experiment_design.py`

1. **Clone the repository**:

   ```bash3. Execute experiments: `python src/run_experiment.py`

   git clone <your-repo-url>

   cd Research_task08_Bias_detectionSee `REPORT.md` for full analysis and findings.4. Analyze results: `python src/analyze_bias.py`

   ```

5. Validate claims: `python src/validate_claims.py`

2. **Create and activate virtual environment**:

   ```bash## Repository Structure

   python3.10 -m venv .venv

   source .venv/bin/activate  # On macOS/Linux## Date Created

   # .venv\Scripts\activate    # On Windows

   ``````November 15, 2025



3. **Install dependencies**:├── README.md                   # This file

   ```bash├── REPORT.md                   # Final research report

   pip install --upgrade pip├── EXPERIMENTAL_DESIGN.md      # Hypothesis documentation

   pip install -r requirements.txt├── requirements.txt            # Dependencies

   ```├── data/

│   └── results.csv            # Source dataset

   **Key dependencies**:├── prompts/

   - `pandas==2.1.0` - Data manipulation and ground truth calculations│   └── variants.json          # Generated prompt pairs (H1A-H5B)

   - `scipy==1.11.4` - Statistical tests (t-test, chi-square, Cohen's d)├── src/

   - `textblob==0.17.1` - Sentiment analysis (polarity/subjectivity)│   ├── experiment_design.py   # Generates prompts

   - `matplotlib==3.8.0` - Visualization generation│   ├── run_experiment.py      # Collects LLM responses

   - `seaborn==0.13.0` - Advanced statistical plots│   ├── analyze_bias.py        # Statistical analysis

   - `python-dotenv==1.0.0` - Optional environment configuration│   └── validate_claims.py     # Ground truth validation

└── results/

4. **Verify installation**:    ├── logs_csv/              # Response logs (CSV)

   ```bash    ├── logs_jsonl/            # Response logs (JSONL)

   python -m py_compile src/*.py    ├── summaries/             # Analysis summaries

   # Should complete silently with no errors    └── analysis/              # Visualizations

   ``````



### Dataset Setup## Hypotheses Tested



The project uses the **International Football Results dataset** (1872-2017) from Kaggle. This dataset contains approximately 40,000 international football matches with detailed statistics.| ID | Bias Type | Manipulation | Example |

|----|-----------|--------------|---------|

1. **Download the dataset**:| **H1** | Framing Effect | Positive vs. negative tone | "growth potential" vs. "underperformed" |

   - Visit [Kaggle International Football Results](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)| **H2** | Anchoring Bias | Prestige cue | "Team A & D are powerhouses" |

   - Download `results.csv` (ensure it contains columns: `date`, `home_team`, `away_team`, `home_score`, `away_score`, `tournament`, `city`, `country`)| **H3** | Attribution Bias | Problem vs. solution | "what went wrong" vs. "opportunities" |

| **H4** | Selection Bias | Data scope | All matches vs. friendlies only |

2. **Place in project**:| **H5** | Definition Bias | Metric ambiguity | "dominance" vs. "consistency" |

   ```bash

   cp ~/Downloads/results.csv data/results.csv## Key Features

   ```

- **Anonymized Data:** Team A/B/C/D/E (no PII per assignment requirements)

3. **Verify dataset**:- **Fixed Values:** Reproducible results across all models

   ```bash- **Multi-Model Support:** Test Claude, GPT-4, Gemini

   python -c "import pandas as pd; df = pd.read_csv('data/results.csv'); print(f'Loaded {len(df)} matches')"- **Multiple Runs:** 3-5 runs per prompt for statistical power

   # Should print: Loaded ~40000 matches- **Statistical Tests:** t-tests, chi-square, Cohen's d effect sizes

   ```- **Sentiment Analysis:** TextBlob polarity + rule-based scoring

- **Ground Truth Validation:** Flags fabricated statistics

**Note**: The dataset is used only to compute anonymized aggregate statistics. Individual match details are not included in prompts. All team names are replaced with "Team A" through "Team E" to eliminate cultural bias.- **Visualizations:** Box plots, heatmaps, bar charts



## Running the Experiment## Dependencies



### Step 1: Generate Prompt Variants```

pandas==2.1.0

This script creates 10 prompt variants (2 per hypothesis) with the fixed anonymized dataset block:scipy==1.11.4

textblob==0.17.1

```bashmatplotlib==3.8.0

python src/experiment_design.pyseaborn==0.13.0

```numpy==1.26.4

python-dotenv==1.0.0

**What it does**:pyyaml==6.0.1

- Reads `data/results.csv` and computes aggregate statistics```

- Anonymizes top 5 teams as Team A-E with fixed win rates

- Generates `prompts/variants.json` containing:## Expected Outcomes

  - H1A/H1B: Framing (wins vs. losses)

  - H2A/H2B: Anchoring (high-to-low vs. low-to-high)**If models are bias-free:** H1A/H1B produce similar outputs  

  - H3A/H3B: Attribution (home advantage vs. balance)**If models exhibit bias:** Framing significantly affects sentiment (p < 0.05)

  - H4A/H4B: Selection (top 3 vs. bottom 2)

  - H5A/H5B: Metric (goals vs. percentages)## Common Issues



**Output**: `prompts/variants.json` (ready for manual copy-paste to LLMs)**`ModuleNotFoundError`:** Run `pip install -r requirements.txt`  

**`FileNotFoundError`:** Run `python src/experiment_design.py` first  

**Example snippet**:**Fabricated stats:** Run `validate_claims.py` to detect

```json

{## Extending the Project

  "dataset_block": "Team A - 63.5% | Team B - 59.2% | Team C - 58.7% | Team D - 57.8% | Team E - 55.1%",

  "variants": [- Test additional models (Llama, Mistral)

    {- Add new hypotheses (H6, H7)

      "prompt_id": "H1A_framing_wins",- Automate with API calls

      "dataset": "...",- Cross-model comparison analysis

      "question": "Summarize the key insights about these international football teams' performance..."

    }## Ethical Considerations

  ]

}- Data anonymized per assignment requirements

```- Limitations documented in `REPORT.md`

- Findings shared to improve LLM deployment practices

### Step 2: Collect LLM Responses

## Contact

This interactive script guides you through collecting responses from LLMs (GPT-5, Claude 3 Opus, Gemini 1.5 Pro):

**Author:** Aditya Deshmukh  

```bash**Email:** [your.email@syr.edu]

python src/run_experiment.py --model gpt-5 --model-version gpt-5-turbo-2024-10-01 --runs 5

```---



**Parameters**:**Last Updated:** November 15, 2025

- `--model`: LLM identifier (gpt-5 | claude-opus | gemini-pro)
- `--model-version`: Specific version string (e.g., "gpt-5-turbo-2024-10-01", "claude-3-opus-20240229")
- `--runs`: Number of responses per prompt (default: 3, recommended: 5-10 for statistical power)

**Workflow**:
1. Script displays a prompt from `variants.json`
2. You copy the prompt → paste into LLM interface → copy response
3. Paste response back into terminal
4. Script logs to both CSV and JSONL formats
5. Repeat for all 10 prompts × N runs

**Output**:
- `results/logs_csv/responses_YYYYMMDD_HHMMSS.csv` - Quick analysis format
- `results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl` - Detailed structured data

**Example log entry**:
```json
{
  "timestamp": "2024-12-15T14:32:10",
  "prompt_id": "H1A_framing_wins",
  "model": "gpt-5",
  "model_version": "gpt-5-turbo-2024-10-01",
  "response": "The data reveals Team A as the dominant force with a 63.5% win rate...",
  "sentiment": "positive",
  "run_number": 1
}
```

**Data Collection Goals**:
- Minimum: 30 total responses (10 prompts × 3 runs)
- Recommended: 50-90 responses (10 prompts × 5-9 runs) for statistical significance
- Multi-model: Collect from all 3 LLMs if resources permit (enables cross-model comparison)

### Step 3: Analyze Bias Patterns

This script performs comprehensive quantitative analysis on collected responses:

```bash
python src/analyze_bias.py results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl
```

**Analyses Performed**:

1. **Sentiment Analysis**:
   - Computes TextBlob polarity (-1 to +1) and subjectivity (0 to 1) for each response
   - Aggregates by hypothesis (H1-H5) and variant (A vs B)
   - Identifies systematic sentiment shifts between paired prompts

2. **Statistical Testing**:
   - **Paired t-tests**: Compare sentiment scores between A/B variants
   - **Chi-square tests**: Compare categorical sentiment distributions (positive/neutral/negative)
   - **Cohen's d effect sizes**: Quantify magnitude of bias (small: 0.2, medium: 0.5, large: 0.8)

3. **Claim Validation**:
   - Extracts numerical claims about Team A-E win rates
   - Compares against fixed ground truth (Team A: 63.5%, etc.)
   - Flags hallucinations or systematic over/under-estimations

4. **Visualization Generation** (requires real data):
   - Box plots: Sentiment distributions by hypothesis
   - Heatmaps: Cross-model bias patterns
   - Bar charts: Claim accuracy by team

**Output**:
- Console summary with hypothesis-level statistics
- `results/analysis/*.png` - Generated visualizations
- `results/summaries/analysis_report.json` - Machine-readable results

**Example console output**:
```
=== Hypothesis H1 (Framing) ===
H1A (Wins):     μ=0.42, σ=0.18, n=5
H1B (Losses):   μ=0.21, σ=0.14, n=5
Paired t-test:  t=3.21, p=0.008 **
Cohen's d:      1.28 (large effect)
Interpretation: Win framing produces significantly more positive sentiment
```

### Step 4: Validate Numerical Claims

This script extracts and validates specific numerical claims from LLM responses:

```bash
python src/validate_claims.py results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl
```

**What it does**:
- Uses regex patterns to extract claims like "Team A has a 63.5% win rate"
- Compares against fixed ground truth values
- Flags mismatches (hallucinations, rounding errors, or fabricated statistics)

**Ground Truth Reference**:
```python
{
    "Team A": 63.5,
    "Team B": 59.2,
    "Team C": 58.7,
    "Team D": 57.8,
    "Team E": 55.1
}
```

**Output**:
- `results/summaries/claim_validation_report.json`
- Console summary: "Found 45 claims, 3 mismatches (6.7% error rate)"

**Example validation**:
```json
{
  "claim": "Team A has a 63% win rate",
  "extracted_value": 63.0,
  "true_value": 63.5,
  "error": -0.5,
  "within_tolerance": true,
  "prompt_id": "H1A_framing_wins"
}
```

## Output Files Explained

### 1. CSV Logs (`results/logs_csv/`)
- **Format**: Excel-compatible comma-separated values
- **Use case**: Quick filtering, pivot tables, manual inspection
- **Columns**: `timestamp`, `prompt_id`, `model`, `model_version`, `response_text`, `sentiment_label`, `run_number`

### 2. JSONL Logs (`results/logs_jsonl/`)
- **Format**: JSON Lines (one JSON object per line)
- **Use case**: Structured analysis, easy to parse with Python/pandas
- **Fields**: Full metadata + response text + computed features

### 3. Summaries (`results/summaries/`)
- **claim_validation_report.json**: Numerical accuracy assessment
- **analysis_report.json**: Statistical test results (generated after analysis)
- **sentiment_by_hypothesis.json**: Aggregated sentiment scores

### 4. Visualizations (`results/analysis/`)
- Box plots: Sentiment distributions
- Heatmaps: Model × Hypothesis bias patterns
- Bar charts: Claim accuracy by team
- Scatter plots: Polarity vs. Subjectivity

## Ethical Considerations

This research follows strict ethical guidelines:

1. **No Human Subject Data**: Uses publicly available historical sports data only (Kaggle dataset). No personal information, no surveys, no identifiable participants.

2. **Anonymization**: All team names replaced with "Team A-E" to eliminate cultural bias and national stereotypes. No political or sensitive topics.

3. **Transparency**: Prompts and dataset blocks are identical except for tested variables. No deceptive practices. LLMs are prompted as data summarization tools, matching their real-world use case.

4. **Reproducibility**: Fixed random seeds, pinned dependencies, and version-controlled prompts ensure others can replicate findings.

5. **Bias Awareness**: Project explicitly aims to document potential biases to inform responsible LLM use—not to exploit them.

6. **IRB Status**: This research is considered **IRB-exempt** (no human subjects, publicly available data, computational analysis only). If publishing in journals requiring IRB review, Syracuse University's IRB should be consulted.

## Main Documents

### REPORT.md (553 lines)
**Comprehensive research report** structured as:
- **Title & Abstract**: Executive summary of research question and methods
- **Introduction**: Motivation, background on cognitive biases in humans and LLMs
- **Literature Review**: Prior work on framing effects, anchoring, and LLM biases
- **Hypotheses**: Five testable predictions (H1-H5) with justifications
- **Methodology**: Detailed experimental design, prompt construction, data collection protocol
- **Results**: [TBD - fill after data collection] Statistical findings, visualizations, hypothesis outcomes
- **Discussion**: [TBD] Interpretation, limitations, implications for LLM deployment
- **Conclusion**: [TBD] Key takeaways and future research directions
- **References**: Academic citations in APA format

**Status**: Ready for submission except "TBD" sections (requires actual data collection)

### EXPERIMENTAL_DESIGN.md (251 lines)
**Methodology documentation** covering:
- Research question and significance
- Hypothesis formulation with cognitive bias theory grounding
- Dataset selection and anonymization rationale
- Prompt engineering principles (minimal framing, identical data blocks)
- Data collection protocol (manual copy-paste workflow, logging format)
- Analysis plan (sentiment analysis, statistical tests, visualization strategy)
- Quality assurance (fixed ground truth, multi-run validation, syntax checking)
- Technical implementation (Python 3.10, pandas, scipy, textblob)
- Timeline and milestones (Oct 15, Nov 1, Nov 15 Qualtrics reports)
- Reproducibility checklist (requirements.txt, random seeds, version control)

**Status**: Complete and ready for IRB documentation if needed

### COMPLETION_SUMMARY.md
**Project progress tracker** with:
- Task completion checklist
- Known issues and debugging notes
- Next steps before Nov 15 deadline
- Qualtrics report submission reminders (Oct 15, Nov 1, Nov 15)

## Key Findings

**Note**: This section will be updated after data collection (30-90 LLM responses) is complete. Current state: **Experimental design validated, data collection in progress**.

### Expected Outcomes (Based on Human Cognitive Bias Literature)

1. **H1 (Framing)**: Win-framed prompts expected to produce more positive sentiment than loss-framed prompts, even though data is identical (predicted Cohen's d > 0.5).

2. **H2 (Anchoring)**: High-to-low ordering expected to anchor narratives on top teams, while low-to-high may emphasize competitive parity (predicted sentiment difference > 0.2).

3. **H3 (Attribution)**: Home advantage framing may lead to more cautious interpretations (lower confidence), while competitive balance framing may produce stronger claims.

4. **H4 (Selection)**: Prompts highlighting bottom 2 teams expected to produce more negative tone and emphasize struggle narratives.

5. **H5 (Metric)**: Goal-based analysis may focus on offensive prowess, while percentage-based may emphasize consistency and reliability.

### Actual Results: [TBD - Update After Data Collection]

**Data Collection Status**:
- [ ] 30 minimum responses collected (10 prompts × 3 runs)
- [ ] 50-90 recommended responses collected (10 prompts × 5-9 runs)
- [ ] Multi-model data (GPT-5, Claude 3 Opus, Gemini 1.5 Pro)

**Analysis Status**:
- [ ] Sentiment analysis completed (`analyze_bias.py`)
- [ ] Statistical tests run (t-tests, chi-square, effect sizes)
- [ ] Claim validation performed (`validate_claims.py`)
- [ ] Visualizations generated (box plots, heatmaps)
- [ ] Results integrated into REPORT.md

**Placeholder for Findings**:
```
[After running analyze_bias.py, summarize:]
- Which hypotheses were supported (p < 0.05)?
- Which had large effect sizes (Cohen's d > 0.8)?
- Were there unexpected patterns or null results?
- How did models differ (GPT-5 vs Claude vs Gemini)?
- What percentage of numerical claims were hallucinated?
```

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: python-dotenv**
   - **Fix**: `python-dotenv` is optional. If you see this error, it means the script tried to load a `.env` file but the module isn't installed. Either install it (`pip install python-dotenv`) or ignore—scripts work without it.

2. **Architecture mismatch on Apple Silicon Macs**
   - **Symptom**: `pandas` installed for x86_64 but you have ARM64
   - **Fix**: Always use a virtual environment (`python3.10 -m venv .venv`) instead of system Python to avoid architecture conflicts.

3. **scipy 1.11.0 yanked error**
   - **Fix**: The project uses `scipy==1.11.4` specifically (1.11.0 was removed due to licensing issues). Run `pip install --upgrade scipy==1.11.4`.

4. **Empty analysis output**
   - **Cause**: No data in JSONL file or file path incorrect
   - **Fix**: Verify JSONL file exists and contains valid JSON objects (one per line). Check file path in command.

5. **TextBlob download error**
   - **Symptom**: "Resource 'corpora/brown' not found"
   - **Fix**: Run `python -m textblob.download_corpora` to download required NLTK data.

### Validation Commands

```bash
# Check Python version
python --version  # Should be 3.10+

# Verify all dependencies installed
pip list | grep -E "pandas|scipy|textblob|matplotlib"

# Test all scripts compile
python -m py_compile src/*.py

# Validate dataset loaded correctly
python -c "import pandas as pd; print(pd.read_csv('data/results.csv').shape)"

# Check prompt generation works
python src/experiment_design.py && cat prompts/variants.json | head -n 20
```

## Timeline and Submission

**Key Deadlines** (IST 652 Fall 2025):
- **October 15, 2025**: Qualtrics Report #1 (Experimental Design)
- **November 1, 2025**: Qualtrics Report #2 (Progress Update)
- **November 15, 2025**: Final Qualtrics Report + GitHub Repository Link

**Current Status**: Experimental design complete, data collection in progress. All code validated and ready for use.

**Before Final Submission**:
1. Complete data collection (30-90 responses)
2. Run all analysis scripts (`analyze_bias.py`, `validate_claims.py`)
3. Generate visualizations (box plots, heatmaps)
4. Fill in "TBD" sections in REPORT.md with actual results
5. Update this README.md Key Findings section with concrete outcomes
6. Create COMPLETION_SUMMARY.md final version
7. Push to GitHub with clean commit history
8. Submit GitHub URL via Qualtrics form

## Citation

If you use this project in your research, please cite:

```
Deshmukh, A. (2025). Task 08: Bias Detection in LLM Data Narratives. 
Syracuse University, IST 652: Scripting for Data Analysis.
GitHub: <your-repo-url>
```

## License

This project is created for academic purposes as part of IST 652 coursework at Syracuse University. The International Football Results dataset is sourced from Kaggle and subject to its original license. Code and documentation are provided as-is for educational use.

## Contact

**Student**: Aditya Deshmukh  
**Course**: IST 652 - Scripting for Data Analysis  
**Institution**: Syracuse University  
**Semester**: Fall 2025

For questions about methodology or replication, please refer to EXPERIMENTAL_DESIGN.md or REPORT.md.

---

**Last Updated**: December 2024  
**Project Status**: Data Collection Phase  
**Documentation Version**: 2.0 (Comprehensive Rewrite)
