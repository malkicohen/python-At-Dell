name = input("enter first name\n")
last_name = input("enter last name\n")
age = int(input("enter age\n"))
print("name", name)
print(last_name)
print(f"age", age)

if age + 3 < 15:
    print(f"The user {age} is a child")
elif 15 < age + 3 < 23:
    print(f"The user {age} is young")
else:
    print(f"The user {age} is an adult")
