import sys

print("HELLO USER")
print("Sign in to play the game")
gmail = input("Please enter your gmail ID:"  )
password = input("Please enter you gmail password:" )
print("Okay user verified")
print("Welcome to Number Ninja")
choice = input("Do you want to play Number Ninja? : ")
if  choice  == "yes":
    print("Move forward")
else:
      print("Back to the home")
      print(" Game is closing")
      sys.exit()

number1 = int(input('Enter your number:' ))
print("Okay so your number is: ",number1)

import random
number2 = random.randint(1,100)



while True:
       
      number1 = int(input("Enter your number: "))

      if  number1 == number2:
         print("Your answer is correct")
         break
      elif    number1 > number2:
           print("Think little more shorter")   
      
      else:
      
            print("Think little more bigger")  

print("YOU WON THE GAME ")            
             

            