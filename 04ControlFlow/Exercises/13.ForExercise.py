'''
- Ask the user to input a positive integer number.
- Store the input to the `num` integer variable.
- Create a variable named sum and initialize it to 0.
- Use `for-loop` to sum every number up to and including `num` into the `sum` variable.
- Print out the `sum` variable after summing is done.
- *Do not use an `if` statement for this exercise.*
'''

num = int(input("Enter a positive integer number: "))
sum = 0

for index in range(num + 1):
  sum += index

print(sum)