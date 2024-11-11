fruit= ["apple","banana","cherry","date"]
fruit.append("elderberry")
fruit.remove("banana")
fruit.insert(1,"blueberry")
# print("Number of fruit:", len(fruit))
fruit.sort()
# print("sorted list", fruit)

tuple
dimension = (10,20,30) 
# print("second value in tuple:", dimension[1])
try:
    dimension[0] = 2
    # print (dimension)
except Exception as e:
    # print ("Error:", e)
    
 for dimensions in dimension:
    # print(dimensions)
    pass

student_grades = {"Alice":85, "Bob":90, "Charlie":78}
student_grades["Diana"] = 92   
student_grades["Charlie"] = 80
student_grades.pop("Alice")

for student, grade in student_grades.items  ():
    print(f"{student}: {grade}")


class_grades = {"Alice":{"Math":85, "Science":92, "English":88},
                "Bob":{"Math":79, "Science":85, "English":90},
                "Charlie":{"Math":95, "Science":89, "English":87}
                }

class_grades["Diana"] = {"Math":88, "Science":91, "English":86}
class_grades["Bob"]["Science"] = 90

average_grade = sum(grade.values())/ len(grade) # calculate the average_grade
for student, grades in class_grades.items():
    average_grade = sum(grades.values()) / len(grades)
    print(f"{student}`s average grade is: {average_grade:.2f}")

    del class_grades["Charlie"]

for student, grades in class_grades.items():
    # print(f"{student}`s grades:")
    # print(f"Math: {grades["Math"]}") # Type
    # print(f"Science: {grades["Science"]}")
    # print(f"English: {grades["English"]}/n")
    pass









