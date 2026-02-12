import pandas as pd

# 1️⃣ Load the dataset
df = pd.read_csv(r"C:\Users\varshitha v\Desktop\ds_ai_internship\src\day10python.py\customer_orders.csv")

# Print original shape
print("Shape before cleaning:", df.shape)

# 2️⃣ Check missing values
print("\nMissing values report:")
print(df.isna().sum())

# 3️⃣ Fill missing numeric values with median
numeric_columns = df.select_dtypes(include=['number']).columns

for col in numeric_columns:
    median_value = df[col].median()
    df[col].fillna(median_value, inplace=True)

# 4️⃣ Remove duplicate rows (exact match across all columns)
df = df.drop_duplicates()

# Print cleaned shape
print("\nShape after cleaning:", df.shape)
