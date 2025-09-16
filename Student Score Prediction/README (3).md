# 📘 Student Performance Prediction

## 📌 Project Overview
This project focuses on student performance prediction using various academic, social, and personal factors.  
The dataset was preprocessed, encoded, and enriched through feature engineering to improve model accuracy.

---

## 🛠️ Steps Followed

### 🔹 Data Cleaning
- Removed duplicates and handled missing values (using median/mode imputation).  
- Standardized categorical values (e.g., "Yes/No" → 1/0).  

### 🔹 Encoding
- **Ordinal encoding** for ordered features (e.g., "Low", "Medium", "High").  
- **One-hot encoding** for nominal categorical features (e.g., School_Type, Gender).  

### 🔹 Feature Engineering
Created new features such as:  
- `study_sleep_ratio = Hours_Studied / (Sleep_Hours + 1)`  
- `is_high_attendance = (Attendance > 90)`  
- `parent_support_index = Parental_Involvement * Parental_Education_Level`  
- `activity_score = Extracurricular_Activities + Physical_Activity`  
- `improvement_ratio = Exam_Score / (Previous_Scores + 1)`  
- And several other derived features.  

### 🔹 Modeling
- Split the dataset into training and testing sets.  
- Trained regression models: **Linear Regression, Random Forest, SVM** to predict *Exam Score*.  
- Evaluated models using:  
  - MSE (Mean Squared Error)  
  - RMSE (Root Mean Squared Error)  
  - MAE (Mean Absolute Error)  
  - R² Score  

---

## 📊 Results
- Models achieved strong performance, with **R² close to 1.0** in cross-validation.  
- **Feature engineering significantly improved prediction accuracy.**  

---

## 🚀 How to Run

Clone the repository:
```bash
git clone <your-repo-link>
```

Install required libraries:
```bash
pip install -r requirements.txt
```

Run the notebook or script:
```bash
jupyter notebook student_performance.ipynb
```

---

## 📌 Notes
- The dataset requires preprocessing before model training.  
- Feature engineering plays a crucial role in boosting accuracy.  
- Future improvements could include hyperparameter tuning and testing deep learning models.  
