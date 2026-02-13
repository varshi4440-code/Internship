import matplotlib.pyplot as plt
categories = ['A', 'B', 'C']
values = [11, 20, 15]

plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Simple Bar Chart Example")
plt.show()