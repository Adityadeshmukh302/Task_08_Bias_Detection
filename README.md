# Task 08: Bias Detection in LLM Data Narratives# Task 08: Bias Detection in LLM Data Narratives



**Author:** Aditya Deshmukh  

**Course:** IST 652 - Scripting for Data Analysis, Syracuse University  

**Submission Date:** November 15, 2025

---

---



## Overview

## Overview

This project investigates whether Large Language Models exhibit cognitive biases similar to humans when presented with identical data in different formats. Specifically, I test five types of cognitive biases (framing effects, anchoring bias, attribution bias, selection bias, and metric bias) using controlled experimental prompts with the International Football Results dataset from Kaggle.This research project investigates how subtle variations in data presentation can trigger cognitive biases in Large Language Models (LLMs), particularly when they interpret and summarize statistical information. Rather than testing explicit manipulation, we explore whether phenomena documented in human decision-making—such as **framing effects**, **anchoring bias**, **attribution bias**, **selection bias**, and **metric bias**—manifest in LLM-generated narratives about the same underlying dataset.**Author:** Aditya Deshmukh  ## Research Project Overview



The central research question is: **Do subtle variations in how data is presented cause LLMs to generate systematically different narratives, even when the underlying statistics are identical?**



This matters because LLMs are increasingly used to summarize complex datasets in journalism, business intelligence, education, and policy-making. If presentation differences lead to biased conclusions, users might receive misleading insights without realizing the source data was the same.This project investigates whether Large Language Models exhibit cognitive biases similar to humans when presented with identical data in different formats. Specifically, I test five types of cognitive biases—framing effects, anchoring bias, attribution bias, selection bias, and metric bias—using controlled experimental prompts with the International Football Results dataset from Kaggle.



---



## What This Project DoesThe central research question is: **Do subtle variations in how data is presented cause LLMs to generate systematically different narratives, even when the underlying statistics are identical?**The central question is: **Do LLMs exhibit systematic bias patterns when presented with identical data in different formats?** This matters because LLMs are increasingly used to summarize complex datasets in journalism, business intelligence, education, and policy contexts. If subtle presentation differences lead to systematically different interpretations, users may receive biased narratives without realizing the information source was identical.**Course:** Research Task 8 - Syracuse University  



### 1. Data Preparation and Anonymization



I use the International Football Results dataset (1872-2017) containing approximately 40,000 international matches from Kaggle. To eliminate cultural associations and potential confounds, I anonymize the top five teams as Team A through Team E.This matters because LLMs are increasingly used to summarize complex datasets in journalism, business intelligence, education, and policy-making. If presentation differences lead to biased conclusions, users might receive misleading insights without realizing the source data was the same.



The project establishes **fixed ground truth values** for reproducibility:

- Team A: 63.5% win rate

- Team B: 59.2% win rate  ---## What This Project Does**Submission Date:** November 15, 2025This project investigates bias detection in Large Language Model (LLM) data narratives.

- Team C: 58.7% win rate

- Team D: 57.8% win rate

- Team E: 55.1% win rate

- Average goals per match: 2.75## What This Project Does

- Home advantage: 0.49 goals



### 2. Hypothesis Testing with Paired Prompts

### 1. Data Preparation and Anonymization1. **Data Anonymization & Ground Truth Establishment**

I designed 10 experimental prompts organized into 5 paired hypotheses. Each hypothesis tests a specific cognitive bias by presenting identical data in two different ways:



| Hypothesis | Bias Type | Manipulation |

|------------|-----------|--------------|I use the International Football Results dataset (1872-2017) containing approximately 40,000 international matches from Kaggle. To eliminate cultural associations and potential confounds, I anonymize the top five teams as Team A through Team E.   - Uses the International Football Results dataset (1872-2017, ~40,000 matches from Kaggle)

| **H1** | Framing Effect | Win percentages vs. loss percentages |

| **H2** | Anchoring Bias | High-to-low vs. low-to-high team ordering |

| **H3** | Attribution Bias | Home advantage emphasis vs. competitive balance |

| **H4** | Selection Bias | Top 3 teams vs. bottom 2 teams prominence |The project establishes **fixed ground truth values** for reproducibility:   - Anonymizes country names to Team A through Team E to remove cultural associations## Overview## Project Structure

| **H5** | Metric Bias | Goal-based metrics vs. percentage-based metrics |

- Team A: 63.5% win rate

### 3. Multi-Model Response Collection

- Team B: 59.2% win rate     - Establishes **fixed ground truth values** for reproducibility:

The experiment supports three major LLM platforms:

- **GPT-5** (OpenAI)- Team C: 58.7% win rate

- **Claude 3 Opus** (Anthropic, via Syracuse Enterprise License)

- **Gemini 1.5 Pro** (Google)- Team D: 57.8% win rate     - Team A: 63.5% win rate



I use an interactive manual collection workflow where prompts are copied to each LLM's web interface and responses are pasted back for logging. The system supports multiple runs per prompt (recommended 3-10 runs) for statistical robustness.- Team E: 55.1% win rate



