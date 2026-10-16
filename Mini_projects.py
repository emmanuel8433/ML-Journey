"""
print("\n===========================================")
print("       COURSE REGISTRATION MANAGER           ")
print("\n===========================================")

#list
course = ["maths","english","biology","chemistry","cos"]
print(course)
print(course[1])

course.append("biochemistry")
print(course)

course.remove["chemisrty"]
print(course)

print(course)

#tuple

student_profile = ("emmanuel","45","computer-science")
print(student_profile[0])
print(student_profile[-1])

print(student_profile)


#dictionary

student = {
    "name": "emmanuel",
    "level": 100,
    "department": "computer-science",
    "school" : "RSU",
}
print(student.keys())
print(student.values())
print(student.item())
print(student["level"]) = 500
student["registered"]
print(student) = "true"

student.pop("school")
print(student)
print(student["department"])

print(student)


#set

python_student = {"emmanuel","john","favour"}
java_student = {"peter","kosi","sampson"}

print(python_student)
print(java_student)
print(python_student | java_student)
python_student.add("tobi")

print(python_student & java_student)
print(python_student - java_student)


    # WOEKING WITH TXT,CSV,JSON.   MINI PROJECT
    
    
    
student = "name"   
age = 24
department = "D&I"

with open ("student.text","w") as file:
    file.write(f"my name is {student}\n")
    file.write(f"i am ,{age},year old\n")
    file.write(f"my department is {department}")
    
with open ("student.txt", "r") as file:
    content = file.read() 
    
    print(content)       
    

import csv

with open ("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["NAME","AGE","DEPARTMENT"])
    writer.writerow(["emo","david","sam"])
    writer.writerow(["d&i","po","opi"])
    
    
with open ("student.csv", "r") as file:
    reader = csv.reader(file) 
    
    for row in reader:
        print(row)
        
        
import json

student_info = {
    "name" : "emmanuel",
    "age" : 86,
    "course" : "ist",
}        


with open ("student.json","w") as file:
    json.dump(student,file,indent=4)
    
with open ("student.json","r") as file:
    data = json.load(file)   


print(data["name"])
print(["department"])



"""