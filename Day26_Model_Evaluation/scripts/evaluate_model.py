
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix


df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/data/titanic.csv")


X = df[["pclass", "sex", "age", "fare"]].copy()
y = df["survived"]


X.loc[:, "sex"] = X["sex"].map({"male": 0, "female": 1})


X["age"] = X["age"].fillna(X["age"].median())


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)



model = LogisticRegression()
model.fit(X_train, y_train)



y_pred = model.predict(X_test)



print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nPerformance report generated successfully.")