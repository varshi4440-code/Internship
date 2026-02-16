list=[21,43,5,67,87]
print(list)

list.append(31)
print(list)

list.remove(43)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

inventory=["Apples","Bananas","Carrots","Dates"]
print("Current inventory:",inventory)

inventory.append("Eggs")

inventory.remove("Bananas")

inventory.sort()

print("Final Update Inventory:",inventory)
