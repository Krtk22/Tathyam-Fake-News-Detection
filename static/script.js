
async function verifyNews() {
    const headline = document.getElementById("headline").value.trim();
    const button = document.getElementById("verifyBtn");
    const result = document.getElementById("result");
    const prediction = document.getElementById("prediction");
    const confidence = document.getElementById("confidence");
    const confidenceBar = document.getElementById("confidenceBar");
    const resultMessage = document.getElementById("resultMessage");

    if (!headline) {
        alert("Please enter a news headline first.");
        return;
    }

    button.disabled = true;
    button.textContent = "Analyzing...";
    result.classList.remove("hidden");

    prediction.textContent = "Processing...";
    confidence.textContent = "";
    resultMessage.textContent = "";
    confidenceBar.style.width = "0%";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ headline: headline })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.message || data.error || "Prediction unavailable"
            );
        }

        const score = Number(data.confidence);

        if (!Number.isFinite(score) || score < 0 || score > 100) {
            throw new Error("Invalid model confidence returned.");
        }

        prediction.textContent = data.prediction;
        confidence.textContent = `Model confidence: ${score.toFixed(2)}%`;
        confidenceBar.style.width = `${score}%`;

        resultMessage.textContent =
            "This is an AI classification, not independent fact-checking.";

    } catch (error) {
        prediction.textContent = "Analysis unavailable";
        confidence.textContent = "";
        resultMessage.textContent = error.message;
    } finally {
        button.disabled = false;
        button.textContent = "Analyze Headline →";
    }
}
