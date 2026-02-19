import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\varshitha v\Desktop\ds_ai_internship\src\day16python.py\customer_orders (1).csv")

plt.hist(data["value"], bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Values")
plt.show()
