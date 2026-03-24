import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/data/titanic.csv")


features = ["pclass", "sex", "age", "fare"]


X = df[features].copy()
y = df["survived"]


X["sex"] = X["sex"].map({"male": 0, "female": 1})
X["age"] = X["age"].fillna(X["age"].median())
X["fare"] = X["fare"].fillna(X["fare"].median())


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train_scaled, y_train)


joblib.dump(model, "C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/models/logistic_model.pkl")
joblib.dump(scaler, "C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/models/scaler.pkl")


joblib.dump(features, "C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/models/features.pkl")

print("Model trained and saved successfully.")