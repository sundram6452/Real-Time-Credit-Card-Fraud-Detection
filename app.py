
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.title("💳 Credit Card Fraud Detection Dashboard")

# Load data
data = pd.read_csv("creditcard.csv")

# Load model
model = joblib.load("fraud_model.pkl")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Menu",
    ["Dataset Overview", "Visualizations", "Fraud Prediction"]
)

# Dataset Overview
if menu == "Dataset Overview":
    st.subheader("Dataset Overview")

    st.write("Dataset Shape:", data.shape)
    st.dataframe(data.head())

    fraud = data[data["Class"]==1].shape[0]
    normal = data[data["Class"]==0].shape[0]

    st.metric("Fraud Transactions", fraud)
    st.metric("Normal Transactions", normal)

# Visualization
elif menu == "Visualizations":
    st.subheader("Fraud vs Non-Fraud Distribution")

    fig, ax = plt.subplots()
    sns.countplot(x="Class", data=data, ax=ax)
    st.pyplot(fig)

    st.subheader("Transaction Amount Distribution")

    fig2, ax2 = plt.subplots()
    sns.histplot(data["Amount"], bins=50, ax=ax2)
    st.pyplot(fig2)

# Fraud Prediction
elif menu == "Fraud Prediction":

    st.subheader("Predict Transaction")

    time = st.number_input("Transaction Time")
    amount = st.number_input("Transaction Amount")

    if st.button("Predict"):

        prediction = model.predict([[time, amount]])

        if prediction[0] == 1:
            st.error("⚠ Fraud Transaction Detected")
        else:
            st.success("✅ Normal Transaction")
