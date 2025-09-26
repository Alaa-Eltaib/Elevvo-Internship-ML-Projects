# Elevvo Internship ML Projects

Welcome to the **Elevvo Internship ML Projects repository**! This file contains all the machine learning projects completed during the internship program. Each project includes dataset explanation, preprocessing, modeling, and evaluation steps.

---

## **1. Customer Segmentation**
- **Goal:** Segment customers based on their behavior and demographic features.  
- **Techniques:** K-Means clustering, feature scaling, and visualization.  
- **Steps:**  
  - Load dataset and explore features.  
  - Preprocess data: handle missing values, scale features.  
  - Apply K-Means clustering and visualize clusters.  
  - Evaluate and interpret cluster results.

---

## **2. Forest Cover Type Classification**
- **Goal:** Predict the forest cover type from cartographic variables.  
- **Techniques:** Decision Trees, Random Forests, feature engineering, and classification metrics.  
- **Steps:**  
  - Load and explore dataset.  
  - Preprocess data: encoding categorical features, feature engineering.  
  - Train Decision Tree and Random Forest classifiers.  
  - Evaluate models using accuracy, precision, recall, and F1-score.

---

## **3. Loan Approval Prediction**
- **Goal:** Predict whether a loan application will be approved or rejected.  
- **Techniques:** Logistic Regression, Decision Tree, Random Forest, XGBoost, handling imbalanced data with SMOTE, evaluation using Precision, Recall, and F1-score.  
- **Steps:**  
  - Load dataset and explore features.  
  - Handle missing values and encode categorical variables.  
  - Apply SMOTE to balance the dataset.  
  - Train multiple models (Logistic Regression, Decision Tree, Random Forest, XGBoost).  
  - Evaluate models and compare results using classification metrics.

---

## **4. Student Score Prediction**
- **Goal:** Predict student scores based on various study-related factors.  
- **Techniques:** Regression models, feature preprocessing, and evaluation using MAE, RMSE, and R².  
- **Steps:**  
  - Load and explore dataset.  
  - Preprocess features (handle missing values, scale numeric features).  
  - Train regression models (Linear Regression, Random Forest Regressor, etc.).  
  - Evaluate model performance using MAE, RMSE, and R² score.

---

## **Requirements**
- Python 3.11+  
- Core libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`  
- Additional libraries: `xgboost`, `imbalanced-learn`, `kagglehub`  

Install all required packages using:

```bash
pip install -r requirements.txt
