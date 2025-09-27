# 🎓 Student Performance Prediction

This project analyzes the **Student Performance Factors dataset** from Kaggle to predict **exam scores** based on multiple academic, social, and personal factors.  
Models applied include **Linear Regression** and **Polynomial Regression**, with feature engineering and preprocessing steps to improve predictions.

---

## 📂 Dataset

- **Source**: [Student Performance Factors Dataset on Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)  
- **Rows**: 6,607  
- **Columns**: 20 (mix of numerical, categorical, and binary features)  
- **Target Variable**: `Exam_Score` (55 – 101)

### Key Features
- **Numerical**: `Hours_Studied`, `Attendance`, `Sleep_Hours`, `Previous_Scores`, `Physical_Activity`, `Tutoring_Sessions`.  
- **Categorical**: `Parental_Involvement`, `Access_to_Resources`, `Motivation_Level`, `School_Type`, `Gender`, etc.  
- **No major missing values**, except for some categorical fields (handled during preprocessing).  

---

## 🔍 Exploratory Data Analysis (EDA)

- **Correlation Heatmap** to identify relations among study hours, attendance, and exam scores.  
- **Missing Values Heatmap** to check data quality.  
- **Gender distribution** of students.  
- **Boxplots** for outlier detection (e.g., Hours Studied, Exam Scores).  
- **Countplots** to visualize score distributions by study hours and other factors.  

**Findings:**
- Higher study hours and better attendance strongly correlate with exam performance.  
- About **104 outliers** detected in `Exam_Score`.  

---

## ⚙️ Data Preparation

- **Binary encoding** for `Extracurricular_Activities`, `Internet_Access`, `Learning_Disabilities`.  
- **Ordinal encoding** for factors such as:
  - Motivation Level (`Low=0 → High=2`)  
  - Peer Influence (`Negative=-1, Neutral=0, Positive=1`)  
  - Family Income, Teacher Quality, Parental Education, etc.  
- **Feature Engineering**:
  - `study_sleep_ratio`, `parent_support_index`, `score_improvement`, `attendance_score`, `study_quality`, etc.  
- **One-Hot Encoding** for nominal variables (`School_Type`, `Gender`).  
- **Scaling** applied using `StandardScaler` on numerical columns.  

---

## 🧑‍💻 Models

### 1️⃣ Linear Regression


### 2️⃣ Polynomial Regression (degree=2)


### 3️⃣ Reduced Features (without derived ratios)


### 4️⃣ Cross-Validation (5-fold)


---

## 📈 Results

Both **Linear Regression** and **Polynomial Regression** achieved **perfect fit (R²=1.0)**.  
This suggests:
- Dataset is **highly deterministic** with engineered features.  
- Linear models are sufficient; complex models not needed.  

---

## 🛠️ Requirements

Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn kagglehub
