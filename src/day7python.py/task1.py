name = input("Enter your name: ")
goal = input("Enter your Daily Goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Goal: {goal}\n")

print("Journal updated!")
