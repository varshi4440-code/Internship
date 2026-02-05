a={"key":23}
print(a)

student={
    "name":"amith",
    "age":"21",
    "course":"cse",
    }
print(student["name"])
student["age"]=22
student["city"]="delhi"
print(student)

marks={"math":25,"science":75,"english":85}
print(marks.get("math"))
print(marks.get("history",0))
for subject,score in marks.items():
    print(subject,score)
    
n=int(input("enter number of customer:"))
user_purchases={}
for _ in range(n):
      name=input("enter customer name: ")
      amount=int(input(f"enter purchase amount for{name}: "))
      user_purchase[name]=amount

      
      
numbers=[1,2,3,3,4]
print(numbers)
numbers.add(5)
print(numbers)
