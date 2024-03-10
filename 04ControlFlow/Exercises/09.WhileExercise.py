'''
- Ask the user to input a positive integer number.
- Store the input to the `max` integer variable.
- Create a variable named `count_up` and initialize it to 0.
- Use a while loop to count the number from 0 until `max` using `count_up`.
- Print out only the even numbers in the `count_up`.
- *Do not use an `if` statement for this exercise.*
'''

max = int(input("Enter a positive integer number: "))
count_up = 0

while count_up <= max:
  print(count_up)
  count_up += 2
