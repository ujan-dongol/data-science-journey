import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Barplot
sns.barplot(x="day", y="total_bill", data=df)

plt.title("Average Bill per Day")
plt.show()

# Countplot
sns.countplot(x="day", data=df)

plt.title("Count of Records per Day")
plt.show()

# Boxplot
sns.boxplot(x="day", y="total_bill", data=df)

plt.title("Boxplot of Bills per Day")
plt.show()
