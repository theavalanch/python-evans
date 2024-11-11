with open ('import/input_dict.txt','r') as infile:
    original_dict = {}
    for line in infile:
        line.strip()
        key, value =line.split(':')
        original_dict[key.strip()] = value.strip()
        inverted_dict = {value : key for key, value in original_dict.items()}
        with open('inverted_dict.txt', 'w') as outfile:
            for key, value in inverted_dict.items():
                outfile.write(f"{key}:{value}\n")
print("Dictionary inverted and written to 'inverted_dict.txt' ")


