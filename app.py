
from flask import Flask, render_template, request, jsonify
from model_utils import predict_news

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    headline = data.get("headline", "")

    if not isinstance(headline, str) or not headline.strip():
        return jsonify({
            "error": "Please enter a news headline."
        }), 400

    try:
        result = predict_news(headline)
        return jsonify(result)

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({
            "error": "Model prediction failed."
        }), 500


if __name__ == "__main__":
    app.run(debug=False)
