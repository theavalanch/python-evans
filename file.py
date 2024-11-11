# FILES

# Open a file for reading 
# file = open("data.py", "r")

# Reading from a file 
# print(file.read()) # Read the entire file
# print(file.read(10)) # Read the first 10 character
# print(file.readline()) # Read the first line 
# print(file.readline()) # Read the second line 
# print(file.readlines()) # Read all the lines and return a list

# Run a loop to read the lines 
# for f in file:
    # print(f, end='')

# Manually close the file after done
# file.close()

# With
# open and automatically close the file when done

# with open ("filenewfile.txt", 'x') as file:
    # file.write("Hello, World\n")
    # file.write("welcome to programming with python\n")
    # file.write("Happy coding😂✅✅\n")



# assignments
# task one

def write_to_file(strings):
    with open ("output.txt", "w") as file:
        for string in strings:
            file.write(string + "\n")

# write_to_file(["hello","this is a test", "python is fun"])

# task two
def read_from_file():
    with open ("output.txt", "r") as file:
        for line in file:
            print(line.strip())

# read_from_file


# task three
def count_words_in_file():
    with open("text.txt", 'r') as file:
        content = file.read()
        word = content.split()
        return print(len(word))
    
count_words_in_file()



# task four
def copy_file():
    with open("text.txt", "r") as source_file:
        content = source_file.read()
    with open ("copy.txt", "w") as destination_file:
        destination_file.write(content)






# task five
def append_to_file(text):
    with open ("output.txt", "a") as file:
        file.write("this is a table" + "\n")

# append_to_file(["this is a table"])


























































































