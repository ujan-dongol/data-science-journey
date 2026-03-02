import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib 
import os

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day25_Logistic_regression/data/titanics.csv")

df = df[["survived", "pclass", "sex", "age", "fare"]]

df["sex"] = df["sex"].map({"male": 0, "female":1})

df["age"].fillna(df["age"].median(), inplace=True)

X = df.drop("survived", axis= 1)
y = df["survived"]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

os.makedirs("C:/Users/Asus/Desktop/datascience/Day25_Logistic_regression/models", exist_ok=True)

joblib.dump(model, "C:/Users/Asus/Desktop/datascience/Day25_Logistic_regression/models/logistic_model.pkl")
joblib.dump(scaler, "C:/Users/Asus/Desktop/datascience/Day25_Logistic_regression/models/scaler.pkl")
print("Model and scaler saved in models folder!")