```
- Write a Python program that uses nested `for-loops`.
- The first `for-loop` should increment a variable `i` starting from 0 and ending at 10.
- The second `for-loop` should increment a variable `j` beginning from 0 and ending at 10.
- Print the value of `j` without new lines when `j` is greater than or equal to `i`.
- Print a new line every time the for-loop for `j` ends.
```

for i in range(10):
  for j in range(10):
    if j >= i:
      print(j, end='')
  print()