# Automated Sales Analysis Dashboard

A portfolio-ready data analytics project that cleans and analyzes the **Superstore** dataset, then presents business insights in a live **Streamlit dashboard**.

## Why this project?
Manual sales reporting is slow and hard to scale. This project automates the process so decision-makers can quickly see performance, trends, and risk areas.

## What it delivers
- **Total Sales and Total Profit KPIs**
- **Top 5 products by sales**
- **Sales by region**
- **Monthly sales trend**
- **Top 5 loss-making products**

## Tech stack
- Python
- Pandas
- Matplotlib
- Streamlit

## Project structure
```text
.
├── app.py              # Streamlit dashboard (portfolio/demo app)
├── analysis.py         # Script-based analysis workflow
├── data/
│   └── Superstore.csv
└── requirements.txt
```

## Run locally
```bash
# 1) Create and activate virtual environment (optional but recommended)
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run dashboard
streamlit run app.py
```

## Run script version
```bash
python analysis.py
```

## Deployment (Streamlit Community Cloud)
1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Select your repo, branch `main`, and file `app.py`.
4. Deploy.

## Portfolio links
- **Live Demo:** `https://your-app-name.streamlit.app`
- **GitHub Repo:** `https://github.com/your-username/your-repo-name`
