def print_characters(character, count):
  while count > 0:
    print(character, end='')
    count -= 1

count = int(input("How many lines?: "))
for i in range(1, count + 1):
  print_characters(' ', count - i)
  print_characters('*', i)
  print()