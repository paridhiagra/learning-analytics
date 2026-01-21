# Extra
print("Hello")
print("This is my first program.")
print("I hope you all like it.\nThis is my video related to learn data analytics from basics.") # \n is used to print in a new line.
print("""Hello,
My name is Paridhi Agrawal.
And currently I'm pursuing B-tech in ECE branch.
This is my 3rd year.""")  # Triple quotes are used to print multiple lines.
print('I\'m from Uttar Pradesh.')  

# Variables
a = 1
b = 2
print("Sum of 1 and 2 =", a+b)

# Datatypes and User-inputs
# 1. Strings
name = input("Enter your name: ")
print("Hello,", name)

# 2. Integer
age = int(input("Enter your age: "))
print("My age is ",age)

# 3. Float 
length = float(input("Enter the length of the rectangle: "))
print(length)

# 4. Eval
expression = eval(input("Enter any equation here: "))    # "eval" uses to evaluate any expression.
print("Answer of the given equation is = ",expression)

# # Type casting - implicit and explicit
p = 158
print(p, type(p))
q = 12.35
print(q, type(q))
r = "123"
print(r, type(r))

# explicit typecasting
d = int(r)
print("After conversion type of r is:",type(d))

# implicit typecasting 
s = p+q+d
print(s,type(s))
