# HW3.py
# Author:
import random
import math
import sys
import os
# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
def square(num):
    """input number and return the number squared

    Args:
    num(int): the number to square"""
    return num * num
print(square(5))
# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
# Hint: You will want to use the replace() function
def replace_letter(string, letter, number):
    """takes in a string, a letter, and a number and returns the string with the letter replaced at the number index

    Args:
    string(str): the string to be modified
    letter(str): the letter to replace
    number(int): the index to replace the letter
    """
    return string[:number] + letter + string[number+1:]
print(replace_letter("Hello World", "z", 6))
# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
def within_bounds(num, lower_bound, upper_bound):
    """takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds

    Args:
    num(int): the number to check
    lower_bound(int): the lower bound
    upper_bound(int): the upper bound
    """
    return lower_bound <= num <= upper_bound
print(within_bounds(1, 30, 10))
# Question 4:
# write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."
def personal_info(name, age, color):
    """takes in a name, age, and favorite color and returns a string with the parameters

    Args:
    name(str): the name
    age(int): the age
    color(str): the favorite color
    """
    return f"Hello, my name is {name}. I am {age} years old. My favorite color is {color}."
print(personal_info("Jesse", 25, "blue"))
# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4
def user_info():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    color = input("What is your favorite color? ")
    return personal_info(name, age, color)
print(user_info())
# Question 6:
# import the random module and use it to generate a random number between 1 and 100
def random_number():
    """returns a random number between 1 and 100

    Returns:
    int: random number between 1 and 100
    """
    return random.randint(1, 100)
print(random_number())
# Question 7:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
def square_root(num):
    """returns the square root of a number

    Args:
    num(int): the number to find the square root of
    """
    return math.sqrt(num)
print(square_root(16))
# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
def python_version():
    """prints the version of python you are using
    """
print(sys.version)
# Question 9:
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
def current_directory():
    """prints the current working directory
    """
print(os.getcwd())