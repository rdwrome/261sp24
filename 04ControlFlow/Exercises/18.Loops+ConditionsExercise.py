'''
- Write a Python program that uses `for` and `if` statements.
- Write a Python program to print those numbers divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''

for index in range(1500, 2701, 1):
  if index % 7 == 0 and index % 5 == 0:
    print(index)
