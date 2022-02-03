student = {"Name":"Drax", "Age":13, "Class":"First"}
print(student["Name"])
print(student["Age"])
print(student["Class"])
student["Name"] = "Quill"
print(student["Name"])
student["School"] = "Falletone"
print(student["School"])
print(student)
print(len(student))
#del student["Name"]
print(student)
#student.clear()
print(student)
#del (student)
print(student)
print(student.get("Name"))