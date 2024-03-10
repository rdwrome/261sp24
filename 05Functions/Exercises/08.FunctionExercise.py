def sumup(n):
  sum = 0
  for i in range(n + 1):
    sum += i
  return sum

n = int(input("Enter an integer number: "))
print(f"The sum of all numbers from 1 to {n} is {sumup(n)}")