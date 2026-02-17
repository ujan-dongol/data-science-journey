import matplotlib.pyplot as plt

def create_dashboard(monthly, product, region, df):

    plt.style.use("seaborn-v0_8")

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Monthly Trend
    axes[0, 0].plot(monthly.index, monthly.values, marker='o')
    axes[0, 0].set_title("Monthly Revenue Trend")
    axes[0, 0].grid(True)

    # Annotate highest month
    max_month = monthly.idxmax()
    max_value = monthly.max()
    axes[0, 0].annotate(f"Peak: {max_value}",
                        xy=(max_month, max_value),
                        xytext=(0,10),
                        textcoords="offset points")

    # Product Performance
    axes[0, 1].bar(product.index, product.values)
    axes[0, 1].set_title("Revenue by Product")

    # Region Performance
    axes[1, 0].bar(region.index, region.values)
    axes[1, 0].set_title("Revenue by Region")

    # Distribution
    axes[1, 1].hist(df["revenue"], bins=5)
    axes[1, 1].set_title("Revenue Distribution")

    plt.tight_layout()
    plt.savefig("outputs/sales_dashboard.png")
    plt.show()
    