'''
- Write a Python program that uses `for` and `if` statements.
- Ask the user to input an integer number.
- Print out all the divisors of the number that the user typed in.
'''

num = int(input("Enter an integer number: "))

for index in range(1, num):
  if(num % index == 0):
    print(f"{index} is a divisor of {num}")