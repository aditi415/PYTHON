import pandas as pd

# -----------------------------
# Step 1: Read CSV files
# -----------------------------
products = pd.read_csv("products.csv")
transactions = pd.read_csv("transactions.csv")

# -----------------------------
# Step 2: Data Cleaning
# -----------------------------

# Fill missing prices with mean price
products['price'].fillna(products['price'].mean(), inplace=True)

# Remove duplicate transactions
transactions.drop_duplicates(inplace=True)

# -----------------------------
# Step 3: Merge Datasets
# -----------------------------
data = pd.merge(products, transactions, on='product_id')

# -----------------------------
# Step 4: Analysis
# -----------------------------

# (1) Total quantity sold per segment
segment_sales = data.groupby('segment')['quantity'].sum()
print("\nTotal quantity sold per segment:")
print(segment_sales)

# (2) Segment with highest sales
print("\nHighest sold segment:")
print(segment_sales.idxmax())

# (3) Least sold brand
brand_sales = data.groupby('brand')['quantity'].sum()
print("\nLeast sold brand:")
print(brand_sales.idxmin())

# (4) Top 3 months with highest sales
data['transaction_date'] = pd.to_datetime(data['transaction_date'])
data['month'] = data['transaction_date'].dt.month

monthly_sales = data.groupby('month')['quantity'].sum()
print("\nTop 3 months with highest sales:")
print(monthly_sales.sort_values(ascending=False).head(3))

# (5) Price Analysis
print("\nPrice Analysis:")
print("Total price:", products['price'].sum())
print("Missing prices:", products['price'].isnull().sum())
print("Missing percentage:", products['price'].isnull().mean() * 100)
print("Minimum price:", products['price'].min())
print("Maximum price:", products['price'].max())
print("Mean price:", products['price'].mean())
print("Median price:", products['price'].median())

