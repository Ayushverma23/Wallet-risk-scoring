import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os

df = pd.read_csv("../data/processed_wallet_data.csv")
df.fillna(0, inplace=True)

X = df.drop(columns=["wallet"])
y = X["total_txns"].apply(lambda x: min(x * 10, 1000))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = CatBoostRegressor(
    iterations=200,
    depth=6,
    learning_rate=0.1,
    loss_function='RMSE',
    verbose=False
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/catboost_model.pkl")
print("Model saved to models/catboost_model.pkl")
