# Customer Segmentation (Clustering)

This project applies **unsupervised learning** techniques to segment mall customers into distinct groups based on their **Annual Income** and **Spending Score**.  

Dataset source: [Customer Segmentation Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

---

## 📂 Project Workflow

- **Data Loading**
  - Downloaded via `kagglehub`.
  - Dataset: `Mall_Customers.csv` (200 rows, 5 columns).
  - No missing values, contains demographics and spending information.

- **Feature Selection**
  - Used `Annual Income (k$)` and `Spending Score (1-100)` for clustering.
  - Standardized using `StandardScaler`.

- **KMeans Clustering**
  - Optimal cluster number selected using:
    - **Elbow Method** (inertia)
    - **Silhouette Score**
  - Best value: **k = 5**.
  - Cluster centers plotted and analyzed.

- **Cluster Insights (KMeans Averages)**  

  | Cluster | Annual Income (k$) | Spending Score (1-100) | Segment Description |
  |---------|---------------------|-------------------------|---------------------|
  | 0       | ~55.3              | ~49.5                  | Average income & spending |
  | 1       | ~86.5              | ~82.1                  | High income, high spending |
  | 2       | ~25.7              | ~79.4                  | Low income, high spending |
  | 3       | ~88.2              | ~17.1                  | High income, low spending |
  | 4       | ~26.3              | ~20.9                  | Low income, low spending |

- **DBSCAN (Bonus)**
  - Applied DBSCAN clustering as an alternative.
  - Detected core clusters and noise (`-1` indicates outliers).

---

## 📊 Visualizations
- Elbow method curve for optimal K.
- Scatter plots of clusters (KMeans & DBSCAN) with color-coded groups.
- Cluster centers marked with `X`.

---

## ✅ Key Findings
- **KMeans (k=5)** gave clear and interpretable segments:
  - Luxury customers (high income, high spending).  
  - Budget-conscious customers (low income, low spending).  
  - High-spending low-income customers (potential for promotions).  
- **DBSCAN** identified clusters but was more sensitive to parameter settings.

---

## 🛠️ Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn kagglehub
