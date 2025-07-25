#  Analysis: Wallet Risk Scoring using Compound V2/V3 Data

##  Objective
This project aims to assign **risk scores (0–1000)** to wallets based on their historical activity on the Compound protocol (V2/V3). These scores indicate the creditworthiness of wallets for DeFi platforms.

---

##  Data Collection

- Protocol: **Compound V2** (or V3)
- Source: Blockchain transaction data via Etherscan API
- Number of Wallets: **100 addresses**
- Data includes:
  - Borrow and repay amounts
  - Supply and redeem events
  - Token types
  - Timestamps and gas usage

---

##  Feature Engineering

Extracted meaningful features such as:

| Feature Name              | Description |
|--------------------------|-------------|
| `total_borrows`          | Total amount borrowed by the wallet |
| `total_supplies`         | Total supplied (collateral) amount |
| `repayment_ratio`        | Ratio of repaid to borrowed amount |
| `avg_txn_interval`       | Average time between transactions |
| `num_tokens_used`        | Count of unique tokens interacted with |
| `borrow_to_supply_ratio` | Borrow/Supply ratio — credit utilization |

Processed data saved in: `data/processed_wallet_data.csv`

---

##  Model Choice: CatBoost

### Why CatBoost?

- Handles categorical and numerical data natively  
- Works well with small and medium-sized datasets  
- Requires less hyperparameter tuning  
- Resistant to overfitting with built-in regularization  
- Faster and more interpretable than XGBoost in some cases

Trained model saved at: `src/models/catboost_model.pkl`

---

##  Risk Scoring Logic

- The model outputs a **risk probability/confidence** which is scaled to a **score between 0 and 1000**
- Higher score = lower risk (more creditworthy)

Final scores saved in: `data/wallet_risk_scores.csv`

---

##  Feature Importance

Top influencing features (based on CatBoost):

1. `repayment_ratio`
2. `total_borrows`
3. `borrow_to_supply_ratio`
4. `num_tokens_used`

Visualized in: `data/feature_importance.png`

---

##  Insights

- Wallets with **low repayment ratios** had consistently lower risk scores  
- Borrow-to-supply ratio was a strong indicator of responsible behavior  
- Diversification across tokens generally led to higher creditworthiness  
- Highly active wallets didn’t always mean low risk — transaction quality matters


##  File Overview

| File | Purpose |
|------|---------|
| `src/fetch_data.py` | Downloads transaction data |
| `src/extract_features.py` | Converts raw data to structured features |
| `src/train-model.py` | Trains CatBoost model |
| `src/scoring.py` | Generates scores for new wallets |
| `data/*.csv` | Raw + processed data, final scores |

---

##  Author
Ayush Verma  
[GitHub Repo](https://github.com/Ayushverma23/Wallet-risk-scoring)

