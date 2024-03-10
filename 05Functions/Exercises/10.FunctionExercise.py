def read_integer():
  number = 0
  while number <= 0:
    number = int(input("Enter a positive number: "))
  return number

print("The number that user entered is: ", read_integer())