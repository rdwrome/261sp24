'''
- Ask the user to input a positive integer number.
- Store the input to the `count_down` integer variable.
- Use a while loop to count down the number until and including 0 using `count_down`.
- Print out a character + as much as the `count_down` variable in one line.
- Hint: You can use the `end` parameter for the `print()` function to change what character gets printed out last.
'''
count_down = int(input("Enter a positive integer number: "))

while count_down >= 0:
  print('+', end='')
  count_down -= 1
print()