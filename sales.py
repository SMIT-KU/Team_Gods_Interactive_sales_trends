import pandas as pd
import matplotlib.pyplot as plt


# Load data
data = pd.read_csv("sales_data.csv")
data['Date'] = pd.to_datetime(data['Date'])

# Sales trends over time
def plot_sales_trends(data):
    sales_trends = data.groupby('Date')['Sales'].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(sales_trends.index, sales_trends.values, marker='o', color='blue')
    plt.title("Sales Trends Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.grid(True)
    plt.savefig("sales_trends.png")
    plt.show()

# Regional sales breakdown
def plot_sales_by_region(data):
    regional_sales = data.groupby('Region')['Sales'].sum()
    regions = regional_sales.index
    sales = regional_sales.values
    plt.figure(figsize=(7, 5))
    plt.bar(regions, sales, color='green')
    plt.title("Sales by Region", fontsize=16)
    plt.xlabel("Region", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.savefig("sales_by_region.png")
    plt.show()

# Product sales breakdown
def plot_sales_by_product(data):
    product_sales = data.groupby('Product')['Sales'].sum()
    products = product_sales.index
    sales = product_sales.values
    plt.figure(figsize=(7, 5))
    plt.bar(products, sales, color='orange')
    plt.title("Sales by Product", fontsize=16)
    plt.xlabel("Product", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.savefig("sales_by_product.png")
    plt.show()

# Run the analysis
plot_sales_trends(data)
plot_sales_by_region(data)
plot_sales_by_product(data)
