# Loan Approval Prediction

## Project Description

This project builds a machine learning model to predict whether a loan application will be approved or rejected. The dataset used is the [Loan-Approval-Prediction-Dataset](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset) from Kaggle.

The project covers:

* Binary classification
* Handling imbalanced data
* Feature preprocessing (handling missing values, encoding categorical features)
* Model evaluation focusing on **Precision, Recall, and F1-score**
* Bonus: using **SMOTE** to address class imbalance
* **Interactive GUI for loan prediction using Streamlit**

---

## Dataset

The dataset contains **4269 rows** and **13 columns**:

| Column                     | Description                                |
| -------------------------- | ------------------------------------------ |
| `loan_id`                  | Unique identifier                          |
| `no_of_dependents`         | Number of dependents                       |
| `education`                | Education level                            |
| `self_employed`            | Whether applicant is self-employed         |
| `income_annum`             | Annual income                              |
| `loan_amount`              | Loan amount                                |
| `loan_term`                | Loan term (months)                         |
| `cibil_score`              | Credit score                               |
| `residential_assets_value` | Residential assets value                   |
| `commercial_assets_value`  | Commercial assets value                    |
| `luxury_assets_value`      | Luxury assets value                        |
| `bank_asset_value`         | Bank assets value                          |
| `loan_status`              | Target variable (`Approved` or `Rejected`) |

---

## Installation & Requirements

* Python 3.11+
* Required Python packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn kagglehub streamlit joblib
```

---

## How to Run the GUI

1. Make sure your model file `loan_model.pkl` is in the same folder as `app.py`.
2. Open a terminal and navigate to the project folder.
3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. The interface will open in your browser. Fill in the applicant details **manually**, then click **Predict Loan Approval**.
5. The result will show whether the loan is **Approved (✅)** or **Rejected (❌)**.

---

## Notes

* All input fields are **empty by default**; the user must enter/select all values.
* The GUI is **dark-themed and modern**, with colored buttons for better user experience.
* Ensure numeric values are realistic to avoid errors in prediction.
