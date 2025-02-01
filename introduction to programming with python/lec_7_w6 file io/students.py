
students = []

with open("students.csv") as file :
    for line in file:
        name , house = line.rstrip().split(",") # assign to  two variables
        student ={"name":name,"house":house}
        students.append(student)


for student in sorted(students,key=lambda student:student["name"]): # sorted take a `key` parameter it's type is function.
    print(f"{student ['name']} is in {student ['house']}")
    
