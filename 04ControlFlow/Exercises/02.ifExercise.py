'''
- Write a Python program that asks the user to input an integer number and displays the absolute value of that number. 
- Here is an example printout when the input value is -11:

The absolute value is 11
'''

number = int(input("Enter a number: "))

if number < 0:
  number = -number  
  
print(f"The absolute value is {number}.")