# Homework - Pyramid

1. Pyramid
- Create a file named `{yourlastname}pyramid.py`.
- Write a program that prints out a pyramid that looks like this:

		       #
		      ##
		     ###
		    ####
		   #####
		  ######
		 #######
		########

- Each hash (`#`) is a bit taller than it is wide, so the pyramid itself is also be taller than it is wide.
- Have a variable named `stacks` that decides how tall the pyramid should be for a positive integer between 1 and 8.
- Ask the user how tall (1 ~ 8) the pyramid should be.
- If the number is out of range, make sure to let the user know and exit the program.
- Here's how the program might work when the `stack` variable is `8`:

		       #
		      ##
		     ###
		    ####
		   #####
		  ######
		 #######
		########

- Here's how the program might work when the `stack` variable is `4`:

		   #
		  ##
		 ###
		####

- Here's how the program might work when the `stack` variable is `2`:

		 #
		##

- Here's how the program might work when the `stack` variable is `1`:

		#

- Just as Scratch has a `Repeat` block, so does Python have a `for` loop, via which you can iterate some number of times. Perhaps on each iteration, `i`, you could print that many hashes?
- You can actually *nest* loops, iterating with one variable (e.g., `i`) in the *outer* loop and another (e.g., `j`) in the *inner* loop. For instance, here's how you might print a square of height and width `n`, below. Of course, it's not a square that you want to print :)

```python
for i in range(num):
  for j in range(num):
    print('#', end='')
  print()
```

2. FizzBuzz
- Create a file named `{yourlastname}fizzbuzz.py`.
- Write a Python program that prints all the integers between 1 and 100, except in three situations:

If an integer in the counter is divisible by 3, print "Fizz";

if an integer in the counter is divisible by 5, print "Buzz";

if an integer in the counter is divisible by both 3 and 5, print "FizzBuzz".

The first 5 integers in the console should look like this:
<pre>
						1
						2
						Fizz
						4
						Buzz
</pre>

3. SUBMIT (as a link in the OL to an assignment folder in *your* GitHub repository):
	- Your two .py files
	- A documentation file (in Markdown as an .md file!) that includes information about both .py files as outlined in the syllabus.
