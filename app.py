from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# -----------------------------
# Load Models
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

logistic_model = joblib.load(
    os.path.join(MODEL_DIR, "logistic_regression_model.pkl")
)

random_forest_model = joblib.load(
    os.path.join(MODEL_DIR, "random_forest_model.pkl")
)

xgboost_model = joblib.load(
    os.path.join(MODEL_DIR, "xgboost_model.pkl")
)

scaler = joblib.load(
    os.path.join(MODEL_DIR, "scaler.pkl")
)


# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction
# -----------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        selected_model = request.form["model"]

        features = [
            float(request.form["Time"]),

            float(request.form["V1"]),
            float(request.form["V2"]),
            float(request.form["V3"]),
            float(request.form["V4"]),
            float(request.form["V5"]),
            float(request.form["V6"]),
            float(request.form["V7"]),
            float(request.form["V8"]),
            float(request.form["V9"]),
            float(request.form["V10"]),
            float(request.form["V11"]),
            float(request.form["V12"]),
            float(request.form["V13"]),
            float(request.form["V14"]),
            float(request.form["V15"]),
            float(request.form["V16"]),
            float(request.form["V17"]),
            float(request.form["V18"]),
            float(request.form["V19"]),
            float(request.form["V20"]),
            float(request.form["V21"]),
            float(request.form["V22"]),
            float(request.form["V23"]),
            float(request.form["V24"]),
            float(request.form["V25"]),
            float(request.form["V26"]),
            float(request.form["V27"]),
            float(request.form["V28"]),

            float(request.form["Amount"])
        ]

        data = np.array(features).reshape(1, -1)

        # Scale only Time and Amount
        data[0][0] = scaler.transform([[data[0][0], data[0][29]]])[0][0]
        data[0][29] = scaler.transform([[data[0][0], data[0][29]]])[0][1]

        # Select model
        if selected_model == "Logistic Regression":
            model = logistic_model

        elif selected_model == "Random Forest":
            model = random_forest_model

        else:
            model = xgboost_model

        # Prediction
        prediction = model.predict(data)[0]

        # Confidence
        confidence = None

        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(data)
            confidence = round(np.max(proba) * 100, 2)

        # Result
        if prediction == 1:
            result = "🚨 Fraudulent Transaction"
            color = "red"

        else:
            result = "✅ Legitimate Transaction"
            color = "green"

        return render_template(
            "index.html",
            prediction=result,
            confidence=confidence,
            selected_model=selected_model,
            color=color
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction="Error",
            confidence=None,
            selected_model="",
            color="red",
            error=str(e)
        )


# -----------------------------
# Run
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)