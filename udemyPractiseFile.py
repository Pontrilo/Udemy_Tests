# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# elif (int(18 - age) == 1):
#     print("Please come back in {0} year".format(18 - age))
# else:
#     print("Please come back in {0} years".format(18 - age))
#
#
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time!")

# age = int(input("How old are you? "))

# if (age >=16) and (age <=65):
# if 15 < age < 66:
#     print("Have a good day at work")
# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#
# if (some_condition) or (some_wierd_function_that_does_stff()):
#     #do something

# x = "false"
# if x:
#     print("x is true")

# x = input("Please enter some text ")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

# x = 5
# y = 7
#
# if (x != y):
#     if (x > y):
#         print("x is greater than y")
#     else:
#         print("x is smaller than y")
#
# if (x == y):
#     print("x equals y")

# for i in range(1, 20):
#     print("i is now {}".format(i))
#
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {} ".format(newNumber))
#
# for i in range(0,10):
#     print(int(i))

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in "0123456789":
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))
#
# for state in ["not pining","no more","a stiff","bereft of life"]:
#     print("This parrot is " + state)
# Alternative print("This parrot is {}".format(state))

# for i in range(0, 100, 5):
#     print("i is {} ".format(i))

# for i in range(1,13):
#     for j in range (1,13):
#         print("{1} times {0} is {2}".format(i, j, i*j), end="\t")
#     # print("=================")
#     print('')

# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# for char in quote:
#     if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         print(char, end = '')

# for i in range(0,101,7):
#     print(i)

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         print("I'm ignoring "+ item)
#         continue  # continue bypasses the block of code above
#     print("Buy " + item)
#
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         break  # Will stop the for loop when it reaches the argument above the break
#     print("Buy " + item)
#
# meal = ["eggs", "bacon", "spam", "sausages"]  # list of items to analyse
# nasty_food_item = ""
#
# for item in meal:
#     if item in meal:
#         if item == "spam":  # check if the item spam is in the meal list
#             nasty_food_item = item  # set spam to be a nasty food item if it does exist
#             break
# else:
#     print("I'll have a plate of that then please")  # error to handle the problem that spam might not exist
#
# if nasty_food_item:  # if nasty item does exist from the block above do the below
#     print("Can't i have anything without spam in it")

""" Write a program that prints all the numbers from 0 to 20 that are not divisible by 3 or 5 including zero """
# # My solution
# for i in range(0, 21):
#     if i > 0 and i % 3 == 0:
#         continue
#     elif i > 0 and i % 5 == 0:
#         continue
#     elif i == 0:
#         continue
#     print(i)

# recommended best solutions with and without continue

# using continue
# for x in range(20):
#     if x % 3 == 0 or x % 5 == 0:
#         continue
#     print(x)

# without continue
for x in range(20):
    if x % 3 != 0 and x % 5 != 0:
        print(x)

# number = 5
# multiplier = 10
# answer = 0
#
# for i in range(1):
#     number *= multiplier
#
# answer = number
#
# # add your loop after this comment
#
#
# print(answer)
#

