# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Project Overview

This project implements the **K-Means Clustering algorithm** to segment customers of a retail store based on their purchasing behavior.

Customers are grouped into different clusters based on:

* Annual Income
* Spending Score

The model is deployed using Streamlit to provide an interactive interface.

---

## 🎯 Objective

To group customers into distinct categories for better business understanding and targeted marketing.

---

## 📂 Dataset

Dataset used: *Mall Customer Segmentation Data*

File used:

* `Mall_Customers.csv`

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit

---

## 🧠 Machine Learning Model

* Algorithm: **K-Means Clustering**
* Number of Clusters: 5
* Features Used:

  * Annual Income (k$)
  * Spending Score (1–100)

---

## 📊 Methodology

### 1. Data Preprocessing

* Selected relevant features
* Removed unnecessary columns

### 2. Finding Optimal Clusters

* Used **Elbow Method** to determine optimal value of K

### 3. Model Training

* Applied K-Means clustering algorithm
* Assigned cluster labels to customers

### 4. Visualization

* Plotted clusters using scatter plot for clear segmentation

---

## 👥 Customer Segments Identified

* High Income - High Spending 💰
* High Income - Low Spending 🧠
* Low Income - High Spending 😅
* Low Income - Low Spending 🧍
* Average Customers 😐

---

## 💻 Streamlit App Features

* Interactive sliders for:

  * Annual Income
  * Spending Score
* Predicts customer segment in real-time
* Displays meaningful cluster labels instead of numbers

---

## 📸 Output Example

* Input: Income = 25k$, Score = 80
* Output: **Low Income - High Spending 😅**

---

## ▶️ How to Run Locally

```bash id="p9k4dd"
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Cloud** for public access.

---

## 📌 Conclusion

This project demonstrates how unsupervised learning (K-Means) can be used to analyze customer behavior and assist businesses in decision-making.

---

## 🙌 Author

Developed as part of Machine Learning Internship (SkillCraft Technology)
