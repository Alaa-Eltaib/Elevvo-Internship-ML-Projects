# 🌲 Forest Cover Type Classification (UCI Covertype Dataset)

This project applies **supervised machine learning** techniques to classify forest cover types using the **UCI Covertype dataset**.  
It compares **Random Forest** and **XGBoost** classifiers in terms of accuracy and feature importance.

---

## 📂 Dataset
- **Source**: [UCI Machine Learning Repository - Covertype Dataset](https://archive.ics.uci.edu/dataset/31/covertype)  
- **Size**: 581,012 instances, 54 features, 1 target column.  
- **Target**: `Cover_Type` (7 classes representing forest types).  
- **Features**:  
  - Numerical (e.g., Elevation, Aspect, Slope, Distances, Hillshade).  
  - Categorical (binary indicators for 4 wilderness areas & 40 soil types).  
- **No missing values**.

---

## 📊 Exploratory Data Analysis (EDA)
- **Target distribution**: Imbalanced but covers all 7 classes.  
- **Elevation** is a strong discriminator between cover types.  
- **Soil type & wilderness area** provide categorical insights.  
- PCA projection shows partial separation of classes.  

Visualizations included:
- Class distribution plot.  
- Boxplot of Elevation vs Cover Type.  
- Correlation heatmap.  
- Wilderness and Soil type distributions.  
- PCA 2D scatter plot.  

---

## ⚙️ Preprocessing
- Train-test split: **80/20 stratified split**.  
- Standard scaling applied to numeric features.  
- Target label encoded for XGBoost.  

---

## 🧑‍💻 Models

### 🔹 Random Forest
- `n_estimators=200`, `random_state=42`.  
- Accuracy: **95.4%**  
- Strong performance across all classes.  
- Top features: **Elevation, Horizontal Distance to Roadways, Hillshade, Soil Types**.  

### 🔹 XGBoost
- `n_estimators=200`, `max_depth=8`, `learning_rate=0.1`, `subsample=0.8`, `colsample_bytree=0.8`.  
- Accuracy: **89.6%**  
- Performed worse than Random Forest without hyperparameter tuning.  

---

## 📈 Results Summary

| Model          | Accuracy | Notes |
|----------------|----------|-------|
| Random Forest  | **95.4%** | Best performance, robust across all classes |
| XGBoost        | 89.6%    | Underperformed, needs tuning |

---

## 🛠️ Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost ucimlrepo
