"""Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year and therefore be out of date the next year
"""


#init vars

age = "0"
name = " "
currentYear = 2025
yearsUntil = 0
yearIn = 0

#create function to calculate the year the user will turn 100 and print it out
def years(age):
    yearsUntil = 100 - age
    yearIn = currentYear + yearsUntil
    print(name + ", assuming the current year is 2025, you will be 100 in the year: ", + yearIn)


#get name
name = input("Hello, to begin please enter your name: > ")
#get age
age = input("To find out what year you will turn 100, please enter your age: > ")
years(int(age))


#this could easily be updated to allow the user to put in the current year by adding the currentYear varible as an input, however the constraints ask it be out of date next year