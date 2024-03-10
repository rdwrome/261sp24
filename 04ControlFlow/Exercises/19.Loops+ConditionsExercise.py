'''
- Write a Python program that uses nested `for` statements.
- Ask the user to input a number.
- Print a block of hashtags based on the user’s input.
- For example, if the user types in three, the program should print out the following:

###
###
###

- Hint: use the `end` parameter of the `print()` function.
'''

num = int(input("Enter a number: "))

for x in range(num):
  for y in range(num):
    print('#', end='')
  print()