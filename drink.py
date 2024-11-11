import sys
x = 5
y = 10

# Condition
# if x < y:
#     # Statement
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

# if x != y:
#     print("x is not equal to y")
# elif x == y:
#     print("x is equal to y")

# Assignment
# If invalid drink? Continue asking what they want
# then in the fifth time, ask if they want to continue
# If 'yes' keep asking. If 'no' stop the program
#  ...
#  Do the same for cash payment 
coke = 450
fanta = 400
print("We have\n1. Coke\n2. Fanta\n")
# while True:
drink = input("What do you want? ")
if drink == "coke" or drink == "1":
    qty = int(input("how many are you buying?"))
    print("We have\n1. Vanilla\n2. Diet")
    option = input("Enter your choice: ")
    balance = coke * qty
    if option == "vanilla":
        print("Take your vanilla coke")
    elif option == "diet":
        print("Take your diet coke")
    else:
        print("Take your original coke")
        print(f"Your total balance is {balance}")
elif  drink == "fanta" or drink == "2":
    qty = input("how many are you buying?")
    print("We have\n1. Peach\n2. Grape")
    option = input("Enter your choice: ")
    flavor = ["peach", "grape"]
    if option in flavor:
        print(f"Take your {option} fanta")
    else:
        print("Take your original fanta")
else:
    print("Sorry, we don't have time")
    sys.exit()

print("\n1. Cash payment\n2. Bank payment")
payment = input ("Enter Cash or bank: ")

if payment == "cash" or payment == "1":
    amount = int(input("enter amount:"))
if amount >= balance:
    change = amount - balance
    print(f"your change is {change}")
else:
    for _ in range(2):
        print("insufficient fund")
        amount = int(input("enter amount :"))
        if amount < balance:
            continue
if payment == "bank" or payment == "2":
    print(f"We have deducted {balance} from your account")
else:
    print ("invalid payment method")            

    










