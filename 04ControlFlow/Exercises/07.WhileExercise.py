'''
- Ask the user to input a positive integer number.
- Store the input to the `count_down` integer variable.
- Use a while loop to count down the number until and including 0 using `count_down`.
- Print out the countdown numbers.
'''

count_down = int(input("Enter a positive integer number: "))

while count_down >= 0:
  print(count_down)
  count_down -= 1