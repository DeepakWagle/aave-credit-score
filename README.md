# 💳 Aave V2 Wallet Credit Scoring

This project is a machine learning-based solution for assigning **credit scores (0–1000)** to wallets interacting with the **Aave V2 DeFi protocol**. It analyzes historical wallet transactions such as deposits, borrows, repayments, and liquidations to quantify wallet reliability.

> Built for the [HackerEarth Aave V2 Credit Scoring Challenge](https://foursquare.hackerearth.com/).

---

## 🚀 Features

- Parses raw JSON data of 100K+ Aave V2 transactions
- Engineers features per wallet based on transaction patterns
- Assigns credit scores using heuristic or rule-based logic
- Outputs scores to `wallet_scores.csv`
- Visualizes distribution with a credit score histogram
- Includes transparent analysis in `analysis.md`

---

## 🧠 Tech Stack

- **Python 3.10+**
- Libraries: `pandas`, `matplotlib`, `argparse`, `json`

---

## 📂 Project Structure

```bash
aave-credit-score/
├── data/
│   └── user-wallet-transactions.json        # Raw Aave V2 JSON transaction data
├── wallet_scores.csv                        # Final scored wallets (output)
├── assets/
│   └── score_histogram.png                  # Credit score distribution plot
├── src/
│   ├── feature_engineering.py               # Wallet-level feature extraction
│   ├── score_generator.py                   # Score calculator CLI script
│   └── score_histogram.py                   # Histogram visualizer
├── analysis.md                              # Score insights and distribution summary
├── README.md
```

##⚙️ Installation

# 1. Clone the repository
git clone https://github.com/your-username/aave-credit-score.git
cd aave-credit-score

# 2. Create a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt


## 🛠️ Usage
Generate Wallet Credit Scores:
python src/score_generator.py --input data/user-wallet-transactions.json --output wallet_scores.csv

Plot Score Distribution:
python src/score_histogram.py
This will create assets/score_histogram.png.

## 🧾 Example Output
| Wallet Address                             | Credit Score |
| ------------------------------------------ | ------------ |
| 0x00000000001accfa9cef68cf5371a23025b6d4b6 | 850          |
| 0x000000000051d07a4fb3bd10121a343d85818da6 | 850          |
| 0x000000000a38444e0a6e37d3b630d7e855a7cb13 | 1000         |
| ...                                        | ...          |

