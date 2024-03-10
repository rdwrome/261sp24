'''
- Ask the user to input a positive integer number.
- Store the input to the `count_up` integer variable.
- Use `for` loop to count up the number from 0 using `count_up`.
- Print out only the odd numbers of the `count_up` numbers.
- Do not use an `if` statement for this exercise.
'''

count_up = int(input("Enter a positive integer number: "))

for index in range(1, count_up, 2):
  print(index)
