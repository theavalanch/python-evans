# function definition
def greet():
    # Alogrithm or Instruction to follow
    word = "hello world"
    print(word)
# Call the function 
# greet()


def greeting (name):
    print (f"My name is {name}")
# greeting("evans")

def calc(n,x,y):
    print(n + x + y)

# calc(20,30,40)

def multi (length):
    for l in range (length):
        print("##")

# multi(5)

def main ():
    x = int (input("what's x?"))
    print("x squared is", square (x))

def square (n):
    return n * n
# print (square(10))


def calc():
    a = 10 + 5 
    b = a * 2
    c = 10 + b 
    d = c - 5 
    return b
# print(calc())



def condition(x,y):
    if x > y:
        return "x is greater than y"
    elif x < y:
        return "x is less than y"
    return "x is equal to y"

# print(condition(6,6))


# class activity 
def add(a,b):
    return a + b

# print(add(20,50))

def subtract(a, b):
    return a - b
# print(subtract())

def multiplication (a, b):
    return a * b
# print(multiplication(20,40))

def divide(a,b):
    return a// b
# print(divide(50,0))

def maximum_number(a,b,c):
    if a > b and a < c:
        return a
    elif b > a and b > c:
        return b 
    return c
    
def min_num(a, b ,c):
    return f" Minimum number: {min(a,b,c)}"

def sum_num(a,b,c):
    return f"Sum: {sum ([a,b,c])}"

# print(maximum_number(20,30,40))
# print(min_num(50,40,60))
# print(sum_num(77,30,40))
    

# LAMBDA
# A lambda function is a small anonymous function.
# A lambda function can take amy number of arguments, but can only have one expression.
# Syntax: lambda arguments: expression 
# Use lambda functions when an anonymous function is required for a short period of time.
# Example:
x = lambda a, b : (a + 10) * b
# print (x(5,4))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
# print(mydoubler(11))

# print(myfunc(2)(11))

# GLOBAL VARIABLE 
# A variable declared outside a function is a global variable.
# A global variable can be accessed inside and outside the function.
#  Example:
x = 10

def var():
    # Local Variable 
    x = 5
    # print(x)

# var()


# Assignment 
# part 1
def greet_user(name):
    print(f"hello,{name} welcome!")

# greet_user("Evans")

# part 2
def calculate_area(length,width):
    return length * width
area = calculate_area(5,3)
# print(f"The area of the rectangle is:{area}")

# part 3
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
# print(is_even(6))
# print(is_even(23))

# part 4
def celsius_to_fahrenheit(celsius):
    return (celsius * 9//5) + 32

temp_in_fahrenheit = celsius_to_fahrenheit(30)
# print(temp_in_fahrenheit)

# part 5
def find_largest(numbers):
    return max (numbers)
numbers = [34,32,23,12]
# print ("Largest number:", find_largest(numbers))

# part 6
def print_table(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")

# print_table(8)

# part 7

def add(a,b):
    return a + b

# print(add(20,50))

def subtract(a, b):
    return a - b
# print(subtract(10,5))

def multiplication (a, b):
    return a * b
# print(multiplication(20,40))

def divide(a,b):
    return a// b
# print(divide(50,2))


# lambda continuation 
def compare(x,y):
    if x > y:
        return "x is greater than y"
    elif x < y:
        return "x is less than y"
    return "x is equal to y"

# print(compare(8,7))


compare_lambda = lambda x, y: "x is greater than y" if x > y else "x is less than y" if x < y else "x is equal to y"
# print(compare_lambda(8,8))


def operation(x,y):
    if x % 2 == 0:
        return x * y
    return x + y

# print(operation(4,6))    

operation_lambda = lambda x, y: x * y if x % 2 == 0 else x + y
print (operation_lambda(4,6))

def main_function(x,y):
    # Algorithm or instructions to Follow
    # more code here 
        # Another function 
        # more code here
        # more code here

         pass































































