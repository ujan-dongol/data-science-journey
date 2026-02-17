
def transform_data(df):
    monthly_revenue = df.groupby("month")["revenue"].sum()
    product_revenue = df.groupby("product")["revenue"].sum()
    region_revenue = df.groupby("region")["revenue"].sum()
    
    return monthly_revenue, product_revenue, region_revenue