All responses are logged in two formats:- Average goals per match: 2.75     - Team B: 59.2% win rate

- **CSV logs** for quick Excel analysis

- **JSONL logs** for detailed structured analysis- Home advantage: 0.49 goals



### 4. Comprehensive Bias Analysis     - Team C: 58.7% win rateThis project systematically evaluates cognitive biases in Large Language Model (LLM) data narratives through controlled experimental manipulation. Using identical numerical datasets, we test whether prompt framing causes LLMs to generate systematically different conclusions.```



The analysis pipeline includes:### 2. Hypothesis Testing with Paired Prompts



**Sentiment Analysis**       - Team D: 57.8% win rate

Using TextBlob, I compute polarity scores (-1 to +1) and subjectivity scores (0 to 1) for each response.

I designed 10 experimental prompts organized into 5 paired hypotheses. Each hypothesis tests a specific cognitive bias by presenting identical data in two different ways:

**Statistical Testing**  

- Paired t-tests to compare sentiment between A/B variants     - Team E: 55.1% win rateResearch_task08_Bias_detection/

- Chi-square tests for categorical sentiment distributions

- Cohen's d effect sizes to quantify bias magnitude| Hypothesis | Bias Type | Manipulation |



**Claim Validation**  |------------|-----------|--------------|     - Average goals per match: 2.75

Using regex patterns, I extract numerical claims from LLM responses and compare them against fixed ground truth values to detect hallucinations or fabricated statistics.

| **H1** | Framing Effect | Win percentages vs. loss percentages |

**Visualization**  

The system generates box plots, heatmaps, and distribution charts to visualize bias patterns across models and hypotheses.| **H2** | Anchoring Bias | High-to-low vs. low-to-high team ordering |     - Home advantage: 0.49 goals## Quick Start├── data/



---| **H3** | Attribution Bias | Home advantage emphasis vs. competitive balance |



## Repository Structure| **H4** | Selection Bias | Top 3 teams vs. bottom 2 teams prominence |



```| **H5** | Metric Bias | Goal-based metrics vs. percentage-based metrics |

Research_task08_Bias_detection/

├── README.md                      # This file2. **Hypothesis Testing Through Paired Prompts**│   └── results.csv          # Input dataset (manually populated)

├── REPORT.md                      # Complete research report (553 lines)

├── EXPERIMENTAL_DESIGN.md         # Detailed methodology (251 lines)### 3. Multi-Model Response Collection

├── COMPLETION_SUMMARY.md          # Progress tracking

├── requirements.txt               # Python dependencies   - Tests 5 specific cognitive biases with 10 total prompts (2 variants per hypothesis)

│

├── data/The experiment supports three major LLM platforms:

│   └── results.csv               # Download from Kaggle (see Setup below)

│- **GPT-5** (OpenAI)   - **H1 (Framing)**: Win percentages vs. loss percentages### 1. Setup Environment├── src/

├── prompts/

│   └── variants.json             # Generated prompt pairs (H1A-H5B)- **Claude 3 Opus** (Anthropic, via Syracuse Enterprise License)

│

├── results/- **Gemini 1.5 Pro** (Google)   - **H2 (Anchoring)**: High-to-low vs. low-to-high team ordering

│   ├── logs_csv/                 # CSV format logs

│   ├── logs_jsonl/               # JSONL format logs  

│   ├── summaries/                # Validation reports

│   └── analysis/                 # Generated visualizationsI use an interactive manual collection workflow where prompts are copied to each LLM's web interface and responses are pasted back for logging. The system supports multiple runs per prompt (recommended 3-10 runs) for statistical robustness.   - **H3 (Attribution)**: Home advantage emphasis vs. competitive balance emphasis│   ├── experiment_design.py # Generate experimental prompts

│

└── src/

    ├── experiment_design.py      # Generate experimental prompts

    ├── run_experiment.py         # Collect LLM responsesAll responses are logged in two formats:   - **H4 (Selection)**: Top 3 teams vs. bottom 2 teams prominence

    ├── analyze_bias.py           # Statistical analysis

    └── validate_claims.py        # Validate numerical claims- **CSV logs** for quick Excel analysis

```

- **JSONL logs** for detailed structured analysis   - **H5 (Metric)**: Goal-based vs. percentage-based analysis```bash│   ├── run_experiment.py    # Execute LLM experiments

---



## Getting Started

### 4. Comprehensive Bias Analysis

### Prerequisites



- Python 3.10 or higher (tested on macOS ARM64)

- Virtual environment recommended to avoid dependency conflictsThe analysis pipeline includes:3. **Multi-Model LLM Response Collection**# Create virtual environment│   ├── analyze_bias.py      # Analyze bias in results

- Access to at least one LLM platform (GPT-5, Claude 3 Opus, or Gemini 1.5 Pro)



### Setup

**Sentiment Analysis**     - Supports GPT-5, Claude 3 Opus (Syracuse Enterprise License), and Gemini 1.5 Pro

**Step 1: Clone the repository**

Using TextBlob, I compute polarity scores (-1 to +1) and subjectivity scores (0 to 1) for each response.

```bash

