#roll the dice game
import random


while True:
    answer = input("Roll the dice? enter y or n ")
    if answer == "y":
     die1 = random.randint(1,6)
     die2 = random.randint(1,6)
     print("[", (die1), ",", (die2), "]")
    elif answer == "n":
     break
    else: 
       print("That is not a valid entry")
    

     

