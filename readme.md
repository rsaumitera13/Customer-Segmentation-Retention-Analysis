# ⚡ STRATEGOS: Enterprise Retention OS v3.0    link -- https://customer-segmentation-retention-analysis-sumit.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-XGBoost-F37626)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit_Cloud-success)

## 📌 Project Overview
**STRATEGOS** is an end-to-end Machine Learning web application designed to solve a critical business problem: **Customer Churn**. 

Moving beyond basic exploratory data analysis, this project acts as a functional SaaS dashboard. It utilizes a trained XGBoost classifier to predict individual customer defection risk and prescribes targeted, real-time retention strategies based on user telemetry.

## 🎯 Business Value
Acquiring a new customer is exponentially more expensive than retaining an existing one. This tool allows Business Strategy and Customer Success teams to:
* **Identify At-Risk MRR (Monthly Recurring Revenue):** Proactively flag accounts likely to cancel.
* **Optimize Discount Budgets:** Prevent offering unneeded promotions to "Safe" customers.
* **Deploy Asymmetric Strategies:** Utilize principles like *Appealing to Self-Interest* to lock in high-value users via targeted contract upgrades.

## 💻 Tech Stack
* **Frontend UI:** Streamlit (Custom Glassmorphism CSS, Lottie Animations, Option Menu)
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Preprocessing), XGBoost (Classification Engine)
* **Visualizations:** Plotly Interactive Graphs
* **Model Serialization:** Joblib

## 🚀 Features
1. **Command Center:** Real-time KPI tracking (Retention Rate, LTV, Active Nodes).
2. **Risk Profiler:** Interactive ML inference. Input customer parameters (Tenure, Contract, Monthly Charges) to generate a dynamic risk gauge and AI-recommended actions.
3. **Strategy Vault:** Actionable retention playbooks mapping predictive output to real-world business tactics.

## 📂 Project Structure
```text
telco-retention-analytics/
├── .venv/                   # Local Python environment (Ignored in Git)
├── data/
│   └── telco_churn.csv      # Source Dataset (Kaggle)
├── app.py                   # Streamlit Frontend Application
├── engine.py                # ML Training & Pipeline Script
├── requirements.txt         # Production Dependencies
├── retention_model.pkl      # Serialized XGBoost Model
├── .gitignore               # Git rules
└── README.md                # Project Documentation                                                                                                                                                                Here is a professional, hiring-manager-ready README.md file designed to make your GitHub repository stand out.

It perfectly captures the "End-to-End Business Impact" narrative that companies in 2026 are looking for.

How to use this:
In your VS Code, create a new file named exactly README.md in your main project folder.

Copy and paste everything in the block below into that file.

Save it, then use the Git commands (git add README.md, git commit -m "Add README", git push origin main) to upload it to your repository.

Markdown
# ⚡ STRATEGOS: Enterprise Retention OS v3.0

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-XGBoost-F37626)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit_Cloud-success)

## 📌 Project Overview
**STRATEGOS** is an end-to-end Machine Learning web application designed to solve a critical business problem: **Customer Churn**. 

Moving beyond basic exploratory data analysis, this project acts as a functional SaaS dashboard. It utilizes a trained XGBoost classifier to predict individual customer defection risk and prescribes targeted, real-time retention strategies based on user telemetry.

## 🎯 Business Value
Acquiring a new customer is exponentially more expensive than retaining an existing one. This tool allows Business Strategy and Customer Success teams to:
* **Identify At-Risk MRR (Monthly Recurring Revenue):** Proactively flag accounts likely to cancel.
* **Optimize Discount Budgets:** Prevent offering unneeded promotions to "Safe" customers.
* **Deploy Asymmetric Strategies:** Utilize principles like *Appealing to Self-Interest* to lock in high-value users via targeted contract upgrades.

## 💻 Tech Stack
* **Frontend UI:** Streamlit (Custom Glassmorphism CSS, Lottie Animations, Option Menu)
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Preprocessing), XGBoost (Classification Engine)
* **Visualizations:** Plotly Interactive Graphs
* **Model Serialization:** Joblib

## 🚀 Features
1. **Command Center:** Real-time KPI tracking (Retention Rate, LTV, Active Nodes).
2. **Risk Profiler:** Interactive ML inference. Input customer parameters (Tenure, Contract, Monthly Charges) to generate a dynamic risk gauge and AI-recommended actions.
3. **Strategy Vault:** Actionable retention playbooks mapping predictive output to real-world business tactics.

## 📂 Project Structure
```text
telco-retention-analytics/
├── .venv/                   # Local Python environment (Ignored in Git)
├── data/
│   └── telco_churn.csv      # Source Dataset (Kaggle)
├── app.py                   # Streamlit Frontend Application
├── engine.py                # ML Training & Pipeline Script
├── requirements.txt         # Production Dependencies
├── retention_model.pkl      # Serialized XGBoost Model
├── .gitignore               # Git rules
└── README.md                # Project Documentation
⚙️ Local Installation & Setup
1. Clone the repository:

Bash
git clone https://github.com/rsaumitera13/Customer-Segmentation-Retention-Analysis
cd telco-retention-analytics
2. Create and activate a virtual environment:

Bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies:

Bash
pip install -r requirements.txt
4. Train the ML Engine (Generates .pkl file):

Bash
python engine.py
5. Launch the Dashboard:

Bash
streamlit run app.py
🧠 The Machine Learning Pipeline
The backend engine (engine.py) processes raw telecom data, handling missing values in financial columns. It utilizes Scikit-Learn's LabelEncoder for categorical feature transformation and trains an XGBClassifier optimized for logloss. The resulting model is serialized for rapid inference by the Streamlit frontend.

👨‍💻 Author
Saumitra S. Rath

Data scientist | 2025 Graduate

📍 Hyderabad, IN

