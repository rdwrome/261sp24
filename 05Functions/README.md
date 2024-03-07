# Functions

## Functions
- takes input value, does a process to it, returns an output value
- we've been using many that are already built-in python (print, type, range), now we'll write our own!

- Function Definition + Call
  - definition has to come before call, but call happens where call happens
```python
#function
def circle_area(x):
  return x * x * 3.14
#call
print(circle_area(3.0))
```

- See LoopvsFunction.pdf in this folder

- Function with one argument/parameter
```python
#function
def cube(n):
  return n * n * n
#call
print(cube(2))
```

- Function with Multiple Inputs
```python
#function
def sqr(x, n):
  return x ** n # remember what this means?
#call
print(sqr(2, 3))
```

- Passing parameters into function argument calls
```python
def get_radius(circumference):
  return circumference / 3.14 / 2
number = 15
print(f"The radius of circle with circumference of {number} is {get_radius(number)}")
```
```python
def sqr(x, n):
  return x ** n
base = 2
exponent = 3
print(f"{base} to the power of {exponent} is:", sqr(base, exponent))
```

- Nesting Function Calls
```python
def print_lyrics():
  print("I'm gonna take my horse to the old town road.")
  print("I'm gonna ride 'til I can't no more.")

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

print(repeat_lyrics())
```
```python

def sqr(n):
  return n * n

def pow4(n):
  return sqr(n) * sqr(n)

print(pow4(2))
```

- Multiple Outputs
```python
def getInstruments():
  return 'Drum', 'Guitar', 'Bass'

primary, secondary, tertiary = getInstruments()

print("My Instruments are: ", primary, secondary, tertiary)
```

- Function with if
```python
def minimum(x,y):
  if x < y:
    return x
  return y
print(minimum (3, 4))
```
- Function with if/else
```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

n = 3

print(f"Factorial of {n} is {factorial(n)}")
```
- Functions with for loops
```python
def func(count):
  for i in range(count + 1):
    print(f"{count - i} Lovely!")
print(func(5))
```
```python
def sumup(n):
  sum = 0
  for i in range(n + 1):
    sum += i
  return sum
print(sumup(5))
```

## Variables
- Where they hold meaning is called their **scope**
### Local Variables
 - Only hold meaning with single function calls
 - "the accidental of variables"
 -
 ```python
 def print_favorite_instrument():
   instrument = input("What is your favorite instrument? ")
   print("Your favorite instrument is: ", instrument)

 def print_least_favorite_instrument():
   instrument = input("What is your least favorite instrument? ")
   print("Your least favorite instrument is: ", instrument)

 print_favorite_instrument()
 print_least_favorite_instrument()
```
### Global Variables
  - persist between function calls
  - can be called from within a function with the keyword `global`
  - mostly used for boolean statements
  - "the keysignature of variables"
  - see the Processing folder

## Functions in Processing

## The midterm is coming

## Pyramids and FizzBuzz!

## For Next Week: Power.md
