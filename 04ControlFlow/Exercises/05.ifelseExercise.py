'''
- Write a Python program that asks the user to input an integer number and determine whether the number is even or odd.
- In this program, ensure that the number input from the user is positive.
- Print out whether the number is even or odd.
- If the number is invalid, print out that the number needs to be positive.
'''

number = int(input("Enter an integer number: "))

if number > 0:
  if number % 2:
    print("The number is odd.")
  else:
    print("The number is even.")
else:
  print("The number you enter must be a positive number.")

