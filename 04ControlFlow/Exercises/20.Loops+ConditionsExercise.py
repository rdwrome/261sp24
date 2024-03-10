'''
- Write a Python program that uses `for` and `if` statements.
- Ask the user to input a number and check to ensure the number is greater than 0.
- Print * as many as the user’s input.
- Start a new line every 5 *’s.
'''

num = int(input("Enter a number: "))

if num > 0:
  for index in range(num):
    print('*', end='')
    if index % 5 == 4:
      print()
