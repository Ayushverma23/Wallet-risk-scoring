 
# config.py

from dotenv import load_dotenv
import os

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"

COMPOUND_V2_CONTRACTS = {
    "Comptroller": "0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b",
    "cTokens": [
        "0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643", 
        "0x39AA39c021dfbaE8faC545936693aC917d5E7563",  

    ]
}
