# Day 25 – Titanic Logistic Regression Model Training & Evaluation with Mini ML Web Application

---

### Overview

This project focuses on training and evaluating a Logistic Regression model using the preprocessed Titanic dataset.

After completing data preprocessing and feature engineering (Day 24), this phase involves building a predictive model and analyzing its performance using standard evaluation techniques.

---

### Objectives

- Perform train-test split  
- Apply feature scaling  
- Train Logistic Regression model  
- Generate predictions  
- Evaluate model performance  
- Visualize confusion matrix  
- Save trained model and scaler  

---

### Tools Used

- Python  
- Pandas  
- Scikit-Learn  
- Matplotlib  
- Seaborn  
- Joblib  

---

### Techniques Applied

- Train-Test Split (80% training, 20% testing)  
- StandardScaler (Feature Scaling)  
- Logistic Regression (Binary Classification)  
- Accuracy Score Evaluation  
- Classification Report Analysis  
- Confusion Matrix Visualization  
- Model Saving using `.pkl` files  

---

### Why This Matters

Proper model training and evaluation:

- Converts processed data into predictions  
- Measures real-world performance  
- Helps identify model strengths and weaknesses  
- Prevents overfitting  
- Enables reuse of trained models without retraining  

---

### Key Concepts

- Supervised Learning  
- Binary Classification  
- Sigmoid Function  
- Probability Threshold (0.5)  
- Precision, Recall, F1-Score  
- Confusion Matrix (TP, FP, TN, FN)  

---

### Interview Highlights

- Explain Logistic Regression clearly  
- Why feature scaling is required  
- Difference between classification and regression  
- How to interpret confusion matrix  
- Difference between precision and recall  
- Why use joblib for saving models  
- Importance of train-test split  

---

### Mini Project: Interactive ML Web Application

To make the model usable, a lightweight web application was developed.

### Features

- User inputs passenger details
- Inputs are automatically
- Encoded
- Scaled
Model predicts survival instantly
Result displayed in user-friendly format

### Run the Application
- streamlit run app.py
- The browser will open automatically.
- This demonstrates real-world ML deployment workflow.

### Conclusion

This project demonstrates how to train, evaluate, and save a machine learning classification model.

It forms a strong foundation for real-world machine learning workflows and model deployment.

---
