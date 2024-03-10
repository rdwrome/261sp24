def sqr(n):
  return n * n

def pow4(n):
  return sqr(n) * sqr(n)

number = int(input("Enter an integer number: "))
print(f"{number} to the power of 4 is:", pow4(number))