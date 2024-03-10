'''
- Ask the user to input an integer number.
- Determine if the number is negative, positive, or 0.
- Exit the program when the user types in 9.
'''

num = 0

while num != 9:
  num = int(input("Enter an integer number: "))
  if num == 0:
    print("The number you entered is 0.")
  elif num > 0:
    print("The number you entered is positive.")
  else:
    print("The number you entered is negative.")

print("Exiting program!!")
