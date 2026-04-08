import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('kmeans_model.pkl', 'rb'))

# Cluster Labels (based on your analysis)
cluster_labels = {
    0: "Average Customers 😐",
    1: "High Income - High Spending 💰",
    2: "Low Income - High Spending 😅",
    3: "High Income - Low Spending 🧠",
    4: "Low Income - Low Spending 🧍"
}

# Title
st.title("🛍️ Customer Segmentation App")

st.write("Enter customer details:")

# Inputs
income = st.slider("Annual Income (k$)", 10, 150, 50)
score = st.slider("Spending Score (1-100)", 1, 100, 50)

# Prediction
if st.button("Predict Cluster"):
    data = np.array([[income, score]])
    cluster = model.predict(data)

    st.success(f"Customer belongs to: {cluster_labels[cluster[0]]}")
