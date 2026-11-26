\# Flower Prediction Using Machine Learning



\## 1. Project Overview

This project predicts the species of an Iris flower using machine learning and a Streamlit web application.



\## 2. Dataset

The project uses the Iris dataset from Scikit-learn.



It contains three flower species:

\- Setosa

\- Versicolor

\- Virginica



Input features:

\- Sepal length

\- Sepal width

\- Petal length

\- Petal width



\## 3. Data Cleaning

\- Checked for missing values.

\- Identified and removed one duplicate record.

\- Detected possible outliers using a boxplot.

\- Retained possible outliers because they may be valid flower measurements.



\## 4. Exploratory Data Analysis

Used Matplotlib and Seaborn to create:

\- Flower count plot

\- Petal length histogram

\- Correlation heatmap

\- Outlier boxplot



\## 5. Feature Importance

Random Forest feature importance results:

\- Petal width: 45.10%

\- Petal length: 40.06%

\- Sepal length: 11.99%

\- Sepal width: 2.86%



All four features were retained.



\## 6. Model Development

Models trained:

\- Decision Tree Classifier

\- Random Forest Classifier



The data was split into 80% training and 20% testing data.



\## 7. Model Tuning and Evaluation

GridSearchCV selected these Random Forest settings:

\- Number of trees: 50

\- Maximum depth: None



Grid search cross-validation accuracy: 95%



Final test accuracy: 90%



The classification report also includes precision, recall and F1-score.



\## 8. Streamlit Application

The app accepts four flower measurements and predicts the flower species.



\## 9. Technologies

\- Python

\- Pandas

\- Scikit-learn

\- Matplotlib

\- Seaborn

\- Streamlit

\- Joblib

\- Jupyter Notebook

\- Git and GitHub



\## 10. How to Run



Install the required libraries:



```bash

pip install streamlit pandas scikit-learn matplotlib seaborn joblib

```



Run the application from the project folder:



```bash

streamlit run app.py

```



Open http://localhost:8501 in your browser.

