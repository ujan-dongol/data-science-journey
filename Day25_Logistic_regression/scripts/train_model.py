import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day25_Logistic_regression/data/titanics.csv")
print("Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

# Select Important Features
df = df[["survived", "pclass", "sex", "age", "fare"]]

# Convert categorical to numeric
df["sex"] = df["sex"].map({"male": 0, "female": 1})
print(df.columns)
# Fill missing Age values
df["age"].fillna(df["age"].median(), inplace=True)


#  Define X and y
X = df.drop("survived", axis=1)
y = df["survived"]

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day25_Logistic_regression/outputs/confusion matrix.png")
plt.show()