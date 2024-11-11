favourite_fruits = ["Pineapple","Apple","Orange","Banana","Grapes"]
favourite_fruits.append("Mango")
favourite_fruits.pop(2)
favourite_fruits[1] = "strawberry"
# print(favourite_fruits) 



tuple 
cities_to_visit = ("Liverpool", "Paris","New York","Barcelona")
# print(cities_to_visit[0])
# print(cities_to_visit[3])
#  "Try":
    #  cities_to_visit[1] = "Nashville"





"task three"
person ={
    "Name": "John",
    "Age": 25,
    "City": "New York"
} 
person["Email"] = "John@gmail.com"
person["Age"] = 26
person.pop("City")
# print(person)



"Task four"  
student_profile = {
    "name": "Alice",
    "Age": 21,
    "Grades":{
        "math": 90,
        "science": 85,
        "literature": 88
        },
        "contact_info": {
            "Email":
            "Alice@example.com",
            "phone": "123-456-7890"
        }
}
# print("student's name:", student_profile["name"])
# print("science grade:", student_profile["Grades"]["science"])
student_profile["Grades"]["literature"] = 92
student_profile["contact_info"]["address"] = "123 main street, New York"
# print("updated student profile:", student_profile)



"Taskfive"
company = {
    "IT":{
        "manager": " John Doe",
        "Employees": ["Alice", "Bob", "Charlie"]
    },
    "HR": {
        "manager": "Jane Smith",
        "Employees": ["Dave", "Eva"]
    },
    "Marketing": {
        "manager": "Michael Brown",
        "Employees": ["Fiona","George"]
    }
}
# print(f"The HR manager is: {company['HR']['manager']}")
# print(f"Employees in the IT department:{company['IT']['Employees']}")
company["Marketing"]['Employees'] = "Hannah"
company["IT"]['manager'] = "Sarah Conor"
# print("updated company dictionary:")
# print(company)






