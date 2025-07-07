student = {
    "name": "Kaviya",
    "age": 20,
    "course": "AIML"
}
print(student)
student["email"] = "abc@example.com"
print(student)
del student["course"]           
student.pop("email")             
print(student)
print(student.keys())     
print(student.values())   
print(student.items())    
print(student.get("name"))
print(student.get("email", "Not Found"))  
print(student.get("age", "Not Found"))
print(student.get("course", "Not Found"))


student["age"] = 21
print(student)
student["name"] = "Kaviya R"
print(student)
student["course"] = "Data Science"
print(student)

nested = {
    "p1": {"name": "abc", "domain": "AI"},
    "p2": {"name": "def", "domain": "Web Dev"}
}

print(nested["p1"]["domain"])  

print(nested["p2"]["name"])    
print(nested["p1"]["name"])    
print(nested["p2"]["domain"])

new_student = student.copy()
print(new_student)

if "name" in student:
    print("Name is present")
else:
    print("Name is not present")

if "email" in student:
    print("Email is present")
else:
    print("Email is not present")

if "age" in student:
    print("Age is present")
else:
    print("Age is not present")

if "course" in student:
    print("Course is present")
else:
    print("Course is not present")

# The .get() method is used to retrieve a value from a dictionary.
# If the key is not found, it returns None or a specified default value. (eg "Not Found" in line 16, 17, 18)
# It is also used in exceptional handling to avoid KeyError and also used a replacement for try-except block.
# The .copy() method creates a duplicate copy of the dictionary.
# The .keys() method returns a list of all the keys in the dictionary.
# The .values() method returns a list of all the values in the dictionary.
# The .items() method returns a list of all the key-value pairs in the dictionary.
# The .pop() method removes a key-value pair from the dictionary and returns the value.
# The .del statement removes a key-value pair from the dictionary.
