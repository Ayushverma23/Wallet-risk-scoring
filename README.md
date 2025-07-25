 
#  Wallet Risk Scoring using Compound V2 Transaction Data

This project aims to build a machine learning-based risk scoring system (0–1000 scale) for crypto wallets based on their interaction history with the **Compound V2 DeFi protocol**. The output can be used to assess the credibility and riskiness of a given wallet.

---

##  Overview

The goal is to process 100 wallet addresses and assign each a **risk score** by analyzing their on-chain activity. We extract behavioral and financial features from the Compound protocol, apply data processing and feature engineering, train a regression model, and generate risk scores accordingly.

---

##  1. Data Collection

- **Source**: We used the **Compound V2 protocol** and queried data via the **Etherscan API**.
- **Wallet Sample**: 100 wallet addresses provided for analysis.
- **Endpoints Used**:
  - `txlist`: For wallet-level transaction history
  - `getLogs`: To extract protocol-specific interactions like supply, borrow, and repay actions

We gathered a snapshot of wallet behavior by calling Etherscan APIs for each address, saving the cleaned and structured output in `processed_wallet_data.csv`.

---

##  2. Feature Selection Rationale

From the raw data, we engineered and selected the following **key features** based on their relevance to financial behavior and risk prediction:

| Feature                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `num_transactions`         | Total number of Compound-related transactions                              |
| `num_borrows`              | Number of borrow actions – more borrows indicate higher financial exposure |
| `num_repayments`           | Number of times the user repaid loans – a sign of responsibility           |
| `num_liquidations`         | Number of times the wallet was liquidated – strong risk indicator          |
| `unique_tokens_interacted` | Diversity of tokens used – shows exposure and activity                      |
| `total_borrowed`           | Total borrowed value in USD-equivalent                                     |
| `total_repaid`             | Total repayment value – used to infer repayment behavior                   |
| `days_active`              | Number of days active on Compound                                          |

These features were stored in `features.csv`.

We dropped features with:
- High correlation with each other (to reduce multicollinearity)
- Low variance or zero-value across almost all wallets
- No significant predictive power in trial runs

---

##  3. Scoring Methodology

We framed the scoring task as a **regression problem**, where the model predicts a score between 0–1000.

### Model Choice:
We used **CatBoost Regressor** because:
- It handles categorical and numerical features efficiently
- It works well with small to medium tabular datasets
- It is robust against overfitting, especially with default parameters

### Training:
- Train-test split: 80-20%
- Evaluation metrics: MAE (Mean Absolute Error) and RMSE
- The model was trained on `features.csv` and stored as `catboost_model.pkl`

### Output:
We loaded the model and predicted scores for the 100 wallets using the same features. The results were saved to:

-  `data/wallet_risk_scores.csv`
-  A duplicate of this file was saved in the root as `wallet_risk_scores.csv`

---

##  4. Justification of Risk Indicators

We selected the risk indicators based on actual financial behavior in DeFi protocols:

| Indicator        | Why It Matters |
|------------------|----------------|
| **Liquidations** | A strong signal of wallet instability and inability to repay loans |
| **Low Repayment-to-Borrow Ratio** | Indicates default-prone behavior |
| **Few Transactions / Low Activity** | Often associated with low trust wallets or one-time scammers |
| **Token Diversity** | A proxy for wallet maturity – diversified usage implies more responsible activity |
| **High Borrowing Without Repayment** | Direct red flag, contributes to high risk |

All these indicators are used by real-world DeFi credit protocols to assess wallet risk.

---



## Future Improvements

- Add wallet clustering for better behavioral grouping
- Include non-Compound DeFi interactions 
- Build a real-time dashboard for live scoring new wallets
- Use graph-based wallet similarity as an additional signal

---

##  Requirements

Install dependencies with:
```bash
pip install pandas catboost scikit-learn requests matplotlib

```
## Author
Built by Ayush Verma
