import pandas as pd
import joblib
import os

df = pd.read_csv("../data/processed_wallet_data.csv")
model = joblib.load("../src/models/catboost_model.pkl")

wallets = df["wallet"]
X = df.drop(columns=["wallet"])
predictions = model.predict(X)
predictions = [max(0, min(1000, int(round(score)))) for score in predictions]
output_df = pd.DataFrame({
    "wallet": wallets,
    "risk_score": predictions
})
output_df.to_csv("../data/wallet_risk_scores.csv", index=False)

print(" Risk scores predicted and saved to 'data/wallet_risk_scores.csv'")
 
