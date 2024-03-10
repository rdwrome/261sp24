'''
- Write a Python program that asks the user to input two integer numbers.
- Find out if the second input is a divisor of the first input.
- If the second input is a divisor (i.e., first: 9, second: 3), print out the following:

3 is a divisor of 9

- If the second input is not a divisor (i.e., first: 17, second: 5), print out the following:

5 is not a divisor of 17
'''

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

# First way of doing this
if first % second == 0:
  print(f"{second} is a divisor of {first}")
else:
  print(f"{second} is not a divisor of {first}")

# Second way of doing this
if first % second:
  print(f"{second} is not a divisor of {first}")
else:
  print(f"{second} is a divisor of {first}")