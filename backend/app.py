from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model and vectorizer (update this path if needed)
model = joblib.load(
    r"C:\Users\Sahithi\OneDrive\Documents\scamscan\model\scam_model.pkl")
vectorizer = joblib.load(
    r"C:\Users\Sahithi\OneDrive\Documents\scamscan\model\vectorizer.pkl")


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
