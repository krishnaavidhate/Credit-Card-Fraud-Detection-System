# Credit-Card-Fraud-Detection-System
💳 Credit Card Fraud Detection System

A machine learning web application that detects fraudulent credit card transactions in real time using multiple classification models, with an interactive Flask-based interface for testing predictions.


📌 Overview

Credit card fraud costs billions of dollars annually, and fraudulent transactions make up a tiny fraction of all transactions — making detection a classic imbalanced classification problem. This project builds and compares three machine learning models to classify transactions as legitimate or fraudulent, then deploys the best-performing pipeline behind a simple web interface where users can input transaction features and get an instant prediction.


✨ Features


🔍 Real-time fraud prediction through a web form
🤖 Choice of three trained models: Logistic Regression, Random Forest, and XGBoost
⚖️ Feature scaling pipeline using a pre-fitted StandardScaler
🧪 One-click "Load Legit Example" / "Load Fraud Example" buttons to quickly test the app
📓 Full exploratory data analysis and model training notebook included
🌐 Deployable to any Python-hosting platform (Render, Railway, PythonAnywhere)



🧠 Models Used

ModelDescriptionLogistic RegressionBaseline linear classifier, fast and interpretableRandom ForestEnsemble of decision trees, handles non-linearity wellXGBoostGradient-boosted trees, typically highest performance on tabular data

All models were trained on the same preprocessed, scaled feature set and can be compared directly from the app's model dropdown.


📊 Dataset

This project uses the Credit Card Fraud Detection dataset from Kaggle.


284,807 transactions made by European cardholders in September 2013
492 frauds (~0.17% of all transactions) — highly imbalanced
Features V1–V28 are PCA-transformed components (original features anonymized for confidentiality)
Amount is the transaction amount
Class is the target: 1 = fraud, 0 = legitimate



⚠️ The raw CSV (~145 MB) is not included in this repository due to GitHub's file size limits. Download it directly from Kaggle using the link above and place it in the data/ folder if you want to re-run the notebook.




🗂️ Project Structure

credit-card-fraud-detection/
├── app.py                     # Flask application
├── templates/
│   └── index.html             # Web UI
├── models/
│   ├── logistic_model.pkl
│   ├── rf_model.pkl
│   ├── xgb_model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── credit_card.ipynb      # EDA + model training + evaluation
├── data/
│   └── creditcard.csv         # (not tracked — see Dataset section)
├── requirements.txt
├── .gitignore
└── README.md


⚙️ Installation & Setup


Clone the repository


bash   git clone https://github.com/YOUR_USERNAME/credit-card-fraud-detection.git
   cd credit-card-fraud-detection


Create a virtual environment (recommended)


bash   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate


Install dependencies


bash   pip install -r requirements.txt


Run the app


bash   python app.py


Open your browser at http://127.0.0.1:5000



🚀 Usage


Enter the 28 PCA features (V1–V28) and the transaction Amount, or click "Load Legit Example" / "Load Fraud Example" to autofill sample values.
Select a model from the dropdown (Logistic Regression, Random Forest, or XGBoost).
Click Predict Transaction to see the result.



🌐 Live Demo

🔗 Live App (add your deployed link here, e.g. Render/Railway URL)


Deployed on Render — note the free tier may take 30–60 seconds to spin up after inactivity.




🛠️ Tech Stack


Python — core language
scikit-learn — Logistic Regression, Random Forest, preprocessing
XGBoost — gradient boosting model
Pandas / NumPy — data manipulation
Flask — web application framework
Jinja2 — HTML templating
Joblib — model serialization



📈 Future Improvements


Add SHAP-based explainability to show why a transaction was flagged
Display model precision/recall/F1 comparison directly in the UI
Add a REST API endpoint (/predict-api) returning JSON for programmatic access
Add input validation and better error handling on the frontend
Containerize with Docker for easier deployment



👤 Author

Krishna
Third-year B.Tech student, Artificial Intelligence and Data Science
SNJB College of Engineering


📄 License

This project is open source and available under the MIT License.
