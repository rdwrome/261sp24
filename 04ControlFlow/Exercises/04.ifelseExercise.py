'''
- Write a Python program that asks the user to input two integer numbers.
- Determine the difference between the two numbers.
- You must display the difference in a positive number.
- Here is an example output when the user inputs 2 and 10:

The difference between 2 and 10 is 8
'''

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
difference = 0

if first > second:
  difference = first - second
else:
  difference = second - first

print(f"The difference between {first} and {second} is {difference}")

#Another way
# difference = first - second
# if difference < 0:
#   difference = -difference