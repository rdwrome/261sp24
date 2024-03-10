def max3(a, b, c):
  max = a
  if b > max:
    max = b
  if c > max:
    max = c
  return max

x = int(input("Enter the first integer number: "))
y = int(input("Enter the second integer number: "))
z = int(input("Enter the third integer number: "))

print(f"The maximum number of", x, y, z, "is:", max3(x,y,z))