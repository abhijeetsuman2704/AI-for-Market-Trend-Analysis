# 📈 AI for Market Trend Analysis

This project analyzes **US retail sales and macroeconomic trends** using data-driven techniques.  
It combines **time-series forecasting, clustering, and a custom Retail Health Index** to provide insights that support **strategic planning for retailers**.

---

## 🔎 Project Overview
- **Objective**: Understand US retail performance and its relationship with macroeconomic indicators.  
- **Methods**: Data cleaning, feature engineering, forecasting models (e.g., Ridge, LSTM, Prophet), clustering, and health index creation.  
- **Outcome**: An interactive **Streamlit dashboard** to visualize trends, retailer clusters, and forecasts.  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/AI-for-Market-Trend-Analysis.git
cd AI-for-Market-Tr

2. Create and activate a virtual environment

python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit dashboard

streamlit run streamlit_app.py

AI-for-Market-Trend-Analysis/
├── README.md               <- Project documentation (this file)
├── requirements.txt        <- Python dependencies
├── streamlit_app.py        <- Streamlit dashboard entry point
├── notebooks/              <- Jupyter notebooks with analysis
├── src/                    <- Python scripts for data & models
│   ├── data.py
│   ├── features.py
│   ├── models.py
│   └── utils.py
└── data/                   <- Sample datasets (for demo only)

