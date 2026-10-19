import random
#use list comprehensiom to create a new ist of surnames
surnames = ["GOAT", "living thing", "Bannana"]
students = ["Evan", "Zach", "Jace", "Christian", "Duane", "John", "Mr Klins"]

#use the list comprehension to create a new list with the names combined with a random surname
student_names = [student + " the " + 
                 random.choice(surnames) for student in students if  student != "Mr Klins"]
print(student_names)

















