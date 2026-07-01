from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# load models
logistic_model = joblib.load("logistic_model.pkl")
rf_model = joblib.load("rf_model.pkl")
xgb_model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")


# column order
columns = [
'V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14',
'V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount'
]

@app.route('/')
def home():
    return render_template('index.html', form_data=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = []

        for col in columns:
            val = request.form.get(col)
            if val is None or val.strip() == "":
                return render_template('index.html',
                                       prediction=f"Error: {col} is empty",
                                       form_data=request.form)
            values.append(float(val))

        input_df = pd.DataFrame([values], columns=columns)
        scaled = scaler.transform(input_df)

        model_choice = request.form.get('model')

        if model_choice == "logistic":
            prediction = logistic_model.predict(scaled)[0]
            model_name = "Logistic Regression"

        elif model_choice == "rf":
            prediction = rf_model.predict(scaled)[0]
            model_name = "Random Forest"

        else:
            prediction = xgb_model.predict(scaled)[0]
            model_name = "XGBoost"

        if prediction == 1:
            result = f"⚠️ Fraud Transaction Detected by {model_name}"
        else:
            result = f"✅ Legitimate Transaction ({model_name})"

        return render_template('index.html',
                               prediction=result,
                               form_data=request.form)

    except Exception as e:
        print("ERROR:", e)
        return render_template('index.html',
                               prediction="Server Error — check terminal",
                               form_data=request.form)

if __name__ == "__main__":
    app.run(debug=True)
