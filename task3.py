# Program to check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


# Program to check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# Program to check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# Program to find the largest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest Number:", a)
elif b >= a and b >= c:
    print("Largest Number:", b)
else:
    print("Largest Number:", c)


# Program to calculate grade based on marks
mark = int(input("Enter your mark: "))
if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Grade F")


# Program for login validation using nested if
username = input("Enter Username: ")
password = input("Enter Password: ")
if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")


# Program to check scholarship eligibility
marks = int(input("Enter Marks: "))
attendance = int(input("Enter Attendance Percentage: "))
if marks >= 75:
    if attendance >= 80:
        print("Eligible for Scholarship")
    else:
        print("Not Eligible (Low Attendance)")
else:
    print("Not Eligible (Low Marks)")