# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# For reproducibility
np.random.seed(42)

# 1️⃣ Normal Distribution (Human Heights)
heights = np.random.normal(loc=165, scale=10, size=1000)

# 2️⃣ Right-Skewed Distribution (Household Incomes)
incomes = np.random.exponential(scale=50000, size=1000)

# 3️⃣ Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.exponential(scale=10, size=1000)
scores = np.clip(scores, 0, 100)

datasets = {
    "Normal Distribution (Heights)": heights,
    "Right-Skewed Distribution (Incomes)": incomes,
    "Left-Skewed Distribution (Easy Exam Scores)": scores
}

for title, data in datasets.items():
    df = pd.DataFrame(data, columns=["Value"])
    
    mean = df["Value"].mean()
    median = df["Value"].median()
    
    # Plot Histogram
    plt.figure()
    plt.hist(df["Value"], bins=30, density=True)
    
    # KDE Overlay
    kde = gaussian_kde(df["Value"])
    x_vals = np.linspace(df["Value"].min(), df["Value"].max(), 1000)
    plt.plot(x_vals, kde(x_vals))
    
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.show()
    
    print(title)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    
    if mean > median:
        print("Right-Skewed (Mean > Median)")
    elif mean < median:
        print("Left-Skewed (Mean < Median)")
    else:
        print("Normal Distribution (Mean ≈ Median)")
    
    print("-" * 50)

