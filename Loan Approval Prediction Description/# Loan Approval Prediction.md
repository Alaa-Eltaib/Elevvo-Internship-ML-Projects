# Loan Approval Prediction

This project aims to build and evaluate machine learning models to predict **loan approval status** based on applicant and financial details.  
The dataset was obtained from [Kaggle](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset).

---

## 📂 Project Structure

- **Data Loading**  
  Downloaded via `kagglehub`, cleaned, and preprocessed.  
  - Removed extra spaces in column names.  
  - Encoded target column (`loan_status`: Approved → 1, Rejected → 0).  
  - Split dataset into numeric and categorical features.

- **Preprocessing**  
  - **Numerical Features** → Median imputation + Standard Scaling.  
  - **Categorical Features** → Most frequent imputation + One-hot encoding.  
  - Combined using `ColumnTransformer`.

- **Models Tested**
  - Logistic Regression (with/without SMOTE)
  - Decision Tree
  - Random Forest
  - XGBoost

- **Evaluation Metrics**
  - Precision  
  - Recall  
  - F1-score  

- **Model Comparison Table (Top Results)**  

  | Model                | Precision | Recall | F1-score |
  |-----------------------|-----------|--------|----------|
  | Random Forest         | 0.985     | 0.987  | 0.986    |
  | XGBoost              | 0.981     | 0.987  | 0.984    |
  | Decision Tree         | 0.978     | 0.987  | 0.982    |
  | Logistic Regression   | 0.955     | 0.921  | 0.938    |
  | Logistic + SMOTE      | 0.951     | 0.923  | 0.937    |

---

## ✅ Best Model

The **Random Forest Classifier** achieved the highest performance.  
It was retrained on the full dataset and saved as:

```bash
loan_model.pkl


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
