# Step 1: Create a dictionary with at least three contacts
contacts = {
    "Asha": "9876543210",
    "Ravi": "9123456780",
    "Meena": "9988776655"
}

# Step 2: Add a new contact
contacts["Kiran"] = "9012345678"

# Step 3: Update an existing contact's phone number
contacts["Ravi"] = "9000000000"

# Step 4: Safe access using .get()
existing_contact = contacts.get("Asha", "Contact not found")
missing_contact = contacts.get("Suresh", "Contact not found")

print("Lookup Results:")
print("Asha:", existing_contact)
print("Suresh:", missing_contact)

print("\nContact List:")
# Step 5: Iterate using .items()
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
