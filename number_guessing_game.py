print("\n===================================")
print("      NUMBER GUESSING GAME           ")
print("\n===================================")

secret_number = 7
guess = 0

while guess != secret_number:
     guess = int(input("Enter your guess between 1-10:"))

if guess < secret_number:
    print("too low try again")
elif guess  > secret_number :
    print("too high try again")   
else:
    print("winner!!!")    
print("Thanks for playing!")
