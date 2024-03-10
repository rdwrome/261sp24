'''
- Write a Python program that asks the user to input three integers.
- Compare the three values and determine whether three numbers are equal, two are equal, or none are equal.
- Print out the following lines based on the result:

Three numbers are equal.
Two numbers are equal.
None are equal.
'''

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first == second == third:
  print("Three numbers are equal.")
elif first == second or second == third or third == first:
  print("Two numbers are equal.")
else:
  print("None are equal.")