git clone https://github.com/Adityadeshmukh302/Task_08_Bias_Detection.git   - Interactive manual collection workflow (copy prompt → paste response)python3 -m venv .venv│   └── validate_claims.py   # Validate experimental claims

cd Task_08_Bias_Detection

```**Statistical Testing**  



**Step 2: Create and activate a virtual environment**- Paired t-tests to compare sentiment between A/B variants   - Multi-run capability for statistical robustness (3-10 responses per prompt recommended)



```bash- Chi-square tests for categorical sentiment distributions

python3.10 -m venv .venv

source .venv/bin/activate  # On macOS/Linux- Cohen's d effect sizes to quantify bias magnitude   - Dual logging format: CSV (quick analysis) and JSONL (detailed records)source .venv/bin/activate  # On Windows: .venv\Scripts\activate├── prompts/

# On Windows: .venv\Scripts\activate

```



**Step 3: Install dependencies****Claim Validation**  



```bashUsing regex patterns, I extract numerical claims from LLM responses and compare them against fixed ground truth values to detect hallucinations or fabricated statistics.

pip install --upgrade pip

pip install -r requirements.txt4. **Comprehensive Bias Analysis**│   └── variants.json        # Generated prompt variants

```

**Visualization**  

The key dependencies include:

- pandas 2.1.0 (data manipulation)The system generates box plots, heatmaps, and distribution charts to visualize bias patterns across models and hypotheses.   - **Sentiment Analysis**: Uses TextBlob to compute polarity (-1 to +1) and subjectivity (0 to 1)

- scipy 1.11.4 (statistical tests)  

- textblob 0.17.1 (sentiment analysis)

- matplotlib 3.8.0 and seaborn 0.13.0 (visualizations)

---   - **Statistical Testing**: Paired t-tests, chi-square tests, and Cohen's d effect sizes# Install dependencies├── results/

**Step 4: Download the dataset**



Visit [Kaggle: International Football Results 1872-2017](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) and download `results.csv`. Place it in the `data/` directory:

## Repository Structure   - **Claim Validation**: Regex-based extraction and comparison against fixed ground truth

```bash

cp ~/Downloads/results.csv data/results.csv

```

```   - **Visualization**: Box plots, heatmaps, and distribution chartspip install -r requirements.txt│   ├── logs_csv/           # CSV format logs

Verify the dataset loaded correctly:

Research_task08_Bias_detection/

```bash

python -c "import pandas as pd; df = pd.read_csv('data/results.csv'); print(f'Loaded {len(df)} matches')"├── README.md                      # This file

```

├── REPORT.md                      # Complete research report (553 lines)

You should see: `Loaded ~40000 matches`

├── EXPERIMENTAL_DESIGN.md         # Detailed methodology (251 lines)5. **Professional Research Documentation**```│   ├── logs_jsonl/         # JSONL format logs

---

├── COMPLETION_SUMMARY.md          # Progress tracking

## Running the Experiment

├── requirements.txt               # Python dependencies   - Full experimental design with IRB-ready methodology

### Step 1: Generate Prompt Variants

│

Run the experiment design script to create all 10 prompt variants with anonymized data:

├── data/   - Comprehensive research report with literature review, methods, and TBD results sections│   └── summaries/          # Result summaries

```bash

python src/experiment_design.py│   └── results.csv               # Download from Kaggle (see Setup below)

```

│   - Reproducible analysis with pinned dependencies and fixed random seeds

This script:

- Reads the football results dataset├── prompts/

- Computes aggregate statistics for the top 5 teams

- Anonymizes team names as Team A through Team E│   └── variants.json             # Generated prompt pairs (H1A-H5B)### 2. Generate Prompt Variants├── .venv/                  # Virtual environment

- Generates `prompts/variants.json` with paired prompts for each hypothesis

│

**Output:** `prompts/variants.json` (ready for manual testing with LLMs)

├── results/## Repository Structure

### Step 2: Collect LLM Responses

│   ├── logs_csv/                 # CSV format logs

Run the interactive data collection script:

│   ├── logs_jsonl/               # JSONL format logs  ├── requirements.txt

```bash

python src/run_experiment.py --model claude-opus --model-version "claude-3-opus-20240229" --runs 5│   ├── summaries/                # Validation reports

```

│   └── analysis/                 # Generated visualizations```

**Parameters:**

- `--model`: Choose `gpt-5`, `claude-opus`, or `gemini-pro`│

- `--model-version`: Specify the exact model version (e.g., "gpt-5-turbo-2024-10-01")

- `--runs`: Number of times to collect responses for each prompt (recommended: 5-10)└── src/.```bash├── README.md



**Workflow:**    ├── experiment_design.py      # Generate experimental prompts

1. The script displays a prompt from `variants.json`

2. Copy the prompt and paste it into your LLM's web interface    ├── run_experiment.py         # Collect LLM responses├── README.md                      # This file - comprehensive project guide

3. Copy the LLM's response

4. Paste the response back into the terminal    ├── analyze_bias.py           # Statistical analysis

5. Repeat for all 10 prompts

    └── validate_claims.py        # Validate numerical claims├── REPORT.md                      # 553-line research report (ready for submission)python src/experiment_design.py --csv data/results.csv --out prompts/variants.json└── REPORT.md

The script automatically logs responses to:

- `results/logs_csv/responses_YYYYMMDD_HHMMSS.csv````

