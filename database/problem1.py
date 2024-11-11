def write_to_file(filename):
    user_input = input ("Enter data (comma seprated): apple,banana,grapes")
    data_list = user_input.split(',')
    with open(filename,'w') as file:
        for item in data_list:
            file.write(item.strip() + '\n')
write_to_file('user_data.txt')            


# problem 2
def login(username="admin",password= "1234"):
    user = input("Enter username: ")
    passw = input("Enter password: ")
    if username == user and password == passw:
        print ("Login successful")
    else:
        print ("invalid credentials")


# login()


# problem 3

def convert_temp():
    celsius = float(input("enter the temperature in celsius:"))
    fahrenheit = celsius * 9//5 + 32
    print(f"The temperature in Fahrenheit is:{fahrenheit}")

# convert_temp()


# problem 4
# sentence = input("enter a sentence:")
# words = sentence.split()
# for word in word
    # print(f"Word:{word}, Length:{len(word)}")

# problem 5
# list1 = input("enter the first list of numbers separated by spaces:").split
# list2 = input("enter the second list of numbers separated by spaces:").split

# list1 = [int [num] for num in list1]
# list2 = [int [num] for num in list2]

# merged_list = list1 + list2
# merged_list.sort()

# print("Sorted merged list:", merged_list)

# problem 6
def calculate_simple_interest(principal,rate,time):
    simple_interest = (principal * rate * time)//100
    return simple_interest

interest = calculate_simple_interest(principal=1000,rate=5,time=3)

# print(f"Simple interest is:{interest}" )


# problem 7
def word_frequency_counter(sentence):
    words = sentence.split()
    word_count ={}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            for word, count in word_count.items():
                            print(f"{word}': {count}")
# sentence = input ("Enter a sentence:")
# word_frequency_counter(sentence)                            


# problem 8
# import random
# target_number = random.randint(1,50)
# print("welcome to Guess the number!")
# print("i'm thinking of a number between 1 to 50.Can you guess it?")
# while True:
#     guess = int(input("Enter your guess:"))
#     if guess < target_number:
#         print("Too low! try again.")
#     elif guess > target_number:
        # print("Too high! try again")
    # else:
        # print("Congratulations! you've guessed the correct number.")
        break


# problem 9
def reverse_list(lst):
    return lst[::-1]
my_list = [1, 2, 3, 4, 5]
reverse_list = reverse_list(my_list)
# print("original list:", my_list)
# print("Reversed list:", reverse_list)


# problem 10
# def is_anagram(word1,word2):
#     word1 = word1.replace("","").lower()
#     word2 = word2.replace ("","").lower()
#     return sorted(word1) == sorted (word2)
# is_anagram(word1="listen", word2= "silent")
                                                                                                                                                                                                                               



























