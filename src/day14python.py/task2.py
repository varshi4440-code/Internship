import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample dataset
data = {
    "Age": [22, 25, 47, 52, 46, 56, 23, 28, 30, 60],
    "Salary": [25000, 32000, 120000, 150000, 110000, 170000, 28000, 35000, 40000, 200000]
}

df = pd.DataFrame(data)

# ---------------- Standardization ----------------
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

# ---------------- Normalization ----------------
minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

# ---------------- Histogram Before Scaling ----------------
plt.figure()
plt.hist(df["Salary"], bins=5)
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# ---------------- Histogram After Standardization ----------------
plt.figure()
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Salary After Standardization")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.show()

# ---------------- Histogram After Normalization ----------------
plt.figure()
plt.hist(df_normalized["Salary"], bins=5)
plt.title("Salary After Normalization")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.show()

print("Original Data:\n", df)
print("\nStandardized Data:\n", df_standardized)
print("\nNormalized Data:\n", df_normalized)

