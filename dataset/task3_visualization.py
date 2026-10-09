
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create output folder
os.makedirs("output", exist_ok=True)

# Load dataset
df = pd.read_csv("dataset/sales_data.csv")

# Display dataset
print("FIRST FIVE ROWS")
print(df.head())

print("\nDATASET INFORMATION")
df.info()

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Calculate total sales and profit
print("\nTOTAL SALES:", df["Sales"].sum())
print("TOTAL PROFIT:", df["Profit"].sum())

# Set chart style
sns.set_theme(style="whitegrid")

# Chart 1: Sales by category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar", color="steelblue")
plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/1_category_sales.png", dpi=300)
plt.close()

# Chart 2: Sales by region
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales Distribution by Region")
plt.tight_layout()
plt.savefig("output/2_region_sales.png", dpi=300)
plt.close()

# Chart 3: Sales versus profit
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category",
    s=100
)
plt.title("Relationship Between Sales and Profit")
plt.tight_layout()
plt.savefig("output/3_sales_vs_profit.png", dpi=300)
plt.close()

# Chart 4: Dashboard
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

sns.barplot(
    data=df, x="Category", y="Sales",
    estimator=sum, errorbar=None, ax=axes[0, 0]
)
axes[0, 0].set_title("Sales by Category")

sns.barplot(
    data=df, x="Region", y="Sales",
    estimator=sum, errorbar=None, ax=axes[0, 1]
)
axes[0, 1].set_title("Sales by Region")

sns.scatterplot(
    data=df, x="Sales", y="Profit",
    hue="Category", ax=axes[1, 0]
)
axes[1, 0].set_title("Sales vs Profit")

sns.barplot(
    data=df, x="Category", y="Profit",
    estimator=sum, errorbar=None, ax=axes[1, 1]
)
axes[1, 1].set_title("Profit by Category")

fig.suptitle("Retail Sales Analysis Dashboard", fontsize=16)
plt.tight_layout()
plt.savefig("output/4_sales_dashboard.png", dpi=300)
plt.close()

# Save category summary
summary = df.groupby("Category")[["Sales", "Profit"]].sum()
summary.to_csv("output/category_summary.csv")

print("\nCATEGORY SUMMARY")
print(summary)

print("\nPROJECT COMPLETED SUCCESSFULLY!")
print("Check the output folder for charts and results.")
