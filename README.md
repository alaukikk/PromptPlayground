# Prompt Technique Playground

## Setup (Windows + Anaconda)

```bash
conda create -n prompt_playground python=3.11 -y
conda activate prompt_playground
pip install -r requirements.txt
```

1. Copy `.env.example` to `.env`.
2. Put your Groq API key in `.env`.
3. Run `streamlit run app.py`.

## Features
- Four prompting strategies compared with the same Groq model.
- Five predefined benchmark tasks.
- Human ratings for accuracy, relevance, clarity and completeness.
- 5-task × 4-technique score matrix populated from saved ratings.
- Manually recorded unsupported/incorrect claim counts.
- Basic prompt-injection demonstration.
- Experimental image prompt variants and image rendering through a public endpoint.

## Important limitations
- Scores are human ratings, not objective ground truth.
- Hallucination counts must be checked against reliable references by the evaluator.
- Prompt injection demo is a simple educational test, not a security audit.
- The public image endpoint may be rate-limited, unavailable, or change its terms.
- A genuinely LoRA-fine-tuned model is not included in this quick-build package. Do not claim LoRA integration unless you train/load an adapter and demonstrate it.
