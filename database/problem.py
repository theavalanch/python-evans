def login(username="admin",password= "1234"):
    user = input("Enter username: ")
    passw = input("Enter password: ")
    if username == user and password == passw:
        print ("Login successful")
    else:
        print ("invalid credentials")

# login ()

    
# 2
def convert_temp():
    celsius = float(input("enter the temperature in celsius:"))
    fahrenheit = celsius * 9//5 + 32
    print(f"The temperature in Fahrenheit is:{fahrenheit}")
# convert_temp()

























