import json
import argparse
import pandas as pd
from feature_engineering import extract_wallet_features

def assign_credit_score(row):
    score = 1000

    # Penalize liquidations
    score -= row["total_liquidation"] * 100

    # Penalize poor repay behavior
    if row["repay_ratio"] < 0.5:
        score -= 150
    elif row["repay_ratio"] < 1.0:
        score -= 75

    # Penalize excessive borrowing without deposit
    if row["total_deposit"] == 0 and row["total_borrow"] > 0:
        score -= 200

    # Reward long active usage
    if row["time_span_days"] > 30:
        score += 50

    # Normalize score
    return max(0, min(1000, int(score)))

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        transactions = json.load(f)

    df = extract_wallet_features(transactions)
    df["score"] = df.apply(assign_credit_score, axis=1)

    df[["wallet", "score"]].to_csv(output_file, index=False)
    print(f"Scoring complete. Output saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='user-wallet-transactions.json')
    parser.add_argument('--output', default='wallet_scores.csv', help='Output CSV file')
    args = parser.parse_args()

    main(args.input, args.output)
