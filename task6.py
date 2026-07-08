# Create two sets
set1 = {10, 20, 30, 40, 50, 60}
set2 = {40, 50, 60, 70, 80, 90}

print("Set 1:", set1)
print("Set 2:", set2)

# Add an element
set1.add(100)
print("After add():", set1)

# Remove an element
set1.remove(20)
print("After remove():", set1)

# Union of two sets
print("Union:", set1.union(set2))

# Intersection of two sets
print("Intersection:", set1.intersection(set2))

# Difference of two sets
print("Difference (set1 - set2):", set1.difference(set2))

# Copy a set
copy_set = set1.copy()
print("Copied Set:", copy_set)

# Clear the copied set
copy_set.clear()
print("After clear():", copy_set)


# Create a dictionary
student = {
    "id": 101,
    "name": "Suresh",
    "age": 21,
    "city": "Chennai",
    "course": "B.Tech IT"
}

print("Original Dictionary:", student)

# Display keys
print("Keys:", student.keys())

# Display values
print("Values:", student.values())

# Display key-value pairs
print("Items:", student.items())

# Remove one key
student.pop("age")
print("After pop():", student)

# Clear dictionary
student.clear()
print("After clear():", student)


# Function to print a welcome message
def welcome():
    print("Welcome to Python Programming")

welcome()


# Function to add two numbers
def add(a, b):
    print("Sum =", a + b)

add(10, 20)


# Function to find square of a number
def square(num):
    print("Square =", num * num)

square(5)


# Function to find the largest of two numbers
def largest(a, b):
    if a > b:
        print("Largest =", a)
    else:
        print("Largest =", b)

largest(15, 25)


# Function using positional arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Suresh", 21)


# Function using keyword arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=21, name="Suresh")


# Function using default arguments
def greet(name="Student"):
    print("Welcome", name)

greet()
greet("Suresh")


# Function using *args
def total(*numbers):
    print("Numbers:", numbers)
    print("Sum =", sum(numbers))

total(10, 20, 30, 40)


# Function using **kwargs
def details(**student):
    print(student)

details(name="Suresh", age=21, city="Chennai")


# Function to return sum
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)


# Function to return cube
def cube(num):
    return num ** 3

result = cube(4)
print("Cube =", result)


# Function to return largest among three numbers
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

result = largest(15, 30, 25)
print("Largest =", result)