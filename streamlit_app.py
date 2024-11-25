import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Set Streamlit page config
st.set_page_config(page_title="Sample Streamlit App", layout="wide")

# Hide Streamlit branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Title
st.title("Simple Car Price Prediction App")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Select Page", ["Home", "Predict"])

# Sample data for demonstration
if page == "Home":
    st.subheader("Welcome to the Home Page!")
    st.markdown("""
    This is a simple example of a Streamlit app. Here's what you can do:
    - Navigate through pages using the sidebar.
    - Predict car prices based on user inputs.
    """)

if page == "Predict":
    st.subheader("Car Price Prediction")
    st.write("Fill out the details below to predict the car's selling price.")

    # Input fields for user data
    year = st.slider("Year of Purchase", 2000, 2023, 2015)
    km_driven = st.number_input("Kilometers Driven (in KM)", min_value=0, max_value=500000, value=10000)
    fuel_type = st.selectbox("Fuel Type", options=["Petrol", "Diesel", "CNG", "Electric"])
    
    # Feature transformation for demonstration
    fuel_mapping = {"Petrol": 0, "Diesel": 1, "CNG": 2, "Electric": 3}
    fuel_encoded = fuel_mapping[fuel_type]

    # Dummy data for regression (replace with your trained model later)
    X = np.array([[2010, 50000, 0], [2020, 10000, 1], [2015, 30000, 2], [2022, 15000, 3]])
    y = np.array([200000, 800000, 400000, 1000000])
    model = LinearRegression().fit(X, y)

    # Predict button
    if st.button("Predict Price"):
        input_data = np.array([[year, km_driven, fuel_encoded]])
        predicted_price = model.predict(input_data)[0]
        st.success(f"The predicted price for the car is: ₹{predicted_price:,.2f}")

# Footer
st.sidebar.info("Built with ❤️ using Streamlit.")
