# LIST
thislist =["yes",10, True,3.5,"Bright","23",False,'Bright,','40.50']

# index
# print(thislist[0])
# print(thislist[-4])

# slicing
# print(thislist[1:8:2])
# print(thislist[1:8:2]) #Add 2 steps
# print(thislist[:-3])

# Method or Attribute
thislist.append('Anything') # Add item to the end of the list
# thislist.pop() # Remove item from the end of the list 
thislist.insert(2,"FF")
thislist.remove("Bright")
# thislist .sort()
indexlist = thislist.index (3.5)
countlist = thislist.count('Orange')
thislist[0] = "Banana"
# print (thislist)
# print (indexlist)
# print(countlist)

# TUPLE
mytuple = (12, "Yes",True,50.6,"Yes")   
# mytuple.append(20)
counttuple = mytuple.count("Yes")
# print (counttuple)
print(mytuple)
tuple1 = 1,2,3
tuple2 = 4,5,6
concat_tuple = tuple1 + tuple2
# print(concat_tuple)
# print(tuple1 * 3)

# Dictionary
my_dict = {"Bright":"python", "AC":False, "Chair":3}
# print(my_dict["Chair"])

my_dict["Laptop"] = "Dell" # Adding a new entry
my_dict["AC"] = True # modify an existing entry
# print(my_dict)

# Nesting dictionary
student ={"person1":"David",
          'person2':{"name": "John", "age" :20,"course" :{"Python" : "Begin","HTML":3}},
          "person3" : ["Anna", "HTML",12,False]}
# print(student["person1"])
# print(student["person2"]["age"])