- `results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl`

├── EXPERIMENTAL_DESIGN.md         # 251-line methodology documentation

**Data Collection Goals:**

- Minimum: 30 responses (10 prompts × 3 runs)---

- Recommended: 50-90 responses (10 prompts × 5-9 runs) for statistical significance

- Ideal: Collect from multiple models to enable cross-model comparison├── COMPLETION_SUMMARY.md          # Project progress tracking``````



### Step 3: Analyze Bias Patterns## Getting Started



Run the statistical analysis on collected responses:├── requirements.txt               # Pinned Python dependencies



```bash### Prerequisites

python src/analyze_bias.py results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl

```│



This script performs:- Python 3.10 or higher (tested on macOS ARM64)



**Sentiment Analysis**  - Virtual environment recommended to avoid dependency conflicts├── data/

Computes TextBlob polarity and subjectivity scores, aggregated by hypothesis and variant.

- Access to at least one LLM platform (GPT-5, Claude 3 Opus, or Gemini 1.5 Pro)

**Statistical Testing**  

Runs paired t-tests, chi-square tests, and calculates Cohen's d effect sizes to quantify bias.│   └── results.csv                # Kaggle dataset (International Football Results 1872-2017)### 3. Run Experiments## Setup



**Visualization**  ### Setup

Generates box plots, heatmaps, and distribution charts saved to `results/analysis/`.

│

**Example Output:**

```**1. Clone the repository**

=== Hypothesis H1 (Framing) ===

H1A (Wins):     μ=0.42, σ=0.18, n=5├── prompts/

H1B (Losses):   μ=0.21, σ=0.14, n=5

Paired t-test:  t=3.21, p=0.008 **```bash

Cohen's d:      1.28 (large effect)

Interpretation: Win framing produces significantly more positive sentimentgit clone https://github.com/Adityadeshmukh302/Task_08_Bias_Detection.git│   └── variants.json              # Generated prompt pairs (H1A-H5B) with anonymized data

```

cd Task_08_Bias_Detection

### Step 4: Validate Numerical Claims

```│```bash1. Create virtual environment:

Extract and validate numerical claims from LLM responses:



```bash

python src/validate_claims.py results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl**2. Create and activate a virtual environment**├── results/

```



This script:

- Uses regex to extract numerical claims (e.g., "Team A has a 63.5% win rate")```bash│   ├── logs_csv/                  # CSV logs for quick Excel/pandas analysis# Collect data for Claude 3 with 3 runs per prompt   ```bash

- Compares extracted values against fixed ground truth

- Flags hallucinations and fabricated statisticspython3.10 -m venv .venv

- Generates `results/summaries/claim_validation_report.json`

source .venv/bin/activate  # On macOS/Linux│   ├── logs_jsonl/                # JSONL logs for detailed structured data

**Ground Truth Values:**

```python# On Windows: .venv\Scripts\activate

{

    "Team A": 63.5,```│   ├── summaries/                 # JSON summaries and validation reportspython src/run_experiment.py --model Claude3 --runs 3 --model-version "claude-3-opus-20240229"   python3 -m venv .venv

    "Team B": 59.2,

    "Team C": 58.7,

    "Team D": 57.8,

    "Team E": 55.1**3. Install dependencies**│   │   └── claim_validation_report.json

}

```



---```bash│   └── analysis/                  # Generated visualizations and statistical outputs```   source .venv/bin/activate  # On macOS/Linux



## Expected Outcomespip install --upgrade pip



Based on human cognitive bias literature, I expect:pip install -r requirements.txt│       └── README.md



