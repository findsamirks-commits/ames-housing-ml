# 🏠 California Housing Price Prediction Pipeline

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/findsamirks-commits/ames-housing-ml/blob/main/ames_housing_eda_and_model.ipynb)

An end-to-end machine learning project designed to predict California housing prices based on district-level demographic and geographical data. This repository contains the complete workflow, from initial data exploration to a live, interactive web application.

**Project Highlights**
* **Exploratory Data Analysis (EDA):** In-depth feature visualization, correlation mapping, and missing value handling.
* **Model Training & Tuning:** Optimized predictive modeling using Scikit-Learn, including hyperparameter tuning to maximize accuracy.
* **Interactive Web Application:** A live frontend interface built with Streamlit, allowing users to input custom property metrics for real-time price estimations.

**Project Workflow**
```mermaid
graph TD;
    A[Raw Housing Data CSV] -->|Pandas| B(Exploratory Data Analysis)
    B -->|Scikit-Learn| C(Model Training & Tuning)
    C -->|Joblib| D[(Compressed .joblib Model)]
    D -->|Streamlit| E[Interactive Web Application]


