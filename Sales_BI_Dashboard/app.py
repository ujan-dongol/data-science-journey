import streamlit as st
from src.loader import load_data
from src.transformer import transform_data
from src.kpi import calculate_kpis

st.title("Sales BI Dashboard")

df = load_data("data/sales_data.csv")

monthly, product, region = transform_data(df)
kpis = calculate_kpis(df)

st.subheader("KPIs")
for key, value in kpis.items():
    st.write(f"**{key}**: {value}")

st.line_chart(monthly)
st.bar_chart(product)
st.bar_chart(region)
