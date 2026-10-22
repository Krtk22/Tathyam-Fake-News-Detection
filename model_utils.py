
import re
from pathlib import Path

import torch
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

BASE_DIR = Path(__file__).resolve().parent

# New trained model directory
MODEL_PATH = BASE_DIR / "model" / "RoBERTa"

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# Load tokenizer from saved model folder
tokenizer = AutoTokenizer.from_pretrained(
    str(MODEL_PATH)
)

# Load trained RoBERTa model and safetensors weights
model = AutoModelForSequenceClassification.from_pretrained(
    str(MODEL_PATH),
    use_safetensors=True
)

model.to(DEVICE)
model.eval()

print("RoBERTa model loaded successfully!")
print("Running on:", DEVICE)



# Same preprocessing as our original notebook
def clean_title(text):
    text = str(text)
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def predict_news(headline):
    headline = clean_title(headline)

    if not headline:
        raise ValueError("Please enter a valid headline.")

    inputs = tokenizer(
        headline,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    inputs = {
        key: value.to(DEVICE)
        for key, value in inputs.items()
    }

    with torch.inference_mode():
        outputs = model(**inputs)
        probabilities = torch.softmax(
            outputs.logits, dim=-1
        )[0]

    predicted_class = int(
        torch.argmax(probabilities).item()
    )

    # Original dataset: 0 = Fake, 1 = Real
    label = "REAL" if predicted_class == 1 else "FAKE"

    confidence = float(
        probabilities[predicted_class].item() * 100
    )

    return {
        "prediction": label,
        "confidence": round(confidence, 2)
    }
