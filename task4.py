# Program to print numbers from 1 to 20 using while loop
i = 1
while i <= 20:
    print(i)
    i += 1


# Program to print even numbers from 1 to 50
i = 2
while i <= 50:
    print(i)
    i += 2


# Program to print multiplication table using while loop
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


 # Program to find sum of first 10 natural numbers
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1

print("Sum =", sum)


# Get number from user
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed Number =", reverse)


# Program to print numbers from 1 to 20
for i in range(1, 21):
    print(i)


# Program to print odd numbers from 1 to 50
for i in range(1, 51, 2):
    print(i)


# Program to print each character of a string
text = input("Enter a string: ")
for ch in text:
    print(ch)


# Program to print multiplication table using for loop
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Program to find factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)


# Demonstration of range(length)
for i in range(5):
    print(i)


# Demonstration of range(start, end)
for i in range(5, 11):
    print(i)


# Demonstration of range(start, end, step)
for i in range(2, 21, 2):
    print(i)


# Program to stop the loop when number 7 is encountered
for i in range(1, 11):
    if i == 7:
        break
    print(i)


# Program to skip even numbers between 1 and 20
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)


# Program to print characters while skipping vowels
text = input("Enter a string: ")
for ch in text:
    if ch in "aeiou":
        continue
    print(ch)