'''
- Write a Python program that asks the user to input an integer number.
- Use the if statement to determine whether the number entered by the user is the dividend of 10 without any remainders.
- If the number is not a dividend of 10 (for example, 13), print out the following:

The number 13 is not a dividend of 10.
'''

number = int(input("Type in an integer number: "))

# First way of doing it
if number % 10 > 0:
  print(f"The number {number} is not a dividend of 10.")

# Second way of doing it (simpler)
# Python interprets numbers greater than 0 as the Boolean True value
if number % 10:
  print(f"The number {number} is not a dividend of 10.")