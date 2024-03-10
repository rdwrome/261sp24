def print_stars(n):
  while n > 0:
    print('*',end='')
    n -= 1
  print()

number = int(input("Enter an integer number: "))
print_stars(number)