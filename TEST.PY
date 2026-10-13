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
       
       
def withdraw_Money(Account_balnce,withdraw_ammount):
    if Account_balance <=0:
        return"invalid withdraw"
    
    elif withdraw_Amount > Account_balance  :
        return"insufficent fund"     
    
    else:
        remaning_balance = Account_balance - withdraw_Amount
        return" remaining_balance"
    
              
Account_balance = int(input("Enter Account Blance"))       
withdraw_Amount = int(input("Enter withdraw Amount"))

result = withdraw_Amount(Account_balance,withdraw_Amount)
print(result)
    
    
    
    









