import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day26_Model_Evaluation/data/titanic.csv")

# Select features and target
x = df[["pclass", "sex", "age", "fare"]].copy()
y = df["survived"]

# Convert categorical to numeric
x.loc[:, "sex"] = x["sex"].map({"male": 0, "female": 1})

# Fill missing values (FIXED LINE)
x["age"] = x["age"].fillna(x["age"].median())

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(x)

# Model
model = LogisticRegression()

# Cross-validation
scores = cross_val_score(model, X, y, cv=5)

# Output
print("Cross Validation Scores:", scores)
print("Average CV Score:", scores.mean())