import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_curve,
    roc_auc_score
)

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler



df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/data/titanic.csv")

X = df[["pclass", "sex", "age", "fare"]].copy()
y = df["survived"]

X["sex"] = X["sex"].map({"male": 0, "female": 1})
X["age"] = X["age"].fillna(X["age"].median())



model = joblib.load("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/models/logistic_model.pkl")
scaler = joblib.load("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/models/scaler.pkl")



X_scaled = scaler.transform(X)



y_pred = model.predict(X_scaled)
y_prob = model.predict_proba(X_scaled)[:, 1]



cm = confusion_matrix(y, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/outputs/confusion_matrix.png")
plt.close()


fpr, tpr, thresholds = roc_curve(y, y_prob)
auc_score = roc_auc_score(y, y_prob)

plt.figure()
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1])
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/outputs/mini_roc_curve.png")
plt.close()



scaler_cv = StandardScaler()
X_cv = scaler_cv.fit_transform(X)

model_cv = LogisticRegression()
cv_scores = cross_val_score(model_cv, X_cv, y, cv=5)


report_text = classification_report(y, y_pred)

with open("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/outputs/evaluation_report.txt", "w") as f:
    f.write("Titanic Model Evaluation Report\n")
    f.write("--------------------------------\n\n")
    f.write("Classification Report:\n")
    f.write(report_text)
    f.write("\n\nAUC Score: " + str(auc_score))
    f.write("\n\nCross Validation Scores: " + str(cv_scores))
    f.write("\nAverage CV Score: " + str(cv_scores.mean()))

print("Performance report generated successfully.")