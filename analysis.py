import pandas as pd
import json

df = pd.read_csv("data/data.csv", encoding="latin1")

# Clean
df = df.dropna(subset=["CustomerID"])
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df[df["Quantity"] > 0]
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# Monthly revenue & orders
monthly = df.groupby("YearMonth").agg(
    Revenue=("Revenue", "sum"),
    Orders=("InvoiceNo", "nunique")
).reset_index()

# Top 10 products
top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
top_products["Revenue"] = top_products["Revenue"].round(2)

# Top 10 countries
top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
top_countries["Revenue"] = top_countries["Revenue"].round(2)

# KPIs
kpis = {
    "total_revenue": round(df["Revenue"].sum(), 2),
    "total_orders": int(df["InvoiceNo"].nunique()),
    "avg_order_value": round(df.groupby("InvoiceNo")["Revenue"].sum().mean(), 2),
    "peak_month": monthly.loc[monthly["Revenue"].idxmax(), "YearMonth"],
    "total_countries": int(df["Country"].nunique()),
    "total_products": int(df["Description"].nunique()),
}

out = {
    "kpis": kpis,
    "monthly": monthly.to_dict(orient="records"),
    "top_products": top_products.to_dict(orient="records"),
    "top_countries": top_countries.to_dict(orient="records"),
}

with open("data/dashboard_data.json", "w") as f:
    json.dump(out, f, indent=2)

print("Analysis complete. data/dashboard_data.json generated.")
print(f"  Total Revenue : £{kpis['total_revenue']:,.2f}")
print(f"  Total Orders  : {kpis['total_orders']:,}")
print(f"  Avg Order Val : £{kpis['avg_order_value']:,.2f}")
print(f"  Peak Month    : {kpis['peak_month']}")
