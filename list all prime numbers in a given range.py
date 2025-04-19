#list all prime numbers in a given range


#global vars
userNum = " "

#function for checking if a number is prime
def primeCheck(userNum):
    for number in range(int(userNum)):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number)
            

userNum = input("Enter a number to find all prime number starting from 0: > ")
primeCheck(userNum)