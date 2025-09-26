# Loan Approval Prediction

## Project Description
This project aims to build a machine learning model to predict whether a loan application will be approved or rejected. The dataset used is the [Loan-Approval-Prediction-Dataset](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset) from Kaggle.  

The project covers:
- Binary classification  
- Handling imbalanced data  
- Feature preprocessing (handling missing values, encoding categorical features)  
- Model evaluation focusing on **Precision, Recall, and F1-score**  
- Bonus: using **SMOTE** to address class imbalance  

---

## Dataset
The dataset contains **4269 rows** and **13 columns**:
- `loan_id`: Unique identifier  
- `no_of_dependents`: Number of dependents  
- `education`: Education level  
- `self_employed`: Whether applicant is self-employed  
- `income_annum`: Annual income  
- `loan_amount`: Loan amount  
- `loan_term`: Loan term (months)  
- `cibil_score`: Credit score  
- `residential_assets_value`: Residential assets value  
- `commercial_assets_value`: Commercial assets value  
- `luxury_assets_value`: Luxury assets value  
- `bank_asset_value`: Bank assets value  
- `loan_status`: Target variable (`Approved` or `Rejected`)  

---

## Installation & Requirements

- Python 3.11+  
- Required Python packages (can install via `requirements.txt`):

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn kagglehub
