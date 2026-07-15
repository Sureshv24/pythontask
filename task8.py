# Program to read the complete file
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()


# Program to read the first line of a file
file = open("student.txt", "r")
print(file.readline())
file.close()


# Program to read all lines
file = open("student.txt", "r")
lines = file.readlines()
print(lines)
file.close()


# Program to write data into a file
file = open("notes.txt", "w")

file.write("Python is easy.\n")
file.write("Python supports OOP.\n")
file.write("Python is platform independent.\n")
file.write("Python has simple syntax.\n")
file.write("Python is easy to understand.\n")

print("5 lines written successfully.")

file.close()


# Program to append data to a file
file = open("notes.txt", "a")

file.write("Python is used for Web Development.\n")
file.write("Python is used for Data Science.\n")
file.write("Python is open source.\n")

print("3 lines appended successfully.")

file.close()


# Program to create a new file
file = open("newfile.txt", "x")
print("File created successfully.")
file.close()


# Program using with open()
with open("student.txt", "r") as file:
    print(file.read())


# Exception Handling
# Program to handle NameError
try:
    print(name)

except NameError:
    print("Error: Variable is not defined.")

finally:
    print("Program Ended.")


# Program to handle TypeError
try:
    result = 10 + "20"

except TypeError:
    print("Error: Cannot add integer and string.")

finally:
    print("Program Ended.")


# Program to handle ValueError
try:
    num = int("Python")

except ValueError:
    print("Error: Invalid integer value.")

finally:
    print("Program Ended.")


# Program to handle ZeroDivisionError
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Program Ended.")


# Program to handle multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result =", result)

except ValueError:
    print("Error: Please enter only numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Execution Completed.")