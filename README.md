# Real-Time Credit Card Fraud Detection System

## Overview
This project implements a real-time credit card fraud detection system using machine learning. It leverages PySpark for data processing (though the current notebook primarily uses Pandas for initial steps), Scikit-learn for model training, and simulates a Kafka stream for real-time transaction processing. A Streamlit dashboard is also included for visualization and interaction.

## Components
-   **Python**: Core programming language.
-   **PySpark**: Used for setting up a SparkSession, intended for scalable data processing.
-   **Scikit-learn**: For building and evaluating the fraud detection model (RandomForestClassifier).
-   **Pandas**: For data loading, manipulation, and processing.
-   **Kafka-Python**: Simulated for streaming transaction data in a real-time environment.
-   **Streamlit**: For creating an interactive web dashboard to visualize data and make predictions.
-   **Matplotlib & Seaborn**: For data visualization (e.g., confusion matrix, distributions).

## Dataset
The project uses a `creditcard.csv` dataset, which contains anonymized credit card transaction data with features `V1` through `V28`, `Time`, `Amount`, and `Class` (0 for normal, 1 for fraud).

## Project Flow
1.  **Install Dependencies**: Installs necessary Python libraries like `pyspark`, `kafka-python`, `scikit-learn`, and `streamlit`.
2.  **Start Spark Session**: Initializes a SparkSession for distributed computing.
3.  **Load Dataset**: Reads the `creditcard.csv` into a Pandas DataFrame.
4.  **Train Fraud Detection Model**: 
    -   Handles missing values.
    -   Splits data into training and testing sets.
    -   Trains a `RandomForestClassifier`.
    -   Evaluates the model using a classification report.
    -   Saves the trained model as `fraud_model.pkl`.
5.  **Convert Data to Spark DataFrame**: Converts the Pandas DataFrame to a Spark DataFrame (for potential future Spark-based processing).
6.  **Evaluate Model**: Calculates and prints the accuracy score for both training and test sets.
7.  **Confusion Matrix**: Generates and displays a confusion matrix to visualize model performance.
8.  **Simulated Kafka Streaming**: A function `transaction_stream()` simulates a real-time stream of transactions from the dataset.
9.  **Real-Time Fraud Detection**: 
    -   Loads the saved `fraud_model.pkl`.
    -   Processes transactions from the simulated stream one by one.
    -   Predicts fraud for each transaction and prints an alert if fraud is detected.
10. **Store Results**: Saves detected fraudulent transactions into `fraud_results.csv`.
11. **Streamlit Dashboard**: 
    -   An `app.py` file is created for the Streamlit dashboard.
    -   Allows users to explore the dataset, view visualizations (fraud distribution, amount distribution), and make individual fraud predictions.

## How to Run
1.  **Execute Cells Sequentially**: Run all the code cells in the provided Jupyter/Colab notebook from top to bottom.
2.  **Start Streamlit Dashboard**: After executing all cells, navigate to the cell that installs `streamlit` and `pyngrok` (if using Colab) and the cell that creates `app.py`.
3.  **Run `app.py`**: A new cell to run the streamlit app needs to be added and executed. (This notebook only writes the `app.py` file).

## Expected Output
-   Printed output showing Spark session started.
-   Head of the loaded dataset.
-   Model training progress and evaluation metrics (classification report).
-   Confirmation of model saving (`fraud_model.pkl`).
-   Accuracy scores.
-   Confusion matrix plot.
-   Output for detected fraudulent transactions from the simulated stream.
-   A `fraud_results.csv` file containing details of detected fraudulent transactions.
-   A Streamlit web application running locally or exposed via a tunnel (e.g., ngrok).

## Dashboard Functionality
The Streamlit dashboard offers three main sections:
-   **Dataset Overview**: Displays the shape of the dataset, and the count of fraudulent vs. normal transactions.
-   **Visualizations**: Shows the distribution of fraud vs. non-fraud transactions and the distribution of transaction amounts.
-   **Fraud Prediction**: Allows users to input `Time` and `Amount` for a transaction and get an instant prediction (Fraud/Normal).
