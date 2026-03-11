# Insurance Prediction

A machine learning web application that predicts the **Annual Insurance Premium** (in thousands) for a customer based on key personal and policy details. Built with a Linear Regression model and served through an interactive Streamlit UI.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Pipeline](#pipeline)

---

## Overview

This project predicts the annual insurance premium a customer is expected to pay, given the following inputs:

| Input Feature | Description |
|---|---|
| **Age** | Age of the customer (years) |
| **Annual Income (LPA)** | Customer's yearly income in Lakhs Per Annum |
| **Policy Term (Years)** | Duration of the insurance policy in years |
| **Sum Assured (Lakhs)** | Total coverage amount in Lakhs |

The model outputs the **predicted Annual Premium in Thousands**.

---

## Features

- End-to-end ML pipeline: data preprocessing → feature engineering → model training → prediction
- Interactive web interface powered by **Streamlit**
- Pre-trained **Linear Regression** model with **Standard Scaler** for feature normalization
- Modular source code organized in the `src/` package

---

## Tech Stack

- **Python 3.x**
- [scikit-learn](https://scikit-learn.org/) – model training & preprocessing
- [pandas](https://pandas.pydata.org/) – data manipulation
- [Streamlit](https://streamlit.io/) – web application UI
- [pickle](https://docs.python.org/3/library/pickle.html) – model serialization

---

## Dataset

The raw dataset is stored at `Data/raw/insurance.csv` and contains the following columns:

| Column | Description |
|---|---|
| `Customer_ID` | Unique customer identifier |
| `Age` | Customer age |
| `Annual_Income_LPA` | Annual income in Lakhs Per Annum |
| `Policy_Term_Years` | Policy term in years |
| `Sum_Assured_Lakhs` | Sum assured in Lakhs |
| `Annual_Premium_Thousands` | **Target variable** – annual premium in thousands |

---

## Project Structure

```
Insurance-prediction/
├── Data/
│   ├── raw/
│   │   └── insurance.csv          # Raw dataset
│   └── processed/                 # Scaled train/test splits (generated)
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
├── artifacts/
│   ├── model.pkl                  # Trained Linear Regression model
│   └── standard_scaler.pkl        # Fitted StandardScaler
├── src/
│   ├── datapreprocess.py          # Loads and splits the raw dataset
│   ├── featureeng.py              # Scales features and saves processed data
│   ├── modeltraining.py           # Trains the model and saves it
│   └── prediction.py              # Prediction class used by the app
├── app.py                         # Streamlit web application
└── README.md
```

---

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kranthikumar06/Insurance-prediction.git
   cd Insurance-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the pipeline** (only needed if you want to retrain the model)
   ```bash
   cd src
   python featureeng.py      # Preprocess and scale data
   python modeltraining.py   # Train and save the model
   ```

---

## Usage

Start the Streamlit web application:

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`, enter the customer details, and click **Predict** to see the estimated annual premium.

For Streamlit Community Cloud deployments, use a supported Python version such as **3.12** in the app's **Advanced settings**. Python 3.14 can break older Streamlit builds because some standard-library modules were removed.

---

## Pipeline

```
Raw Data (insurance.csv)
        │
        ▼
 datapreprocess.py  →  Train/Test Split
        │
        ▼
  featureeng.py     →  StandardScaler fit/transform  →  Processed CSVs + standard_scaler.pkl
        │
        ▼
 modeltraining.py   →  LinearRegression fit          →  model.pkl
        │
        ▼
   prediction.py    →  Load model & scaler, transform input, predict
        │
        ▼
     app.py         →  Streamlit UI
```
