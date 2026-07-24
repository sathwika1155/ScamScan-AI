from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Get the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model and vectorizer
model = joblib.load(os.path.join(BASE_DIR, "model", "scam_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "model", "vectorizer.pkl"))


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    prob = model.predict_proba(text_vec)[0][prediction]

    return jsonify({
        "prediction": "Scam" if prediction == 1 else "Not Scam",
        "confidence": round(prob * 100, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)
