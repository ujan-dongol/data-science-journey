import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/data/titanic.csv")


x = df[["pclass", "sex", "age", "fare"]].copy()
y = df["survived"]


x.loc[:, "sex"] = x["sex"].map({"male": 0, "female": 1})


x["age"] = x["age"].fillna(x["age"].median())


scaler = StandardScaler()
X = scaler.fit_transform(x)


model = LogisticRegression()


scores = cross_val_score(model, X, y, cv=5)


print("Cross Validation Scores:", scores)
print("Average CV Score:", scores.mean())