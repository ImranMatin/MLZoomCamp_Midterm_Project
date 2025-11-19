import requests
import json

# The URL where your Docker container is listening
URL = "http://localhost:8000/predict"

# 1. Define a Valid Customer Payload (Happy Path)
# This matches the Pydantic model defined in app.py
valid_customer = {
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

# 2. Define an Invalid Payload (Error Path)
# Missing 'tenure' and 'MonthlyCharges' to trigger validation error
invalid_customer = {
    "gender": "Male",
    "SeniorCitizen": 0
}


def run_tests():
    print("--- Starting API Tests ---\n")

    # TEST 1: Valid Prediction
    try:
        print(f"Sending request to {URL}...")
        response = requests.post(URL, json=valid_customer)

        if response.status_code == 200:
            data = response.json()
            print("✅ Success! 200 OK")
            print(f"   Prediction: {data['prediction']}")
            print(f"   Probability: {data['churn_probability']}")
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print(response.text)

    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Is the Docker container running?")
        return

    print("\n" + "-"*30 + "\n")

    # TEST 2: Data Validation (Expecting Failure)
    print("Testing invalid data handling...")
    response = requests.post(URL, json=invalid_customer)

    if response.status_code == 422:
        print("✅ Success! Received expected 422 Validation Error.")
        # FastAPI automatically sends details about what field was missing
        detail = response.json()['detail']
        print(
            f"   API correctly identified missing fields: {len(detail)} errors found.")
    else:
        print(
            f"❌ Unexpected status code: {response.status_code} (Expected 422)")

    print("\n--- Tests Completed ---")


if __name__ == "__main__":
    run_tests()
