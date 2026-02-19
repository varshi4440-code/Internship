# Central Limit Theorem Demonstration

import numpy as np
import matplotlib.pyplot as plt

# Step 1️⃣ Create a heavily right-skewed population (Income-like data)
np.random.seed(42)
population = np.random.exponential(scale=50000, size=10000)

# Step 2️⃣ Take 1000 samples (each of size 30) and compute their means
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

# Step 3️⃣ Plot histogram of the sample means
plt.figure()
plt.hist(sample_means, bins=30, density=True)
plt.title("Distribution of Sample Means (n = 30)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()

