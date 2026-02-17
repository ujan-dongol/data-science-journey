
def calculate_kpis(df):
    total_revenue = df["revenue"].sum()
    total_quantity = df["quantity"].sum()
    avg_revenue = df["revenue"].mean()
    
    best_product = df.groupby("product")["revenue"].sum().idxmax()
    best_region = df.groupby("region")["region"].sum().idxmax() 
    
    return {
        "Total Revenue": total_revenue,
        "Total Quantity": total_quantity,
        "Average Revenue": avg_revenue,
        "Best Product": best_product,
        "Best Region": best_region
    }      