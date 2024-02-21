# HW2.py
# Author: Jesse Nelson


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."
age = int(input("Please enter your age "))
if age > 20:
    print("You are an adult")
elif age < 13:
    print("You are a child")
else:
    print("You are a teenager")

# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
i = 1
for i in range(1,6):
    if i == 1:
        print("1")
    if i == 2:
        print("12")
    if i == 3:
        print("123")
    if i == 4:
        print("1234")
    if i == 5:
        print("12345")
    if i == 6:
        break
# Question 3:
# Write some code that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:
# The highest number.
# The lowest number.
# The average of all the numbers.

# Hint 1: You will need to use a for loop and a counter variable to keep track of the total sum of the numbers.
# Hint 2: You will need to use an if statement to keep track of the highest and lowest numbers.
total = 0
highest_number = -99999
lowest_number = 99999
for i in range(10):
    number = int(input("Please enter a number"))
    total += number

    if number > highest_number:
        highest_number = number

    if number < lowest_number:
        lowest_number = number

average = total / 10
    

print(average, highest_number, lowest_number)

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement
counter = 0
vowel = "a,e,i,o,u"
input_string = str.lower(input("Please enter a string"))
for letter in input_string:
    if letter in vowel:
        counter += 1
print(counter)




