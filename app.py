import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('kmeans_model.pkl', 'rb'))

st.title("🛍️ Customer Segmentation App")

st.write("Enter customer details:")

income = st.slider("Annual Income (k$)", 10, 150, 50)
score = st.slider("Spending Score (1-100)", 1, 100, 50)

if st.button("Predict Cluster"):
    data = np.array([[income, score]])
    cluster = model.predict(data)

    st.success(f"Customer belongs to Cluster: {cluster[0]}")
