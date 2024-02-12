## Variables & Operators

**Y'all Pull**

**A Caveat About the Readings**
- Readings are theory and a little ahead of practice for next few weeks

**Python**
- High-level
- Interpreted
- Object-oriented
- *Do we have it???*

**Objects**
- Made up up values (result of calculation) and variables
- What Python manipulates
- Almost everything in Python is an object
- Every object has a **type** that defines the kinds of things that programs can do with that object

**Data Types**
- Python has a built in function called **type()** to learn the type of an object
- These are the four types we'll deal with in Python
- CODE ALONG
```Python
print(type(10)) #integer
print(type(10.)) #float
print(type("hello,world")) #string
print(type(True)) #boolean
```
**Operators**
- Used to perform operations on objects
- Also sometimes called "operands"
- Simple
```Python
+
-
*
/
% - modulus (divides and then *returns* the remainder) i.e. clocks.
// - floor division (ignores the remainder) i.e. 6//4 is 1 because 4 only goes into 6 once.
** - raised to the power of
```
- PEMDAS (parentheses, exponents, multiplication, division, addition, subtraction) applies!

- Boolean/Comparison
	- Checks for truth!
![Boolean Diagram](bool.png)

**Expressions**
- "Values, Variables and Operators" - Think Python, Chapter 2

**Statements**
- "A unit of code that has an effect...The interpreter executes it." - Think Python, Chapter 2

**Variables**
- Declare a variable, bind an object to it with the = operator, now you've created an assignment statement
- Variables are really easy to bind and rebind
- CODE ALONG
```Python
one = 1
two = 2
cat = one + two
print(cat)
```
**Naming Variables and Keywords**
- You also can't use special characters other than _
- Variable names should start with letters
- They're case sensitive
- You can't use the words below to declare variables because they're keywords
```Python
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```

## Strings
```Python
#len function
print(len('rachel devorah wood rome'))
#indexing
myName = 'rachel'
print(myName[3])
#slicing
print(myName[0:3])
print(myName[2:4])
#concatenation
print('yum'+'my')
print('yum' * 3)
```

## Input and Output
- Get String
```Python
str = input("Name: ")
print("Hello,", str)
```
- Printing paramenters and f-String
```Python
print("Hello,", str, sep='')
print(f"Hello, {str}")
```

- Type Casting
```Python
i = int(input("What's your favorite number? "))
print(f"Your favorite number is {i}")
```

- Printing floating points
	- what is π?
```Python
z = 3.14159265358979323846264338327950288419716939937510
print(f"{z}")
print(f"{z:.50f}")
```
- f-String math
	- int
```Python
bags = 3
bananas = 12
print(f"{bananas} bananas were split into {int(bananas / bags)}groups to fit into {bags} bags.")
```
- Special characters
- tab and new line
```Python
print("col1\tcol2\tcol3\ncol1\tcol2\tcol3\ncol1\tcol2\tcol3")
```
## Exersize:
- Write a program that converts 99 Fahrenheit to Celsius
- Create two variables, **f** and **c**
- Use the equation:
	- Celsius = (Fahrenheit - 32)  5 / 9

## Object-oriented programming
- Some languages can do it, some languages must do it, e.g. javaScript *can* do it, Python *must* do it
- Principles of OOP
    - Encapsulation
  		- object: independent part of the program that manages itself (own rules and ways of doing things)
      - objects are made up of values + variables
      - objects are what Python manipulates
      - objects are reusable
      - a specific realization of an object is a
  	- Inheritance
      - objects get their functions from classes
      - class: template, blueprint for creating objects
  		- superclass is parent, class is child
  		- class inherits attributes of parent (through abstraction) but modifies, evolves
      - classes are reusable
  	- Polymorphism
  		- change the way something works by overriding and overloading
      - change type, have multiple types work together
  		- overriding: walk to moon walk
  		- overloading: walk to

## [Processing](https://processing.org/download) (install & setup for Python)

## For Next Week: Mice.md in this week's 261 repo subfolder! Code + Documentation, as always.
