# Credit-Risk-Loan-Default-Prediction-System
Absolutely! Here's a **ready-to-copy GitHub README** for your **Credit Risk & Loan Default Prediction System** project:

---

# Credit Risk & Loan Default Prediction System 🏦💳

This project focuses on predicting **loan defaults** using a **comprehensive lending dataset** from Kaggle. By analyzing borrower, loan, and collateral details, we aim to build a **machine learning model** that helps banks **assess credit risk efficiently**.

📊 Dataset: [Loan Default Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/loan-default-dataset)

---

## Table of Contents

* [Project Overview](#project-overview)
* [Dataset Description](#dataset-description)
* [Feature Breakdown](#feature-breakdown)
* [Target Variable](#target-variable)
* [Risk Drivers](#risk-drivers)
* [Modeling Approach](#modeling-approach)
* [How to Use](#how-to-use)
* [License](#license)

---

## Project Overview

Banks and financial institutions face **loan default risk**, which can lead to significant financial losses. By leveraging machine learning, we can:

* Predict the likelihood of a borrower defaulting on a loan
* Identify **high-risk borrowers** before loan approval
* Optimize lending strategies and minimize losses

This project builds a **predictive system** using numerical, categorical, and derived risk features.

---

## Dataset Description

The dataset contains **full lending and borrower information**, including:

* Loan applications and borrower demographics
* Credit history and credit score
* Loan terms, interest rates, and upfront fees
* Collateral and property details

This dataset is widely used for **credit risk modeling** and provides **real-world financial features**.

---

## Feature Breakdown

### 🆔 Basic Identifiers

| Feature | Description                    | ML Use                    |
| ------- | ------------------------------ | ------------------------- |
| ID      | Unique loan application number | Not useful for prediction |
| year    | Year loan was applied/issued   | Trend analysis            |

### 👤 Borrower Details

| Feature | Description        | ML Use                                   |
| ------- | ------------------ | ---------------------------------------- |
| Gender  | Applicant’s gender | Optional demographic analysis            |
| age     | Borrower age       | Risk pattern varies by age group         |
| income  | Annual income      | Higher income → better repayment ability |

### 💳 Credit Profile

| Feature                  | Description                  | ML Use                  |
| ------------------------ | ---------------------------- | ----------------------- |
| Credit_Worthiness        | Lender assessment (Good/Bad) | Strong predictor        |
| Credit_Score             | Numeric credit score         | Most powerful predictor |
| credit_type              | Type of credit history       | Risk signal             |
| open_credit              | Active credit lines          | Risk indicator          |
| co-applicant_credit_type | Co-borrower credit profile   | Risk adjustment         |

### 🏦 Loan Details

| Feature       | Description        | ML Use           |
| ------------- | ------------------ | ---------------- |
| loan_type     | Type of loan       | Categorization   |
| loan_purpose  | Purpose of loan    | Risk assessment  |
| loan_amount   | Total loan amount  | Core predictor   |
| term          | Loan duration      | Risk timing      |
| loan_limit    | Loan category      | Risk category    |
| approv_in_adv | Pre-approved loan? | Optional feature |

### 💰 Interest & Charges

| Feature              | Description             | ML Use                |
| -------------------- | ----------------------- | --------------------- |
| rate_of_interest     | Loan interest rate      | Direct risk factor    |
| Interest_rate_spread | Difference vs benchmark | High spread → riskier |
| Upfront_charges      | Fees paid initially     | Minor predictor       |

### 🧾 Payment Structure

| Feature           | Description                  | ML Use               |
| ----------------- | ---------------------------- | -------------------- |
| Neg_ammortization | Negative amortization        | High risk            |
| interest_only     | Only interest paid initially | Risk increase later  |
| lump_sum_payment  | Large final payment          | Balloon payment risk |

### 🏠 Property Details (Collateral)

| Feature           | Description              | ML Use          |
| ----------------- | ------------------------ | --------------- |
| property_value    | Market value of property | Core predictor  |
| construction_type | Building type            | Optional        |
| occupancy_type    | Owner occupied / rental  | Optional        |
| Secured_by        | Asset securing loan      | Risk adjustment |
| Security_Type     | Collateral type          | Optional        |
| total_units       | Housing units            | Optional        |

### 📊 Risk Ratios

| Feature                | Formula                      | Description                        |
| ---------------------- | ---------------------------- | ---------------------------------- |
| LTV                    | Loan Amount ÷ Property Value | Higher LTV → higher default risk   |
| dtir1 (Debt-to-Income) | Total Debt ÷ Income          | Higher DTI → overburdened borrower |

### 🏢 Loan Usage Category

| Feature                | Description    | ML Use                       |
| ---------------------- | -------------- | ---------------------------- |
| business_or_commercial | Business loan? | Business loans often riskier |

### 📍 Location

| Feature | Description     | ML Use                          |
| ------- | --------------- | ------------------------------- |
| Region  | Property region | Economic conditions impact risk |

### 📄 Application Process

| Feature                   | Description              | ML Use   |
| ------------------------- | ------------------------ | -------- |
| submission_of_application | Online / Branch / Broker | Optional |

---

## Target Variable

| Feature | Description                                                |
| ------- | ---------------------------------------------------------- |
| Status  | Loan outcome: Default / Non-default or Approved / Rejected |

🔥 **This is the variable we predict** in our credit risk ML model.

---

## Risk Drivers

**Top Features Banks Focus On:**

1. Credit_Score
2. Income
3. LTV (Loan-to-Value)
4. dtir1 (Debt-to-Income)
5. Loan Amount
6. Rate of Interest
7. Property Value
8. Credit_Worthiness

These features are the **most influential** for predicting loan defaults.

---

## Modeling Approach

* Data cleaning and preprocessing
* Feature engineering: LTV, DTI, loan ratios
* Encoding categorical variables
* Train/test split with stratification
* ML models used: Logistic Regression, Random Forest, XGBoost
* Model evaluation: Accuracy, ROC-AUC, Confusion Matrix

---

## How to Use

1. Clone this repository:

```bash
git clone <repo-url>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run Jupyter notebooks or Python scripts for analysis and model training.

---

## License

This project is for **educational purposes** using a publicly available dataset. Please review Kaggle dataset license before commercial use.

---

If you want, I can **also make a version with badges, dataset stats, and ML results** that you can directly paste to GitHub for a **professional look**.

Do you want me to do that version too?
