import numpy as np
import pandas as pd

# Step 1️⃣: Create sample dataset (you can replace this with your own dataset)
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100)

# Add some extreme values manually
data = np.append(data, [120, 130, -20])

df = pd.DataFrame(data, columns=["Value"])

# Step 2️⃣: Calculate Mean and Standard Deviation
mu = df["Value"].mean()
sigma = df["Value"].std()

print("Mean (μ):", round(mu, 2))
print("Standard Deviation (σ):", round(sigma, 2))

# Step 3️⃣: Calculate Z-Score
df["z_score"] = (df["Value"] - mu) / sigma

# Step 4️⃣: Identify Outliers (|Z| > 3)
outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)


