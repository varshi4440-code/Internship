# dashboard.py

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (example: monthly sales trend)
months = [1, 2, 3, 4, 5]
monthly_sales = [500, 700, 650, 900, 1100]

# Create first subplot (Bar Chart)
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

# Create second subplot (Line Plot)
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the dashboard
plt.show()