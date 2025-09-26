# 🌲 Forest Cover Type Classification

This project predicts the **type of forest cover** based on cartographic and environmental features using the **Covertype dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/covertype).

---

## 📂 Dataset

- **Source**: UCI Machine Learning Repository (Dataset ID = 31)  
- **Records**: 581,012  
- **Features**: 54  
  - 10 quantitative variables (e.g., Elevation, Aspect, Slope, etc.)  
  - 44 categorical variables (wilderness area & soil type, encoded as one-hot)  
- **Target**: 7 forest cover types (labeled 1–7)

---

## 🎯 Project Objectives

1. Load and preprocess the Covertype dataset.  
2. Perform **Exploratory Data Analysis (EDA)** with visualizations.  
3. Train and evaluate machine learning models for **multi-class classification**.  
4. Compare **Random Forest** and **XGBoost**.  
5. Perform **Hyperparameter Tuning** using GridSearchCV and RandomizedSearchCV.  
6. Visualize **confusion matrices** and **feature importance**.  

---

## 🛠 Tech Stack

- **Python**  
- **Libraries**:  
  - `pandas`, `numpy`, `matplotlib`, `seaborn` (data analysis & visualization)  
  - `scikit-learn` (ML models, preprocessing, tuning)  
  - `xgboost` (gradient boosting)  
  - `ucimlrepo` (dataset fetching)  

---

## 📊 Exploratory Data Analysis (EDA)

- **Class Distribution**: Checked balance of forest cover types.  
- **Boxplots**: Elevation vs. forest cover.  
- **Heatmap**: Correlation among numeric features.  
- **Wilderness & Soil Type distributions**.  
- **PCA (2D projection)** for visualization of separability between classes.  

---

## 🤖 Modeling

### Baseline
- **Random Forest** (200 trees) → ~95% accuracy.  
- **XGBoost** (200 trees, tuned depth & learning rate) → higher accuracy after tuning.  

### Hyperparameter Tuning
- **GridSearchCV**: Exhaustive search (slow on full dataset).  
- **RandomizedSearchCV**: Efficient random sampling (preferred for large dataset).  

### Metrics
- Accuracy score.  
- Classification report (precision, recall, F1-score).  
- Confusion matrix heatmap.  
- Feature importance visualization (top 20 features).  

---

## 📈 Results

| Model           | Accuracy (Test Set) |
|-----------------|----------------------|
| Random Forest   | ~95%                 |
| XGBoost         | ~96–97%              |

- **XGBoost** slightly outperforms Random Forest with tuned hyperparameters.  
- Elevation, Soil Type, and Wilderness Area are among the most important predictors.  

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/username/forest-cover-classification.git
   cd forest-cover-classification