**H1 (Framing):** Win-framed prompts will produce more positive sentiment than loss-framed prompts, even with identical data (predicted Cohen's d > 0.5).```



**H2 (Anchoring):** High-to-low ordering will anchor narratives on top teams, while low-to-high may emphasize competitive parity.│   ```



**H3 (Attribution):** Home advantage framing may lead to more cautious interpretations, while competitive balance framing may produce stronger claims.The key dependencies include:



**H4 (Selection):** Prompts highlighting bottom 2 teams will produce more negative tone and emphasize struggle narratives.- pandas 2.1.0 (data manipulation)└── src/



**H5 (Metric):** Goal-based analysis may focus on offensive prowess, while percentage-based may emphasize consistency.- scipy 1.11.4 (statistical tests)  



The actual results will be added to this README and the full REPORT.md after completing data collection and analysis.- textblob 0.17.1 (sentiment analysis)    ├── experiment_design.py       # Generate prompts with fixed anonymized values**Process:** Copy each prompt to LLM web UI → Paste response → Repeat for all variants



---- matplotlib 3.8.0 and seaborn 0.13.0 (visualizations)



## Deliverables    ├── run_experiment.py          # Interactive LLM response collection



### Code Scripts (All Located in `src/`)**4. Download the dataset**

- `experiment_design.py` - Generates all prompt variations

- `run_experiment.py` - Executes LLM queries and logs responses      ├── analyze_bias.py            # Statistical analysis and visualization2. Install dependencies:

- `analyze_bias.py` - Quantitative analysis of outputs

- `validate_claims.py` - Checks LLM statements against ground truthVisit [Kaggle: International Football Results 1872-2017](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) and download `results.csv`. Place it in the `data/` directory:



### Documentation    └── validate_claims.py         # Extract and validate numerical claims

- `prompts/` - Directory with all prompt templates and variations

- `results/` - All raw LLM responses (large files not committed to git)```bash

- `results/analysis/` - Statistical tests, visualizations, summary tables

- `REPORT.md` - Final bias detection report (553 lines)cp ~/Downloads/results.csv data/results.csv```### 4. Analyze Results   ```bash

- `EXPERIMENTAL_DESIGN.md` - Detailed methodology (251 lines)

- `README.md` - This file explaining how to reproduce experiments```



---



## Ethical ConsiderationsVerify the dataset loaded correctly:



This research follows strict ethical guidelines:## Getting Started   pip install -r requirements.txt



1. **No Human Subjects:** Uses only publicly available historical sports data from Kaggle. No personal information, surveys, or identifiable participants.```bash



2. **Data Anonymization:** All team names replaced with "Team A-E" to eliminate cultural bias and national stereotypes.python -c "import pandas as pd; df = pd.read_csv('data/results.csv'); print(f'Loaded {len(df)} matches')"



3. **Transparency:** Prompts are identical except for tested variables. No deceptive practices.```



4. **Reproducibility:** Fixed random seeds, pinned dependencies, and version-controlled prompts ensure replicability.### Prerequisites```bash   ```



5. **Responsible AI:** The project aims to document potential biases to inform responsible LLM deployment, not to exploit weaknesses.You should see: `Loaded ~40000 matches`



6. **IRB Status:** This research is considered IRB-exempt (no human subjects, publicly available data only). For journal publication, Syracuse University's IRB should be consulted.



------



## Troubleshooting- **Python 3.10+** (tested on macOS ARM64 with Python 3.10)python src/analyze_bias.py



### Common Issues and Solutions## Running the Experiment



**ModuleNotFoundError: python-dotenv**  - **Virtual environment** recommended (avoids architecture conflicts on Apple Silicon)

The `python-dotenv` module is optional. Either install it (`pip install python-dotenv`) or ignore the error—scripts work without it.

### Step 1: Generate Prompt Variants

**Architecture mismatch on Apple Silicon Macs**  

Always use a virtual environment (`python3.10 -m venv .venv`) instead of system Python to avoid x86_64 vs ARM64 conflicts.- **LLM API access** for data collection:python src/validate_claims.py --csv data/results.csv --tolerance 0.5## Usage



**scipy 1.11.0 yanked error**  Run the experiment design script to create all 10 prompt variants with anonymized data:

The project uses `scipy==1.11.4` specifically. Run `pip install --upgrade scipy==1.11.4` if needed.

  - OpenAI GPT-5 (requires API key)

**Empty analysis output**  

Verify the JSONL file exists and contains valid JSON objects (one per line). Check the file path in your command.```bash



**TextBlob corpora not found**  python src/experiment_design.py  - Anthropic Claude 3 Opus via Syracuse Enterprise License (SU students/faculty)```

Run `python -m textblob.download_corpora` to download required NLTK data.

```

### Validation Commands

  - Google Gemini 1.5 Pro (requires API key)

```bash

# Check Python versionThis script:

python --version  # Should be 3.10+

- Reads the football results dataset1. Place your dataset in `data/results.csv`

# Verify all dependencies installed

pip list | grep -E "pandas|scipy|textblob|matplotlib"- Computes aggregate statistics for the top 5 teams



# Test all scripts compile without errors- Anonymizes team names as Team A through Team E### Installation

python -m py_compile src/*.py

- Generates `prompts/variants.json` with paired prompts for each hypothesis

# Validate dataset loads correctly

python -c "import pandas as pd; print(pd.read_csv('data/results.csv').shape)"### 5. Review Report2. Run experiment design: `python src/experiment_design.py`



# Check prompt generation works**Output:** `prompts/variants.json` (ready for manual testing with LLMs)

python src/experiment_design.py && cat prompts/variants.json | head -n 20

```1. **Clone the repository**:



---### Step 2: Collect LLM Responses



## Project Timeline   ```bash3. Execute experiments: `python src/run_experiment.py`



**Key Deadlines (IST 652 Fall 2025):**Run the interactive data collection script:

- October 15, 2025: Qualtrics Report #1 (Experimental Design)

- November 1, 2025: Qualtrics Report #2 (Progress Update)     git clone <your-repo-url>

- November 15, 2025: Final Qualtrics Report + GitHub Repository Link

```bash

**Current Status:** Experimental design complete, data collection in progress

python src/run_experiment.py --model claude-opus --model-version "claude-3-opus-20240229" --runs 5   cd Research_task08_Bias_detectionSee `REPORT.md` for full analysis and findings.4. Analyze results: `python src/analyze_bias.py`

---

```

## Key Documents

   ```

**REPORT.md (553 lines)**  

Comprehensive research report with introduction, literature review, hypotheses, methodology, results (TBD), discussion (TBD), and references. Ready for submission after data collection.**Parameters:**



**EXPERIMENTAL_DESIGN.md (251 lines)**  - `--model`: Choose `gpt-5`, `claude-opus`, or `gemini-pro`5. Validate claims: `python src/validate_claims.py`

Detailed methodology documentation covering research questions, hypothesis formulation, dataset selection, prompt engineering, data collection protocol, analysis plan, and reproducibility checklist.

- `--model-version`: Specify the exact model version (e.g., "gpt-5-turbo-2024-10-01")

**COMPLETION_SUMMARY.md**  

Project progress tracker with task completion checklist, known issues, and next steps.- `--runs`: Number of times to collect responses for each prompt (recommended: 5-10)2. **Create and activate virtual environment**:



---



## Contact**Workflow:**   ```bash## Repository Structure



**Aditya Deshmukh**  1. The script displays a prompt from `variants.json`

Syracuse University, School of Information Studies  

IST 652 - Scripting for Data Analysis, Fall 20252. Copy the prompt and paste it into your LLM's web interface   python3.10 -m venv .venv



GitHub Repository: [https://github.com/Adityadeshmukh302/Task_08_Bias_Detection](https://github.com/Adityadeshmukh302/Task_08_Bias_Detection)3. Copy the LLM's response



---4. Paste the response back into the terminal   source .venv/bin/activate  # On macOS/Linux## Date Created



**Last Updated:** November 15, 20255. Repeat for all 10 prompts


   # .venv\Scripts\activate    # On Windows

The script automatically logs responses to:

- `results/logs_csv/responses_YYYYMMDD_HHMMSS.csv`   ``````November 15, 2025

- `results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl`



**Data Collection Goals:**

- Minimum: 30 responses (10 prompts × 3 runs)3. **Install dependencies**:├── README.md                   # This file

- Recommended: 50-90 responses (10 prompts × 5-9 runs) for statistical significance

- Ideal: Collect from multiple models to enable cross-model comparison   ```bash├── REPORT.md                   # Final research report



### Step 3: Analyze Bias Patterns   pip install --upgrade pip├── EXPERIMENTAL_DESIGN.md      # Hypothesis documentation



Run the statistical analysis on collected responses:   pip install -r requirements.txt├── requirements.txt            # Dependencies



```bash   ```├── data/

python src/analyze_bias.py results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl

```│   └── results.csv            # Source dataset



This script performs:   **Key dependencies**:├── prompts/



**Sentiment Analysis**     - `pandas==2.1.0` - Data manipulation and ground truth calculations│   └── variants.json          # Generated prompt pairs (H1A-H5B)

Computes TextBlob polarity and subjectivity scores, aggregated by hypothesis and variant.

   - `scipy==1.11.4` - Statistical tests (t-test, chi-square, Cohen's d)├── src/

**Statistical Testing**  

Runs paired t-tests, chi-square tests, and calculates Cohen's d effect sizes to quantify bias.   - `textblob==0.17.1` - Sentiment analysis (polarity/subjectivity)│   ├── experiment_design.py   # Generates prompts



**Visualization**     - `matplotlib==3.8.0` - Visualization generation│   ├── run_experiment.py      # Collects LLM responses

Generates box plots, heatmaps, and distribution charts saved to `results/analysis/`.

   - `seaborn==0.13.0` - Advanced statistical plots│   ├── analyze_bias.py        # Statistical analysis

**Example Output:**

```   - `python-dotenv==1.0.0` - Optional environment configuration│   └── validate_claims.py     # Ground truth validation

=== Hypothesis H1 (Framing) ===

H1A (Wins):     μ=0.42, σ=0.18, n=5└── results/

H1B (Losses):   μ=0.21, σ=0.14, n=5

Paired t-test:  t=3.21, p=0.008 **4. **Verify installation**:    ├── logs_csv/              # Response logs (CSV)

Cohen's d:      1.28 (large effect)

Interpretation: Win framing produces significantly more positive sentiment   ```bash    ├── logs_jsonl/            # Response logs (JSONL)

```

   python -m py_compile src/*.py    ├── summaries/             # Analysis summaries

### Step 4: Validate Numerical Claims

   # Should complete silently with no errors    └── analysis/              # Visualizations

Extract and validate numerical claims from LLM responses:

   ``````

```bash

python src/validate_claims.py results/logs_jsonl/responses_YYYYMMDD_HHMMSS.jsonl

```# Hypotheses Tested



This script:| **H1** | Framing Effect | Positive vs. negative tone | "growth potential" vs. "underperformed" |

- Uses regex to extract numerical claims (e.g., "Team A has a 63.5% win rate")| **H2** | Anchoring Bias | Prestige cue | "Team A & D are powerhouses" |

- Compares extracted values against fixed ground truth| **H3** | Attribution Bias | Problem vs. solution | "what went wrong" vs. "opportunities" |

- Flags hallucinations and fabricated statistics| **H4** | Selection Bias | Data scope | All matches vs. friendlies only |

- Generates `results/summaries/claim_validation_report.json`| **H5** | Definition Bias | Metric ambiguity | "dominance" vs. "consistency" |



**Ground Truth Values:**### Dataset Setup

```python

{The project uses the **International Football Results dataset** (1872-2017) from Kaggle. This dataset contains approximately 40,000 international football matches with detailed statistics.| ID | Bias Type | Manipulation | Example |

    "Team A": 63.5,

    "Team B": 59.2,|----|-----------|--------------|---------|

    "Team C": 58.7,

    "Team D": 57.8,1. **Download the dataset**:

    "Team E": 55.1

}   - Visit [Kaggle International Football Results](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)

```

   - Download `results.csv` (ensure it contains columns: `date`, `home_team`, `away_team`, `home_score`, `away_score`, `tournament`, `city`, `country`)

---



## Expected Outcomes2. **Place in project**:



Based on human cognitive bias literature, I expect:   ```bash



**H1 (Framing):** Win-framed prompts will produce more positive sentiment than loss-framed prompts, even with identical data (predicted Cohen's d > 0.5).   cp ~/Downloads/results.csv data/results.csv## Key Features



**H2 (Anchoring):** High-to-low ordering will anchor narratives on top teams, while low-to-high may emphasize competitive parity.   ```



**H3 (Attribution):** Home advantage framing may lead to more cautious interpretations, while competitive balance framing may produce stronger claims.- **Anonymized Data:** Team A/B/C/D/E (no PII per assignment requirements)



**H4 (Selection):** Prompts highlighting bottom 2 teams will produce more negative tone and emphasize struggle narratives.3. **Verify dataset**:- **Fixed Values:** Reproducible results across all models



**H5 (Metric):** Goal-based analysis may focus on offensive prowess, while percentage-based may emphasize consistency.   ```bash- **Multi-Model Support:** Test Claude, GPT-4, Gemini



The actual results will be added to this README and the full REPORT.md after completing data collection and analysis.   python -c "import pandas as pd; df = pd.read_csv('data/results.csv'); print(f'Loaded {len(df)} matches')"- **Multiple Runs:** 3-5 runs per prompt for statistical power



---   # Should print: Loaded ~40000 matches- **Statistical Tests:** t-tests, chi-square, Cohen's d effect sizes



## Deliverables   ```- **Sentiment Analysis:** TextBlob polarity + rule-based scoring



### Code Scripts (All Located in `src/`)- **Ground Truth Validation:** Flags fabricated statistics

- `experiment_design.py` - Generates all prompt variations

- `run_experiment.py` - Executes LLM queries and logs responses  **Note**: The dataset is used only to compute anonymized aggregate statistics. Individual match details are not included in prompts. All team names are replaced with "Team A" through "Team E" to eliminate cultural bias.- **Visualizations:** Box plots, heatmaps, bar charts

- `analyze_bias.py` - Quantitative analysis of outputs

- `validate_claims.py` - Checks LLM statements against ground truth



### Documentation## Running the Experiment## Dependencies

- `prompts/` - Directory with all prompt templates and variations

- `results/` - All raw LLM responses (large files not committed to git)

- `results/analysis/` - Statistical tests, visualizations, summary tables

- `REPORT.md` - Final bias detection report (553 lines)### Step 1: Generate Prompt Variants```

- `EXPERIMENTAL_DESIGN.md` - Detailed methodology (251 lines)

- `README.md` - This file explaining how to reproduce experimentspandas==2.1.0



---This script creates 10 prompt variants (2 per hypothesis) with the fixed anonymized dataset block:scipy==1.11.4



## Ethical Considerationstextblob==0.17.1



This research follows strict ethical guidelines:```bashmatplotlib==3.8.0



1. **No Human Subjects:** Uses only publicly available historical sports data from Kaggle. No personal information, surveys, or identifiable participants.python src/experiment_design.pyseaborn==0.13.0



2. **Data Anonymization:** All team names replaced with "Team A-E" to eliminate cultural bias and national stereotypes.```numpy==1.26.4



3. **Transparency:** Prompts are identical except for tested variables. No deceptive practices.python-dotenv==1.0.0



4. **Reproducibility:** Fixed random seeds, pinned dependencies, and version-controlled prompts ensure replicability.**What it does**:pyyaml==6.0.1



5. **Responsible AI:** The project aims to document potential biases to inform responsible LLM deployment, not to exploit weaknesses.- Reads `data/results.csv` and computes aggregate statistics```



6. **IRB Status:** This research is considered IRB-exempt (no human subjects, publicly available data only). For journal publication, Syracuse University's IRB should be consulted.- Anonymizes top 5 teams as Team A-E with fixed win rates



---- Generates `prompts/variants.json` containing:## Expected Outcomes



## Troubleshooting  - H1A/H1B: Framing (wins vs. losses)



### Common Issues and Solutions  - H2A/H2B: Anchoring (high-to-low vs. low-to-high)**If models are bias-free:** H1A/H1B produce similar outputs  



**ModuleNotFoundError: python-dotenv**    - H3A/H3B: Attribution (home advantage vs. balance)**If models exhibit bias:** Framing significantly affects sentiment (p < 0.05)

The `python-dotenv` module is optional. Either install it (`pip install python-dotenv`) or ignore the error—scripts work without it.

  - H4A/H4B: Selection (top 3 vs. bottom 2)

**Architecture mismatch on Apple Silicon Macs**  

Always use a virtual environment (`python3.10 -m venv .venv`) instead of system Python to avoid x86_64 vs ARM64 conflicts.  - H5A/H5B: Metric (goals vs. percentages)## Common Issues



**scipy 1.11.0 yanked error**  

The project uses `scipy==1.11.4` specifically. Run `pip install --upgrade scipy==1.11.4` if needed.

**Output**: `prompts/variants.json` (ready for manual copy-paste to LLMs)**`ModuleNotFoundError`:** Run `pip install -r requirements.txt`  

**Empty analysis output**  

Verify the JSONL file exists and contains valid JSON objects (one per line). Check the file path in your command.**`FileNotFoundError`:** Run `python src/experiment_design.py` first  



**TextBlob corpora not found**  **Example snippet**:**Fabricated stats:** Run `validate_claims.py` to detect

Run `python -m textblob.download_corpora` to download required NLTK data.

```json

### Validation Commands

{## Extending the Project

```bash

# Check Python version  "dataset_block": "Team A - 63.5% | Team B - 59.2% | Team C - 58.7% | Team D - 57.8% | Team E - 55.1%",

python --version  # Should be 3.10+

  "variants": [- Test additional models (Llama, Mistral)

# Verify all dependencies installed

pip list | grep -E "pandas|scipy|textblob|matplotlib"    {- Add new hypotheses (H6, H7)



# Test all scripts compile without errors      "prompt_id": "H1A_framing_wins",- Automate with API calls

python -m py_compile src/*.py

      "dataset": "...",- Cross-model comparison analysis

# Validate dataset loads correctly

python -c "import pandas as pd; print(pd.read_csv('data/results.csv').shape)"      "question": "Summarize the key insights about these international football teams' performance..."



# Check prompt generation works    }## Ethical Considerations

python src/experiment_design.py && cat prompts/variants.json | head -n 20

```  ]



---}- Data anonymized per assignment requirements



## Project Timeline```- Limitations documented in `REPORT.md`



**Key Deadlines (IST 652 Fall 2025):**- Findings shared to improve LLM deployment practices

- October 15, 2025: Qualtrics Report #1 (Experimental Design)

- November 1, 2025: Qualtrics Report #2 (Progress Update)  ### Step 2: Collect LLM Responses

- November 15, 2025: Final Qualtrics Report + GitHub Repository Link

## Contact

**Current Status:** Experimental design complete, data collection in progress

This interactive script guides you through collecting responses from LLMs (GPT-5, Claude 3 Opus, Gemini 1.5 Pro):

---

**Author:** Aditya Deshmukh  

## Key Documents

```bash**Email:** [your.email@syr.edu]

**REPORT.md (553 lines)**  

Comprehensive research report with introduction, literature review, hypotheses, methodology, results (TBD), discussion (TBD), and references. Ready for submission after data collection.python src/run_experiment.py --model gpt-5 --model-version gpt-5-turbo-2024-10-01 --runs 5



**EXPERIMENTAL_DESIGN.md (251 lines)**  ```---

Detailed methodology documentation covering research questions, hypothesis formulation, dataset selection, prompt engineering, data collection protocol, analysis plan, and reproducibility checklist.



**COMPLETION_SUMMARY.md**  

Project progress tracker with task completion checklist, known issues, and next steps.**Parameters**:**Last Updated:** November 15, 2025



---- `--model`: LLM identifier (gpt-5 | claude-opus | gemini-pro)

- `--model-version`: Specific version string (e.g., "gpt-5-turbo-2024-10-01", "claude-3-opus-20240229")

## Contact- `--runs`: Number of responses per prompt (default: 3, recommended: 5-10 for statistical power)



**Aditya Deshmukh**  **Workflow**:

Syracuse University, School of Information Studies  1. Script displays a prompt from `variants.json`

IST 652 - Scripting for Data Analysis, Fall 20252. You copy the prompt → paste into LLM interface → copy response

3. Paste response back into terminal

GitHub Repository: [https://github.com/Adityadeshmukh302/Task_08_Bias_Detection](https://github.com/Adityadeshmukh302/Task_08_Bias_Detection)4. Script logs to both CSV and JSONL formats

5. Repeat for all 10 prompts × N runs

---

**Output**:

**Last Updated:** November 15, 2025- `results/logs_csv/responses_YYYYMMDD_HHMMSS.csv` - Quick analysis format

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


