```markdown
# Day 20 – Statistical Data Visualization with Seaborn

## Overview

This project is part of my Data Science learning journey.

On Day 20, I explored **Seaborn**, a powerful statistical visualization library in Python built on top of Matplotlib. The focus of this session was to understand data distributions, categorical comparisons, and statistical insights using real-world data.

The project demonstrates how visualization helps transform raw data into meaningful business insights.

---

# Technologies Used

- Python 3.x
- Seaborn
- Matplotlib
- Pandas

#  Dataset Used

We used Seaborn's built-in **Tips Dataset**:
```python
import seaborn as sns
df = sns.load_dataset("tips")
````
### Dataset Features:

| Column     | Description           |
| ---------- | --------------------- |
| total_bill | Total restaurant bill |
| tip        | Tip amount            |
| sex        | Customer gender       |
| smoker     | Smoking status        |
| day        | Day of visit          |
| time       | Lunch or Dinner       |
| size       | Number of people      |

---

#  Visualizations Implemented

## 1️⃣ Bar Plot – Average Bill per Day

```python
sns.barplot(x="day", y="total_bill", data=df)
```

🔎 Purpose:

* Shows average total bill for each day.
* Helps identify high revenue days.

---

## 2️⃣ Count Plot – Customer Frequency

```python
sns.countplot(x="day", data=df)
```

🔎 Purpose:

* Shows number of transactions per day.
* Identifies busiest days.

---

## 3️⃣ Box Plot – Bill Distribution by Day

```python
sns.boxplot(x="day", y="total_bill", data=df)
```

- Shows:

* Median
* Quartiles
* Interquartile Range (IQR)
* Outliers

- Insight:

* Detects spending variability.
* Identifies extreme customer bills.

---

## 4️⃣ Histogram with KDE – Distribution Analysis

```python
sns.histplot(df["total_bill"], kde=True)
```

- Observation:

* Most bills are between 10–25.
* The distribution is **Right Skewed**.
* Few high-value outliers exist.

---

## 5️⃣ KDE Plot – Smooth Density Curve

```python
sns.kdeplot(df["total_bill"], fill=True)
```

 Purpose:

* Shows overall spending pattern.
* Helps understand probability density.

---

#  Statistical Concepts Learned

* Distribution
* Skewness
* Outliers
* Central Tendency
* Categorical Comparison
* Data Interpretation

---

#  Key Insights from Analysis

* Majority of restaurant bills are lower values.
* Few customers generate significantly higher bills.
* Weekend days show more variability.
* Distribution of total_bill is right skewed.

---

#  Mini Project: Sales Analytics System

Alongside learning Seaborn, I am building a **Sales Analytics System** as a mini Data Science project.

### Project Highlights:

* FastAPI Backend
* Database integration
* Sales data analysis
* API-based architecture
* Data visualization modules
* Modular project structure

This visualization practice strengthens the analytics component of my Sales Analytics System by helping interpret sales trends, distributions, and revenue patterns effectively.

---

#  Learning Outcome

After completing this project, I can:

* Create professional statistical visualizations
* Interpret skewness and distribution patterns
* Identify business insights from raw data
* Apply visualization techniques in real-world analytics projects
* Integrate visualization knowledge into backend-driven systems

---

#  Future Improvements

* Correlation heatmap
* Pairplot for multi-variable analysis
* Revenue trend visualization
* Integration with real sales dataset

---

#  Conclusion

Day 20 significantly improved my understanding of:

* Statistical thinking
* Visual storytelling
* Business-driven data interpretation

This forms a strong foundation for:

* Data Analytics
* Machine Learning
* Business Intelligence
* Production-level Data Science Projects

---

## 📌 Author

Ujan Dongol
Aspiring Data Scientist | Backend Developer | Analytics Enthusiast

```

---

