import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Histogram with KDE
sns.histplot(df["total_bill"], kde=True)

plt.title("Distribution of Total Bill")
plt.show()

# KDE Plot
sns.kdeplot(df["total_bill"], fill= True)

plt.title("KDE Plot of Total Bill")
plt.show()
