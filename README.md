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
```

**Tech Stack**
* Python, Pandas, NumPy, Scikit-Learn, Streamlit, Google Colab

**How to Run the Web App Locally**
1. Clone this repository to your local machine.
2. Install the required Python dependencies by running: `pip install -r requirements.txt`
3. Download the `california_housing_compressed.joblib` file from the **Releases** section on the right side of this repository and place it in the root folder alongside `app.py`.
4. Run `streamlit run app.py` in your terminal.

**Common Troubleshooting (FAQ)**
* **Error: FileNotFoundError for the .joblib file:** Make sure you downloaded the model from the "Releases" section on the right side of this page and placed it in the exact same folder as your `app.py` script.
* **Error: "streamlit is not recognized":** Ensure you have installed the requirements using `pip install -r requirements.txt`. If it still fails, try running `python -m streamlit run app.py`.

---
**About the Author**
Category Head at Milkbasket with 24 years of retail industry experience. Specializing in Category Management, Merchandising, Business Head, Data Science, retail analytics, and Agentic AI. Alumnus of the Indian Institute of Foreign Trade (IIFT), Delhi, and the Indian Institute of Technology (IIT), Madras.
