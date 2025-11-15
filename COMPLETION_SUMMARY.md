***Summary of Work Completed***

Over the course of Task 08, I designed, implemented, and executed a complete, reproducible research pipeline to study how Large Language Models (LLMs) shift their interpretations of fixed numerical data under different prompt framings. The project followed the four required phases: Experimental Design, Data Collection, Bias Analysis, and Validation/Replication.

The workflow was fully supported by a Python-based toolkit that I built specifically for this assignment. All scripts are included in the repository (src/ folder), and every stage—from prompt generation to verification—was repeatable and logged.

The study used an anonymized dataset (Team A–E), derived from the international football results dataset (1872–2017). I designed a paired-prompt experiment to isolate framing bias, anchoring bias, confirmation bias, selection bias, and metric/definition drift across three models: GPT-5, Claude 3, and Gemini 1.5 Pro. Each model was given identical information and evaluated for narrative differences.
The results were clear: although all three models handled numbers accurately, their narratives shifted based on prompt wording. GPT-5 was the most susceptible to anchoring, Claude remained consistently neutral, and Gemini tended to refuse speculative analysis when data was missing. These patterns match known tendencies across these models and reinforce the overall conclusion that LLMs are sensitive to linguistic cues even when the underlying data remains unchanged.

**Skills Developed**

This project strengthened my skills in multiple areas:

*Experimental design:* Building controlled, paired-prompt studies for analyzing LLM behavior

*Python scripting:* Creating reusable tools to generate prompts, log responses, analyze outputs, and validate numerical claims
Data analysis: Applying sentiment scoring, keyword frequency tracking, anchoring detection, and interpretation of qualitative/quantitative trends

*Reproducible research:* Implementing a version-controlled, script-driven workflow for transparency and repeatability
Critical thinking about AI: Understanding where and how LLMs drift, hallucinate, or demonstrate inconsistent narrative behavior
Scientific writing: Producing detailed explanations, structured reports, and evidence-based conclusions

**Reflection**

Task 08 was one of the most practical projects I’ve completed in this course. Unlike typical machine learning assignments that focus on building models, this task required me to think critically about how models respond and what biases they may inherit from their training or prompt framing. It sharpened my understanding of LLM reliability and helped me appreciate the importance of reproducible code pipelines for bias detection.

The most interesting takeaway for me was how differently each model handles uncertainty. GPT-5 tends to fill gaps more confidently, Claude gravitates toward precision and restraint, and Gemini explicitly refuses unsupported claims. This makes me more cautious when using LLMs for analytical or decision-making tasks, especially where framing may unintentionally lead models toward biased outputs.
Overall, Task 08 taught me how essential it is to design careful experiments, validate claims rigorously, and interpret model output with a healthy balance of curiosity and skepticism.