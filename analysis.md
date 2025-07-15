# 📈 Wallet Credit Score Analysis

This document provides a quick analysis of the credit scores assigned to 3,498 Aave V2 wallets based on their historical transaction behavior.

---

## 📊 Score Distribution

![Score Distribution](assets/score_histogram.png)

---

## 🧮 Score Buckets

## 📊 Score Buckets Summary

| Score Range | Wallet Count | Notes |
|-------------|---------------|-------|
| 0–699       | Very Few      | Mostly incomplete, risky, or inactive wallets |
| 700–849     | ~50–100       | Moderate DeFi activity, partial repayment |
| 850–899     | ~2600+        | Reliable deposit-repay cycles |
| 900–999     | ~800+         | High reliability, heavy DeFi usage |

> Replace `X`, `Y`, `Z` with actual numbers by grouping in pandas.

```python
import pandas as pd
df = pd.read_csv("wallet_scores.csv")
pd.cut(df['score'], bins=[0, 699, 849, 949, 1000]).value_counts()