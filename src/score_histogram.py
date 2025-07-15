import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_score_distribution(score_file, output_image):
    df = pd.read_csv(score_file)

    # Bucket scores into 0–100, 100–200, ..., 900–1000
    bins = [i for i in range(0, 1100, 100)]
    labels = [f"{i}-{i+99}" for i in range(0, 1000, 100)]
    df["score_bucket"] = pd.cut(df["score"], bins=bins, labels=labels, include_lowest=True)

    # Count wallets per bucket
    bucket_counts = df["score_bucket"].value_counts().sort_index()

    # Plot
    plt.figure(figsize=(10, 6))
    bucket_counts.plot(kind="bar", color="#4CAF50", edgecolor="black")
    plt.title("Wallet Credit Score Distribution")
    plt.xlabel("Score Range")
    plt.ylabel("Number of Wallets")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Save to assets/
    os.makedirs("assets", exist_ok=True)
    plt.savefig(output_image)
    print(f"[✓] Histogram saved at: {output_image}")

if __name__ == "__main__":
    score_csv = "wallet_scores.csv"  # Or wherever your output is saved
    output_image = "assets/score_histogram.png"
    plot_score_distribution(score_csv, output_image)
