# Create string variables
first_name = "Suresh"
last_name = "V"
city = "Arni"

print("First Name:", first_name)
print("Last Name:", last_name)
print("City:", city)


# Concatenate first name and last name
full_name = first_name + " " + last_name
print("Full Name:", full_name)


# Repeat city name 3 times
print("City repeated 3 times:", city * 3)


# String case methods
print("Upper Case:", full_name.upper())
print("Lower Case:", full_name.lower())
print("Title Case:", full_name.title())
print("Capitalize:", full_name.capitalize())


# Strip methods
text = "   Python Programming   "
print("After strip():", text.strip())
print("After lstrip():", text.lstrip())
print("After rstrip():", text.rstrip())


# Split a sentence into a list
sentence = "Python is easy to learn"
words = sentence.split()
print("After split():", words)


# Join a list into a sentence
language = ["Python", "is", "easy", "to", "learn"]
new_sentence = " ".join(language)
print("After join():", new_sentence)


# Find a substring
print("Position of 'easy':", sentence.find("easy"))


# Count occurrences of a character
print("Count of 'a':", sentence.count("a"))


# String checking methods
print("Starts with 'Python':", sentence.startswith("Python"))
print("Ends with 'learn':", sentence.endswith("learn"))


name = "Suresh"
number = "12345"
mix = "Python123"

print("isalpha():", name.isalpha())
print("isdigit():", number.isdigit())
print("isalnum():", mix.isalnum())


# Formatted string
age = 21
print(f"My name is {first_name} {last_name}. I am {age} years old and I live in {city}.")


# Escape Character - New Line-\n
print("Python\nProgramming")


# Escape Character - Tab-\t
print("Suresh\t21\tArni")