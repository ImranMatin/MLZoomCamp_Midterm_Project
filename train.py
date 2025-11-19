import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier


def train():
    # Load
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    df = pd.read_csv(url)

    # Clean
    df['TotalCharges'] = pd.to_numeric(
        df['TotalCharges'], errors='coerce').fillna(0)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    X = df.drop(['customerID', 'Churn'], axis=1)
    y = df['Churn']

    # Preprocessing
    numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
    categorical_features = [c for c in X.columns if c not in numeric_features]

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)])

    # Pipeline
    clf = Pipeline(steps=[('preprocessor', preprocessor),
                          ('classifier', RandomForestClassifier(n_estimators=100, max_depth=10))])

    clf.fit(X, y)

    # Save
    joblib.dump(clf, 'model.joblib')
    print("Model trained and saved.")


if __name__ == "__main__":
    train()
