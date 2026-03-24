# Day 26 – Titanic Model Evaluation & Performance Reporting System

---

### Overview

This project implements a complete Machine Learning evaluation pipeline using the Titanic dataset.

It focuses on model validation, performance analysis, and automated reporting, simulating a real-world ML workflow where evaluation is as important as model building.

---

### Objective

- Evaluate classification model performance using statistical metrics  
- Visualize model behavior and prediction quality  
- Validate model stability using cross-validation  
- Generate structured and automated performance reports  

---

### Key Concepts Implemented

#### Confusion Matrix
- True Positive (TP)  
- True Negative (TN)  
- False Positive (FP)  
- False Negative (FN)  

#### Classification Metrics
- Precision → Accuracy of positive predictions  
- Recall → Detection of actual positives  
- F1-score → Balance between precision and recall  

#### ROC Curve
- Plots True Positive Rate (TPR) vs False Positive Rate (FPR)  
- Evaluates performance across thresholds  

#### AUC Score
- Measures model’s ability to distinguish classes  
- 0.5 → Random model  
- 1.0 → Perfect model  

#### K-Fold Cross Validation
- Splits data into multiple folds  
- Reduces variance and bias  
- Provides reliable performance estimation  

---


---

### Workflow

#### Model Training
- Load dataset  
- Handle missing values  
- Encode categorical variables  
- Scale features  
- Train Logistic Regression model  
- Save model using joblib  

#### Performance Evaluation
- Generate predictions  
- Compute confusion matrix  
- Generate classification report  
- Plot ROC curve and calculate AUC score  

#### Cross Validation
- Apply 5-Fold Cross Validation  
- Calculate average performance score  

#### Report Generation
- Generate visual plots  
- Create text-based evaluation summary  

---

### How to Run

#### Step 1: Install Dependencies
pip install -r requirements.txt


### Outputs Generated
- confusion_matrix.png → Classification performance visualization
- roc_curve.png → Model discrimination capability
- evaluation_report.txt → Detailed evaluation summary

### Why This Project Matters
- Demonstrates strong understanding of ML evaluation metrics
- Shows ability to validate model performance
- Reflects real-world ML workflow practices
-Highlights structured pipeline development

#### Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
### Key Learning Outcomes
- Understanding of classification metrics
- Ability to interpret confusion matrix and ROC curve
- Knowledge of model validation techniques
- Experience with automated reporting systems

### Future Enhancements
- Hyperparameter tuning
- Model comparison (Random Forest, XGBoost)
- Precision-Recall curve analysis
- Dashboard visualization
- Real-time monitoring integration