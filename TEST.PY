#
# 
# print("hello world")"

#acceptint input from user



#name = input("Enter your name ")avourite_food = input("Enter your favourite Food"
#print("My favourite Food is " + favourite_food + ". ")



#
# 
# print(t+h)
#print("\n================================================")

#print("       STUDENT PROFILE        ")

#print("\n=-===============================================")

#name = input("Enter your name !")

#num1 = float(input("Enter first score"))
#num2 = float(input ("Enter second score"))
#@num3 = float(input ("enter third score")) 

#full_score = (num1 + num2 + num3)  
#print(full_score)

#average = full_score % 2
#print(average) 

#student_name = "EMMANUEL"
#rint(student_name.upper())
#print(len(student_name))

#um1 = int(input("Enter first number:"))
#num2 = int(input("Enter second number:"))




#result = (num1 /num2)
#print(resu

             #CONTROL STRUCTURS 
        
             
#num = int(input("Enter your score:"))

#if num >= 70:
##    print("excellent")
# num >= 50:
#    print("Good")    
#else:
#    print("faill")    

#print("\n==============================================")
#print("               STUDENT PR0FILE")

#print("\n==============================================")

#grade = int(input("Enter score :"))

#if grade >= 80:
#    print("A")
#elif grade >= 70:
#print("B")
#elif grade >= 60:
 #   print("c")    
#elif grade >= 50:
 #   print("D")    
#else:
 #   print("F")  
 
 
            #calculator
            

#num1 = float(input("Enter first number"))          
#operator  = input("enter an operator")
#num2 = float(input("enter anothe number"))

#if operator =="+" :
 #   print(num1 + num2)
#elif operator == "*"   :
  #  print(num1 *num2)
#elif operator == "-"   :
#print(num1 - num2)
#lif operator == "/"    :
 #   print(num1 / num2)
#else :
#    print("invalid operator")  
    


    
    
    #FUNCTIONS


       #TRANSACTION
       
       



#
# list and tuple
"""
courses = ["biology","chemistry","problem-solving","web-tech"]
print(courses)
print(courses[1])
courses.append("csc")
courses.remove("problem-solving")
print(courses)

print("\n=============================================")
print("       STUDENT TUPLE                           ")
print("\n=============================================")
student_profile = ("emmanuel","19","computer-science")
print(student_profile[2])
print(student_profile[-1])

"""


"""
courses = ["chemistry","biology","english","maths","advance-maths"]
print(courses)
print(courses[0])
print(courses[2])
print(courses[1]) == "cos"
courses.append("algebra")
courses.remove("maths")
print(courses)

profile = ("emmanuel","27","DI")
print(profile[0])
print(profile[2])
print(profile[-3])
print(profile)
"""



#DICTIONARIES
"""
student = {
    "name": "emmanuel",
    "age": 50,
    "department": "computer-science",
    "level": 200
}

print(student)

print(student["name"])
print(student["department"])

student["level"] = 500

student["school"] = "Rivers State University"

print(student)
"""


"""
print("\n=========================================")
print("          STUDENT PROFILE MANAGER          ")
print("\n=========================================")

profile = {
  
    "name" : "emmanuel",
    "age" : 89,
    "course" : "algebra",
    "level" : 500,
    "school" : "RSU",
}
print(profile)
profile["name"]
profile["course"]
profile["level"] = 700
profile["course"] = "english"
profile["country"] = "nigeral"

print(profile)
print(profile["country"])

student = {
    "name": "Emmanuel",
    "age": 19,
    "course": "Computer Science",
    "level": 200
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("course" in student)

student.pop("age")

print(student)




language = {"python","java","c++","python","javascript","c++"}
print(language)

language.add("html")
language.remove("java")
print(language)
print(language[0])
"""

"""
name = "emmanuel"

print(name.upper())

print(name.islower())

print(name[0])

print(name[7])

print(name.replace("emmanuel" , "ella"))


phrase = "python is easy to learn"

print(phrase.split())




phrase = "python is easy to   learn"

print(phrase.split())
print(phrase.strip())
print(phrase)




name = "emmanuel"
age = 67
time = 34

print(f"my name is,{name},i am {age},i leave on{time} street")

numbers = [2,5,8,11,14,17,20]

new_numbers = (numbers % 2 ==0 for number in numbers)
print(new_numbers)

"""









        # TXT FILE

"""
name = "emmanuel"
course = "digital electronic"

with open ("student.txt", "w") as file:
    file.write(f"my name is{name},\n")
    file.write(f"and i studied,{course}")
    
with open ("student.txt","r") as file:
    content = file.read()
    print(content)
    """
    
              #CSV FILE
              # 
"""              
import csv

with open ("student.csv", "w" ,newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["NAME","AGE","COURSE"])
    writer.writerow(["emmanuel,19,python"])
    writer.writerow(["ella,18,networking"])
    
    print(writer)
    
import csv
with open ("student.csv","r")  as file:
    reader = csv.reader(file)   
    
    for row in reader:
        print(row)
"""

          #JSON FILE
          
          
 
 
"""         
import json

student = {
    "name": "Emmanuel",
    "age": 19,
    "department": "Computer Science"
}

# Save the details
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read the details
with open("student.json", "r") as file:
    data = json.load(file)

# Print specific details
print(data["name"])
print(data["department"])
    


      modules

import math

number = 144
print(math.sqrt(number))
print(math.pi)

"""











