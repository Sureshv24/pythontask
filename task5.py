# Create a list with 10 elements
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original List:", numbers)

# Add an element using append()
numbers.append(110)
print("After append():", numbers)

# Insert an element at the 3rd position
numbers.insert(2, 25)
print("After insert():", numbers)

# Add multiple elements using extend()
numbers.extend([120, 130, 140])
print("After extend():", numbers)

# Remove an element using remove()
numbers.remove(50)
print("After remove():", numbers)

# Remove the last element using pop()
numbers.pop()
print("After pop():", numbers)

# Remove an element at a specific index
numbers.pop(3)
print("After pop(3):", numbers)

# Count the occurrences of an element
count = numbers.count(20)
print("Count of 20:", count)

# Find the index of an element
index = numbers.index(60)
print("Index of 60:", index)

# Reverse the list
numbers.reverse()
print("reverse():", numbers)

# Sort the list
numbers.sort()
print("sort():", numbers)

# Create a copy of the list
copy_list = numbers.copy()
print("Copied List:", copy_list)

# tuple operations

# Create a tuple with 8 elements
fruits = ("Apple", "Banana", "Orange", "Mango", "Grapes", "Apple", "Pineapple", "Cherry")

print("Tuple:", fruits)

# Count occurrences of an element
print("Count of Apple:", fruits.count("Apple"))

# Find index of an element
print("Index of Mango:", fruits.index("Mango"))

# Access tuple elements
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])
print("Fifth Element:", fruits[4])

# tuple unpacking
student = ("Suresh", 21, "Chennai")

# Unpack the tuple
name, age, city = student

# Print variables
print("Name:", name)
print("Age:", age)
print("City:", city)

#list unpacking
colors = ["Red", "Green", "Blue"]

# Unpack the list
color1, color2, color3 = colors

# Print variables
print("First Color:", color1)
print("Second Color:", color2)
print("Third Color:", color3)