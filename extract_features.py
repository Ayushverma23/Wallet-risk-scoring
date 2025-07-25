import os
import json
import pandas as pd
from tqdm import tqdm

RAW_TXN_FOLDER = "../data/raw_txns"

FUNCTIONS = [
    "mint",
    "borrow",
    "repayBorrow",
    "redeem",
    "redeemUnderlying",
    "liquidateBorrow"
]

wallet_data = []

for filename in tqdm(os.listdir(RAW_TXN_FOLDER)):
    if not filename.endswith(".json"):
        continue

    wallet = filename.replace(".json", "")
    filepath = os.path.join(RAW_TXN_FOLDER, filename)

   
    feature_dict = {
        "wallet": wallet,
        "total_txns": 0,
    }

    for fn in FUNCTIONS:
        feature_dict[f"{fn}_count"] = 0

    try:
        with open(filepath, "r") as f:
            txns = json.load(f)

   
        if not isinstance(txns, list):
            txns = []

        feature_dict["total_txns"] = len(txns)

        for txn in txns:
            fn_name = txn.get("functionName", "")
            for fn in FUNCTIONS:
                if fn in fn_name:
                    feature_dict[f"{fn}_count"] += 1

    except Exception as e:
        print(f" Error processing {filename}: {e}")

    wallet_data.append(feature_dict)

df = pd.DataFrame(wallet_data)
df.to_csv("../data/processed_wallet_data.csv", index=False)

print(" Feature extraction complete. Output: processed_wallet_data.csv")
