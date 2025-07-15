from collections import defaultdict
from datetime import datetime
import pandas as pd

def extract_wallet_features(transactions):
    wallet_features = defaultdict(lambda: {
        "total_deposit": 0,
        "total_borrow": 0,
        "total_repay": 0,
        "total_redeem": 0,
        "total_liquidation": 0,
        "action_count": 0,
        "unique_assets": set(),
        "first_tx": None,
        "last_tx": None
    })

    for tx in transactions:
        wallet = tx.get("userWallet", "")
        action = tx.get("action", "").lower()
        amount = int(tx["actionData"]["amount"]) / 1e6  # for USDC (6 decimals)
        asset = tx.get("asset", "")
        timestamp = int(tx.get("timestamp", 0))

        wallet_data = wallet_features[wallet]
        wallet_data["action_count"] += 1
        wallet_data["unique_assets"].add(asset)

        if wallet_data["first_tx"] is None or timestamp < wallet_data["first_tx"]:
            wallet_data["first_tx"] = timestamp
        if wallet_data["last_tx"] is None or timestamp > wallet_data["last_tx"]:
            wallet_data["last_tx"] = timestamp

        if action == "deposit":
            wallet_data["total_deposit"] += amount
        elif action == "borrow":
            wallet_data["total_borrow"] += amount
        elif action == "repay":
            wallet_data["total_repay"] += amount
        elif action == "redeemunderlying":
            wallet_data["total_redeem"] += amount
        elif action == "liquidationcall":
            wallet_data["total_liquidation"] += 1

    rows = []
    for wallet, data in wallet_features.items():
        time_span_days = (
            (data["last_tx"] - data["first_tx"]) / (60 * 60 * 24)
            if data["first_tx"] and data["last_tx"] else 0
        )
        repay_ratio = (
            data["total_repay"] / data["total_borrow"]
            if data["total_borrow"] > 0 else 0
        )
        rows.append({
            "wallet": wallet,
            "total_deposit": data["total_deposit"],
            "total_borrow": data["total_borrow"],
            "total_repay": data["total_repay"],
            "repay_ratio": repay_ratio,
            "total_redeem": data["total_redeem"],
            "total_liquidation": data["total_liquidation"],
            "action_count": data["action_count"],
            "unique_assets": len(data["unique_assets"]),
            "time_span_days": time_span_days,
        })

    return pd.DataFrame(rows)
