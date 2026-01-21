"""
Problem = 1
Write a program to display a person's name, age and address in three different lines.
"""
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
print("Name = ",name,"\nAge = ", age,"\nAddress = ", address)

"""
Problem = 2
Write a program to swap two variables.
"""
#Method 1 (using temporary variable)
x = 12
y = 13
temp = x
x = y
y = temp
print("x = ",x)
print("y = ",y)

#Method 2
a = 30
b = 40
c = 50
a,b,c = c,b,a
print("a = ",a)
print("b = ",b)
print("c = ",c)

"""
Problem = 3
Write a program to convert a float into integer.
"""
z = 143.44
print("z = ",z)
print(type(z))
v = int(z)
print("v = ",v)
print(type(v))

"""
Problem = 4
Write a program to take details from a student ID-card and then print it in different lines.
"""
name = input("Enter the name of the student: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
email = input("Enter the email: ")
phone_no = input("Enter your phone number: ")
roll_no = input("Enter the roll no: ")
stu_class = input("Enter your class: ")
school = input("Enter the name of the school: ")
print("-----Student Identity Card-----")
print("Name: ",name)
print("Age: ",age)
print("Address: ",address)
print("Email: ",email)
print("Phone No: ",phone_no)
print("Roll No: ",roll_no)
print("Class: ",stu_class)
print("School: ",school)

"""
Problem = 5
Write a program to take an user input as integer then convert it to float.
"""
integer = input("Enter the integer number you want to convert it into float: ")
print(integer,type(integer))
float_number = float(integer)
print(float_number,type(float_number))
