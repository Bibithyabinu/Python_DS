student = {
    "name": "Anu",
    "age": 22,
    "course":"Python"
}
print("dictionary:")
print(student)
print("name=",student["name"])
student["mark"]=100
student["age"]= 22
student.pop("course")
print("after removing")
print(student)