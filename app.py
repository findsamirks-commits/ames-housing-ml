import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="California Housing Predictor", page_icon="🏠", layout="centered")

st.title("🏠 California Housing Price Predictor")
st.write("Adjust the property details below to get an estimated house value.")

# Load the trained, compressed model
@st.cache_resource
def load_saved_model():
    return joblib.load('california_housing_compressed.joblib')

model = load_saved_model()

st.subheader("Property Characteristics")

col1, col2 = st.columns(2)

with col1:
    median_income = st.number_input("Median Income (in $10,000s)", min_value=0.5, max_value=15.0, value=8.32, step=0.1)
    housing_median_age = st.slider("House Median Age (Years)", min_value=1, max_value=52, value=41)
    total_rooms = st.number_input("Total Rooms in Block", min_value=10, max_value=40000, value=880, step=10)
    total_bedrooms = st.number_input("Total Bedrooms in Block", min_value=5, max_value=7000, value=129, step=5)

with col2:
    population = st.number_input("Block Population", min_value=10, max_value=35000, value=322, step=10)
    households = st.number_input("Total Households", min_value=5, max_value=10000, value=126, step=5)
    latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, value=37.88, step=0.01)
    longitude = st.number_input("Longitude", min_value=-125.0, max_value=-114.0, value=-122.23, step=0.01)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
)

input_df = pd.DataFrame([{
    'longitude': longitude,
    'latitude': latitude,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'median_income': median_income,
    'ocean_proximity_INLAND': 1 if ocean_proximity == 'INLAND' else 0,
    'ocean_proximity_ISLAND': 1 if ocean_proximity == 'ISLAND' else 0,
    'ocean_proximity_NEAR BAY': 1 if ocean_proximity == 'NEAR BAY' else 0,
    'ocean_proximity_NEAR OCEAN': 1 if ocean_proximity == 'NEAR OCEAN' else 0
}])

st.markdown("---")

if st.button("Predict House Value", type="primary"):
    prediction = model.predict(input_df)[0]
    st.success(f"### Estimated Property Value: **${prediction:,.2f}**")
