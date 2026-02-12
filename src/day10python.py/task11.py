#The Integrity Audit
import pandas as pd

df = pd.read_csv(r"C:\Users\varshitha v\Desktop\ds_ai_internship\src\day10python.py\customer_orders.csv")

print("Shape before cleaning:", df.shape)

print("\nMissing Values Report:")
print(df.isna().sum())

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

df = df.drop_duplicates()

print("\nShape after cleaning:", df.shape)

print("\nCleaned Data:")
print(df.head())
