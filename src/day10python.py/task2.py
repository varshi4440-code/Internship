import pandas as pd

# ----------------------------------
# STEP 1: Create Sample Dataset
# ----------------------------------
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Price": ["$1,200", "$800", "$450", "$300"],
    "Date": ["2024-01-05", "2024-01-10", "2024-02-01", "2024-02-05"]
}

df = pd.DataFrame(data)

# ----------------------------------
# STEP 2: Check Initial Data Types
# ----------------------------------
print("Before Conversion:\n")
print(df.dtypes)

# ----------------------------------
# STEP 3: Clean Price Column
# Remove $ and commas, convert to float
# ----------------------------------
df["Price"] = df["Price"].str.replace("[$,]", "", regex=True)
df["Price"] = df["Price"].astype(float)

# ----------------------------------
# STEP 4: Convert Date Column
# ----------------------------------
df["Date"] = pd.to_datetime(df["Date"])

# ----------------------------------
# STEP 5: Check Data Types Again
# ----------------------------------
print("\nAfter Conversion:\n")
print(df.dtypes)

# ----------------------------------
# STEP 6: Now Data is Usable
# ----------------------------------

# Average Price
print("\nAverage Price:", df["Price"].mean())

# Monthly Average Price
print("\nMonthly Average Price:")
print(df.groupby(df["Date"].dt.month)["Price"].mean())