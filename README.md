# Credit-Risk-Loan-Default-Prediction-System
Perfect! Here’s a **professional, GitHub-ready README** for your **Credit Risk & Loan Default Prediction System** including **model comparison, insights, and business recommendations**. You can copy-paste this directly:

---

# Credit Risk & Loan Default Prediction System 🏦💳

This project focuses on predicting **loan defaults** using a **comprehensive lending dataset** from Kaggle. By analyzing borrower, loan, and collateral details, we build a **machine learning system** to help banks **assess credit risk efficiently**.

📊 Dataset: [Loan Default Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/loan-default-dataset)

---

## Table of Contents

* [Project Overview](#project-overview)
* [Dataset Description](#dataset-description)
* [Feature Breakdown](#feature-breakdown)
* [Target Variable](#target-variable)
* [Risk Drivers](#risk-drivers)
* [Modeling Approach](#modeling-approach)
* [Model Comparison](#model-comparison)
* [Business Recommendations](#business-recommendations)
* [How to Use](#how-to-use)
* [License](#license)

---

## Project Overview

Banks face **loan default risk**, which can cause financial losses. Machine learning helps:

* Predict the likelihood of default
* Identify **high-risk borrowers** before loan approval
* Optimize lending strategies and reduce losses

This system uses **numerical, categorical, and derived risk features** for predictive modeling.

---

## Dataset Description

The dataset contains **loan applications and borrower information**, including:

* Borrower demographics and credit history
* Loan terms, interest rates, and upfront fees
* Collateral and property details

It is widely used for **credit risk modeling** and contains **real-world financial features**.

---

## Feature Breakdown

### 🆔 Basic Identifiers

| Feature | Description                    | ML Use                  |
| ------- | ------------------------------ | ----------------------- |
| ID      | Unique loan application number | Not used for prediction |
| year    | Year loan was applied          | Trend analysis          |

### 👤 Borrower Details

| Feature | Description        | ML Use                                   |
| ------- | ------------------ | ---------------------------------------- |
| Gender  | Applicant’s gender | Optional demographic analysis            |
| age     | Borrower age       | Risk patterns vary by age group          |
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

| Feature       | Description        | ML Use          |
| ------------- | ------------------ | --------------- |
| loan_type     | Type of loan       | Categorization  |
| loan_purpose  | Purpose of loan    | Risk assessment |
| loan_amount   | Total loan amount  | Core predictor  |
| term          | Loan duration      | Risk timing     |
| loan_limit    | Loan category      | Risk category   |
| approv_in_adv | Pre-approved loan? | Optional        |

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

### 🏠 Property Details

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

🔥 **This is what the model predicts.**

---

## Risk Drivers

**Top Influential Features:**

1. Credit_Score
2. Income
3. LTV (Loan-to-Value)
4. dtir1 (Debt-to-Income)
5. Loan Amount
6. Rate of Interest
7. Property Value
8. Credit_Worthiness

These features are the **most important for predicting loan default**.

---

## Modeling Approach

* Data cleaning and preprocessing
* Feature engineering: LTV, DTI, loan ratios
* Encoding categorical variables
* Train/test split with stratification
* Models used: Logistic Regression, Decision Tree, Random Forest, XGBoost
* Evaluation: Accuracy, ROC-AUC, Confusion Matrix

---

## Model Comparison

| Model               | Train Accuracy | Test Accuracy | Train AUC | Test AUC |
| ------------------- | -------------- | ------------- | --------- | -------- |
| Logistic Regression | 1.000          | 0.780         | 1.000     | 0.952    |
| Decision Tree       | 0.914          | 0.868         | 0.945     | 0.825    |
| Random Forest       | 0.891          | 0.834         | 0.923     | 0.749    |
| XGBoost             | 0.917          | 0.871         | 0.923     | 0.749    |

**Test Accuracy Ranking:**

1. XGBoost – 0.871
2. Decision Tree – 0.868
3. Random Forest – 0.834
4. Logistic Regression – 0.780

**Key Insights:**

* **Logistic Regression:** High AUC but poor Class 1 detection → Overfitting
* **Decision Tree:** Balanced, strong Class 1 detection
* **Random Forest:** Moderate performance
* **XGBoost:** Best overall Test Accuracy, good generalization

---

## Business Recommendations

1. **Risk-Based Loan Approval**
   Reject or manually review high-risk applicants (high LTV, DTI, low credit score, negative amortization).

2. **LTV & Loan Amount Control**
   Cap LTV at 75–80% and reduce loan amounts for high-LTV borrowers.

3. **Debt Burden Monitoring**
   Approve loans only if DTI ≤ 40%; offer longer tenure for high DTI.

4. **Credit Score-Based Pricing**
   Lower interest rates for high-score borrowers; stricter terms for low-score borrowers.

5. **Interest Rate Spread Management**
   Avoid excessive spreads for borderline-risk customers.

6. **High-Risk Flags**
   Manual review for negative amortization, large lump sums, or risky co-applicant types.

7. **Upfront Charges Optimization**
   Reduce or waive charges for medium/low-risk customers to reduce financial stress.

8. **Early Warning & Monitoring System**
   Track medium/high-risk borrowers post-disbursement; send reminders or restructure options.

9. **Portfolio Strategy**
   Limit exposure to high LTV / low credit score segments and monitor defaults by loan type and application channel.

**Business Value:**

* Reduces Non-Performing Assets (NPA)
* Improves approval decision speed
* Enhances profitability and customer experience

---

## How to Use

1. Clone repository:

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

This project is **educational** using a public dataset. Review Kaggle dataset license before commercial use.

---

I can also **make this README visually pop with badges, GIFs for model performance, and feature importance charts** like a professional data science repo.

Do you want me to do that next?
