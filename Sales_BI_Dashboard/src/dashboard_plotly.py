import matplotlib.pyplot as plt

def create_dashboard(monthly, product, region, df):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    axes[0, 0].plot(monthly.index, monthly.values)
    axes[0, 0].set_title("Monthly Revenue Trend")
    axes[0, 0].set_xlabel("Month")
    axes[0, 0].set_ylabel("Revenue")

    axes[0, 1].bar(product.index, product.values)
    axes[0, 1].set_title("Revenue by Product")

    axes[1, 0].bar(region.index, region.values)
    axes[1, 0].set_title("Revenue by Region")

    axes[1, 1].hist(df["revenue"], bins=5)
    axes[1, 1].set_title("Revenue Distribution")

    plt.tight_layout()
    plt.savefig("outputs/sales_dashboard.png")
    plt.show()
