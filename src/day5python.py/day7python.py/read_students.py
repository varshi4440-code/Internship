import csv
with open("students.csv","r",newline="") as file:
    reader=csv.DictReader(file)
    print("Students who passed : ")
    for row in reader:
        if row["status"].strip() =="Pass":
            print(row["Name"])
