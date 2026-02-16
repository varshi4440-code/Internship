import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Example dataset (replace with your dataset)
data = pd.read_csv(r"C:\Users\varshitha v\Desktop\ds_ai_internship\src\day13python.py\housing.csv.csv")

# Plot Histogram with KDE
plt.figure(figsize=(8,5))
sns.histplot(data['Price'], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

price_skewness = skew(data['Price'])
price_kurtosis = kurtosis(data['Price'])

print("Skewness:", price_skewness)
print("Kurtosis:", price_kurtosis)

plt.figure(figsize=(8,5))
sns.countplot(x=data['City'])
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()