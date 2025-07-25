 
# fetch_data.py

import requests
import json
import os
import pandas as pd
from time import sleep
from config import ETHERSCAN_API_KEY, ETHERSCAN_BASE_URL, COMPOUND_V2_CONTRACTS


RAW_DATA_DIR = os.path.join("..", "data", "raw_txns")
os.makedirs(RAW_DATA_DIR, exist_ok=True)

wallet_df = pd.read_csv(os.path.join("..", "wallets.csv"))
wallets = wallet_df["wallet_id"].dropna().unique()


def fetch_wallet_txns(wallet_address):
    """Fetches all normal transactions for a wallet from Etherscan"""
    url = f"{ETHERSCAN_BASE_URL}?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&sort=asc&apikey={ETHERSCAN_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] == "1":
            return data["result"]
        else:
            print(f"  No transactions or error for {wallet_address}: {data['message']}")
            return []
    except Exception as e:
        print(f" Error fetching txns for {wallet_address}: {e}")
        return []

def filter_compound_txns(txns):
    """Keep only Compound-related txns (cTokens or Comptroller)"""
    compound_addresses = set(addr.lower() for addr in COMPOUND_V2_CONTRACTS["cTokens"])
    compound_addresses.add(COMPOUND_V2_CONTRACTS["Comptroller"].lower())
    
    filtered = [txn for txn in txns if txn["to"] and txn["to"].lower() in compound_addresses]
    return filtered

def main():
    for i, wallet in enumerate(wallets):
        print(f"\n[{i+1}/{len(wallets)}] Fetching txns for wallet: {wallet}")
        
        txns = fetch_wallet_txns(wallet)
        compound_txns = filter_compound_txns(txns)

        print(f" Found {len(compound_txns)} Compound txns")

        out_path = os.path.join(RAW_DATA_DIR, f"{wallet}.json")
        with open(out_path, "w") as f:
            json.dump(compound_txns, f, indent=2)

        sleep(0.3)

if __name__ == "__main__":
    main()
