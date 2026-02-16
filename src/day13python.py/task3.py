import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv(r"C:\Users\varshitha v\Desktop\ds_ai_internship\src\day13python.py\housing.csv.csv")

# -----------------------------------
# 1️⃣ Correlation Matrix
# -----------------------------------
corr_matrix = df.corr(numeric_only=True)

print("Correlation Matrix:\n")
print(corr_matrix)

# -----------------------------------
# 2️⃣ Heatmap using Matplotlib
# -----------------------------------
plt.figure()
plt.imshow(corr_matrix)
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title("Correlation Matrix Heatmap")
plt.colorbar()
plt.show()

# -----------------------------------
# 3️⃣ Identify High Correlation (>0.8)
# -----------------------------------
print("\nHighly Correlated Pairs (> 0.8):")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            print(f"{corr_matrix.columns[i]} & {corr_matrix.columns[j]} → {corr_matrix.iloc[i, j]:.2f}")

# -----------------------------------
# 4️⃣ Boxplot for Outlier Detection (Price)
# -----------------------------------
plt.figure()
plt.boxplot(df["Price"])
plt.title("Boxplot of Price")
plt.ylabel("Price")
plt.show()
