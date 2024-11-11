def count_vowels(strings):
    count = 0
    for string in strings:
        strings = "evans is a handsome boy"
        if string in ("a,e, i ,o, u"):
            count += 1
    return count
# print(count_vowels())          
    

# Creating a dictionary from two lists
keys = ["name","age","city"]
values = ["alice", 30, "new york"]
dicts = {}
for key, value in zip (keys, values):
    dicts[key] = value
print(f"Dictionary: {dicts}")
