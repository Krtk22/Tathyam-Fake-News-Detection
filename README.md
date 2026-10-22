# Tathyam — AI-Powered Fake News Detection

Tathyam is a final-year project exploring the use of deep learning to identify potentially misleading news headlines. The current repository contains a **Fake News Detection** prototype powered by a fine-tuned **RoBERTa** text classification model, with a **Flask** web interface.

> **Project status:** Fake News Detection prototype available. Deepfake Detection is planned for future integration and is **not yet included** in this repository.

## Features

- Enter a news headline through a simple web interface.
- Classify the headline as **REAL** or **FAKE** using RoBERTa.
- Display the model's softmax confidence score.
- Explore model training code and experiments in the `model_training/` directory.

**Important:** The output is a model prediction, **not a verified fact-check**. A high confidence score does not guarantee factual correctness. Predictions may be unreliable for headlines outside the training data's domain.

## Tech Stack

| Component | Technology |
| --- | --- |
| Model | RoBERTa (`roberta-base`, fine-tuned) |
| Deep learning | PyTorch, Hugging Face Transformers |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Training environment | Google Colab |

## Repository Structure

```text
Tathyam/
├── app.py
├── model_utils.py
├── model/
│   └── RoBERTa/
│       ├── config.json
│       ├── model.safetensors          # Download separately; not tracked by Git
│       ├── tokenizer.json
│       ├── tokenizer_config.json
│       ├── training_config.json
│       └── training_history.csv
├── model_training/
│   └── fake_news/
│       └── RoBERTa/
│           └── roberta_training.ipynb
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
├── .gitignore
└── README.md
```

*The tree illustrates the intended layout; some files may be added in later commits.*

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Tathyam.git
cd Tathyam
```

Replace `YOUR_USERNAME` with the actual repository owner.

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` has not yet been committed, the minimum application dependencies are `flask`, `torch`, `transformers`, and `safetensors`.

### 4. Add the trained checkpoint

Place the fine-tuned model files in `model/RoBERTa/`. The directory must contain at least the compatible `config.json`, `model.safetensors`, and tokenizer files.

**Model download:** _Link to be added._

The model weights are excluded from regular Git commits because of their size. Without the trained checkpoint, the app cannot make predictions. Do not substitute the original `roberta-base` weights for the fine-tuned classifier.

### 5. Start the app

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

## Model Training

The RoBERTa training notebook is located at:

```text
model_training/fake_news/RoBERTa/roberta_training.ipynb
```

The project uses the **FakeNewsNet** headline dataset for supervised training. The model takes headline text as input and predicts one of two classes:

- `0` — FAKE
- `1` — REAL

The inference implementation cleans text, tokenizes it, runs the model, and returns a predicted class and softmax score. For reproducibility, consult the training notebook for the exact preprocessing, data split, hyperparameters, and evaluation procedure.

## Evaluation and Limitations

The model should be evaluated on a held-out test set using metrics such as accuracy, precision, recall, F1-score, and a confusion matrix. **Verified test metrics will be added here once consolidated.**

Known limitations include:

- A text-only classifier cannot independently verify a claim against reliable sources.
- Performance may degrade on short factual statements, unfamiliar topics, or different geographic/news domains.
- The displayed softmax score is not necessarily a calibrated probability that a claim is true.
- Incorrect predictions are possible, even for well-known facts.

## Roadmap

- [x] Build a Flask-based Fake News Detection prototype
- [x] Integrate a fine-tuned RoBERTa classifier
- [x] Add a headline input and prediction interface
- [ ] Publish reproducible evaluation results and model download instructions
- [ ] Add training notebooks and comparisons for additional fake-news models
- [ ] Integrate the Deepfake Detection module
- [ ] Explore explainability techniques such as LIME

## Team and Contributions

Tathyam is a six-member final-year project. Individual model development, integration, evaluation, and documentation contributions will be recorded here as the relevant work is added to the repository.

## Disclaimer

Tathyam is an **academic research prototype**. Its predictions should not be used as the sole basis for judging the truth of news, making consequential decisions, or accusing anyone of spreading misinformation. Verify important claims against trustworthy primary sources.
