# MLZoomCamp_Midterm_Project

## 📉 End-to-End Customer Churn Prediction System

A production-grade Machine Learning system that predicts customer churn. This project demonstrates a full-stack MLOps lifecycle: from data engineering and model training to containerized deployment and data drift monitoring.

# Live Demo: [Link to your Render URL here]

# Docker Hub: [Link to your Docker Hub Repo here]

## 🏗️ Architecture

The system is built using a modular architecture, ensuring scalability and reproducibility.

- Data: Telco Customer Churn dataset (IBM).

- Training: Scikit-Learn Pipeline (Random Forest) with automated preprocessing.

- Serving: FastAPI for real-time inference.

- Deployment: Docker container deployed to Render Cloud.

- CI/CD: GitHub Actions triggers automated training and deployment on every push.

- Monitoring: Evidently, AI checks for data drift between training and production data.

## 🛠️ Tech Stack

- Language: Python 3.9

- ML Libraries: Scikit-learn, Pandas, Numpy, Joblib

- API Framework: FastAPI, Uvicorn

- Containerization: Docker

- Orchestration: GitHub Actions (CI/CD)

- Monitoring: Evidently AI

## 📂 Project Structure

├── .github/workflows
│   └── deploy.yml       # CI/CD Pipeline configuration
├── app.py               # FastAPI application (Inference)
├── train.py             # Training script (ETL + Model Training)
├── test_api.py          # Integration tests for the API
├── monitor_drift.py     # Drift detection script
├── Dockerfile           # Docker image definition
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

## 🚀 Getting Started

Option 1: Run with Docker (Recommended)
Pull the image:

docker pull <your-username>/churn-predictor:latest

Run the container:

docker run -p 8000:8000 <your-username>/churn-predictor:latest
Access the API: Open your browser to http://localhost:8000/docs to see the Swagger UI.

## Option 2: Run Locally

Clone the repo:

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
Install dependencies:

pip install -r requirements.txt
Train the model:

python train.py
## Output: Model trained and saved as model.joblib

Start the server:

- uvicorn app:app --reload
  
## 🔌 API Usage

The API accepts customer data and returns a Churn prediction (Yes/No) and a Probability score.

Endpoint: POST /predict

Example Request:

JSON

{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "No",
  "MultipleLines": "No phone service",
  "InternetService": "DSL",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "Yes",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 29.85,
  "TotalCharges": 29.85
}
Example Response:

JSON

{
  "prediction": "No Churn",
  "churn_probability": "14.5%"
}
📊 Monitoring & Observability
To ensure model reliability in production, this project uses Evidently AI to detect data drift.

Logging: The API logs all incoming requests to production_logs.csv.

Drift Check: Run the monitoring script to compare production data vs. training data.

Bash

python monitor_drift.py
Sample Drift Report:

[Insert a screenshot of your evidently html report here]

🔄 CI/CD Pipeline
This project uses GitHub Actions for continuous integration and deployment:

Push to Main: Triggers the pipeline.

Build: Sets up Python environment and installs dependencies.

Train: Runs train.py to ensure the model is retrained on the latest code/data.

Containerize: Builds a new Docker image.

Deploy: Pushes the image to Docker Hub and triggers a redeploy on Render.
