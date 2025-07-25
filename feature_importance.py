 
from catboost import CatBoostRegressor, Pool
import joblib
import pandas as pd
import matplotlib.pyplot as plt


model = joblib.load("../src/models/catboost_model.pkl")
df = pd.read_csv("../data/processed_wallet_data.csv")

X = df.drop(columns=["wallet"])
y = pd.read_csv("../data/wallet_risk_scores.csv")["risk_score"]

feature_importances = model.get_feature_importance(Pool(X, y))
features = X.columns

plt.figure(figsize=(10, 6))
plt.barh(features, feature_importances, color="skyblue")
plt.xlabel("Importance")
plt.title("CatBoost Feature Importance")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=300)
print("Saved feature_importance.png successfully.")
