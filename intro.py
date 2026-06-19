"""
Multi-line comment:
This program prints personal details,
creates variables, checks data types,
performs string concatenation,
and demonstrates type casting.
"""

# Printing personal details
print("Name: Suresh")
print("College Name: ABC College")
print("City: Arni")

print("\n--- Variables ---")

# Creating variables
name = "Suresh"
age = 21
percentage = 85.5
college = "ABC College"

# Printing variables
print("Name =", name)
print("Age =", age)
print("Percentage =", percentage)
print("College =", college)

print("\n--- Data Types ---")

# Variables of different data types
integer_var = 100
float_var = 99.99
string_var = "Python"
boolean_var = True

# Printing values and their types
print("Integer Value:", integer_var)
print("Type of Integer:", type(integer_var))

print("Float Value:", float_var)
print("Type of Float:", type(float_var))

print("String Value:", string_var)
print("Type of String:", type(string_var))

print("Boolean Value:", boolean_var)
print("Type of Boolean:", type(boolean_var))

print("\n--- String Concatenation ---")

# String concatenation
str1 = "Hello "
str2 = "World"
result = str1 + str2

print("String 1:", str1)
print("String 2:", str2)
print("Concatenated String:", result)

print("\n--- Type Casting ---")

# String to Integer
str_num = "100"
int_num = int(str_num)
print('String "100" to Integer:', int_num)

# Integer to String
num = 50
str_num2 = str(num)
print("Integer 50 to String:", str_num2)

# Integer to Float
num2 = 25
float_num = float(num2)
print("Integer 25 to Float:", float_num)

# 0 and 1 to Boolean
bool_zero = bool(0)
bool_one = bool(1)

print("Boolean value of 0:", bool_zero)
print("Boolean value of 1:", bool_one)