# Task 1: Print the Elements of a List
# For Loop:
# Write a program that iterates over a list of numbers and prints each number.
# While Loop:
# Write the same program using a `while` loop instead of a `for` loop.
# CODE


# Task 2: Reverse a String
# For Loop:
# Write a program that takes a string as input and prints
# the string in reverse order using a `for` loop.
# While Loop:
# Write the same program using a `while` loop.
# CODE


# Task 3: FizzBuzz
# For Loop:
# Write a program that prints numbers from 1 to 50.
# For multiples of 3, print "Fizz" instead of
# the number, and for multiples of 5, print "Buzz."
# For numbers that are multiples of both
# 3 and 5, print "FizzBuzz."
# While Loop:
# Write the same program using a `while` loop.
# CODE



import random
my_list = [1,2,3,4,5]
# print(my_list)
# numbers = [10,20,30,40,50]


# for number in numbers:
#     print(number)

# numbers = [10,20,30,40,50]
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1 

# TASK 2 REVERSE A STRINGS "FOR LOOP"
# input_string = input("Enter a string:")
# reversed_string = ""
# for char in input_string: 
#     reversed_string = char + reversed_string
#     print("Reversed string:", reversed_string)


# WHILE LOOP 
# i = len(input_string) -1
# while i >= 0:
    # print(input_string[i], end="")
    # i -= 1


# user_input = input("evans:evans")
# index = len(user_input) -1
# while index >= 0:
#     print(user_input[index])
#     index -= 1


# TASK 3: FIZZ BUZZ
for number in range(1,51):
    if number % 3 == 0 and number % 5 == 0:
        # print("FIZZBUZZ") 
        pass
    # elif number % 3 == 0:
    #     print("FIZZ")
    # elif number % 5 == 0:
    #     print("BUZZ")
    # else:
    #     print(number)

# WHILE LOOP:
# number = 1
# while number <= 50:
#     if number % 3 == 0 and number % 5 == 0:
#         print("FIZZBUZZ")
#     elif number % 3 == 0:
#         print("FIZZ")
#     elif number % 5 == 0:
#         print("BUZZ")
#     else:
#         print(number)






# assignment 
# part 1
# n = int(input("please enter a positive integer:"))
# total_sum = 0
# for number in range(1, n + 1):
#     total_sum += number
# print(f"The sum of numbers from 1 to {n} is:{total_sum} ")


# part 2
# number = int(input("please enter a number:"))
# print(f"multiplication table for {number}:")
# for i in range(1,13):
#     print(f"{number} * {i} = {number * i}")


# part 3
random_number = random.randint(1,10)
guess = None
attempts = 0 
# while True:
#     attempts += 1
#     guess_number = int (input("guess the number (between 1 and 10):"))
#     if guess_number == random_number:
#         print(f"Congratulations! you've guessed the correct number {random_number} in {attempts} attempts.")
#         break
#     elif guess_number < random_number:
#         print("Too low")
#     else:
#         print("Too high")



number = int(input("Please enter a positive integer:"))
factorial = 1
current = number
while current > 1:
    factorial *= current
    current -= 1
print(f"the factorial of {number} is:{factorial}")










































































