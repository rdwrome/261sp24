def sqr(x, n):
  return x ** n

base = int(input("Enter an integer number: "))
exponent = int(input("Enter another integer number: "))
print(f"{base} to the power of {exponent} is:", sqr(base, exponent))