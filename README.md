# Loan-Prediction-MLOPS


## Overview
This repository contains a complete end-to-end Loan Prediction project that utilizes machine learning models for predicting loan approval. The project incorporates MLOps practices to ensure reproducibility, model tracking, and streamlined deployment. The deployed application is available : https://loan-prediction-mlops.streamlit.app 

The project aims to predict loan approval based on user inputs. It utilizes several machine learning models, compares their performance, and promotes the best-performing model to production using MLflow. A Streamlit-based web application allows users to interact with the model and make predictions.



## Features

Machine Learning Models:  Logistic Regression  / Random Forest  / Support Vector Classifier

MLOps Integration:
- Model tracking and comparison with MLflow.

- Promotion of the best model to the production stage.

Web Application:

- User-friendly interface built with Streamlit.

- Deployed online for easy access.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/AsmaCherifa/Loan-Prediction-MLOPS.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Loan_prediction
    ```

3. Create a virtual environment and install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit Application:

  ```bash
    mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns
    ```
