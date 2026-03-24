import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score


model = joblib.load("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/models/logistic_model.pkl")
scaler = joblib.load("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/models/scaler.pkl")


df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/data/titanic.csv")


features = ["pclass", "sex", "age", "fare"]

X = df[features].copy()
y = df["survived"]


X["sex"] = X["sex"].map({"male": 0, "female": 1})
X["age"] = X["age"].fillna(X["age"].median())
X["fare"] = X["fare"].fillna(X["fare"].median())

# Scale features
X_scaled = scaler.transform(X)

# Predict probabilities
y_prob = model.predict_proba(X_scaled)[:, 1]

# ROC Curve
fpr, tpr, thresholds = roc_curve(y, y_prob)

plt.figure()
plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/outputs/roc_curve.png")

# AUC Score
auc = roc_auc_score(y, y_prob)
print("AUC Score:", auc)