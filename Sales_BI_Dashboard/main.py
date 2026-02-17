from src.loader import load_data
from src.transformer import transform_data
from src.kpi import calculate_kpis
from src.dashboard_matplotlib import create_dashboard

def main():
    df = load_data("data/sales_data.csv")

    monthly, product, region = transform_data(df)

    kpis = calculate_kpis(df)

    print("===== KPI SUMMARY =====")
    for key, value in kpis.items():
        print(f"{key}: {value}")

    create_dashboard(monthly, product, region, df)

if __name__ == "__main__":
    main()