from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model at startup
model = joblib.load('model.joblib')

app = FastAPI()

# Define expected input data structure


class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.post("/predict")
def predict(data: CustomerData):
    # Convert input data to DataFrame
    df_input = pd.DataFrame([data.dict()])

    # Predict
    prediction = model.predict(df_input)
    probability = model.predict_proba(df_input)

    result = "Churn" if prediction[0] == 1 else "No Churn"
    churn_prob = round(probability[0][1] * 100, 2)

    return {"prediction": result, "churn_probability": f"{churn_prob}%"}
