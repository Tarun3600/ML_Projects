# Rock vs Mine Prediction using Logistic Regression

This project aims to classify sonar returns from rocks and mines using a Logistic Regression model. The dataset used contains sonar readings that help differentiate between rocks and metal cylinders (mines). The steps include data collection, preprocessing, model training, and evaluation.

## Project Overview

1. **Data Collection and Preprocessing**:
    - Import dependencies: numpy, pandas, sklearn
    - Load the dataset into a pandas DataFrame
    - Explore the dataset: check its shape, statistical measures, and class distribution
    - Separate features (X) and labels (Y)

2. **Data Splitting**:
    - Split the data into training and testing sets (90% training, 10% testing) with stratification to maintain class balance.

3. **Model Training**:
    - Use Logistic Regression to train the model with the training data.

4. **Model Evaluation**:
    - Evaluate the model’s accuracy on both training and testing data.

5. **Predictive System**:
    - Create a system to predict if a given sonar reading corresponds to a rock or a mine.

## Dependencies

- numpy
- pandas
- scikit-learn
