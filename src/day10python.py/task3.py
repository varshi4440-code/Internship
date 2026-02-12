import pandas as pd

# ----------------------------------
# STEP 1: Create messy dataset
# ----------------------------------
data = {
    "Location": [" New York", "new york", "NEW YORK ", 
                 "Los Angeles", " los angeles ", "LOS ANGELES"]
}

df = pd.DataFrame(data)

print("Before Cleaning:")
print(df["Location"].unique())

# ----------------------------------
# STEP 2: Remove whitespace
# ----------------------------------
df["Location"] = df["Location"].str.strip()

# ----------------------------------
# STEP 3: Standardize casing
# (You can use .str.lower() OR .str.title())
# ----------------------------------
df["Location"] = df["Location"].str.title()

# ----------------------------------
# STEP 4: Verify result
# ----------------------------------
print("\nAfter Cleaning:")
print(df["Location"].unique())

