# Python

## Made from Scratch!

## Intro to Python
- High-level = human-readable!
- General but!
	- [Modules and libraries can make it more specific](https://wiki.python.org/moin/UsefulModules)
		- Modules: simple .py file that "abstracts out" specific information (functions, variables, other things)
		- libraries (or packages) are a collection of modules
- Interpreted (executed by the interpreter vs. compiled)
  - Easier to debug
  - Runs a little slower
- Object-oriented (much more on this later!)
- Scripts are a sequence of definitions and commands executed in the shell
- #nocommentcomment

## Python vs. Scratch (see .pdf in this folder)

**[Do You Have Python3?](https://www.python.org/downloads/)**

- More functional standard libraries than 2
- Some things only supported on 2, though
  - python --version
  - python3 --version
- IF YOU'VE DOWNLOADED PYTHON3 TODAY: open "update shell profile command" in the python3 folder
- Check your pip!
	- pip --version
	- pip3 --version

## CLI vs IDE

**Command Line Interfaces (CLI)**
- Most commonly used for compiled languages
- "under the hood"

***Most common commands***

	- `pwd` Print Working Directory (prints the path to the directory [folder] that you are currently in). Map+Compass.

	- `ls` Lists the files stored in the Working Directory

	- `cd` Change Directory (changes working directory to different directory)
		>You can type `cd` and then drag and drop the folder you'd like to work in, into the Terminal Window. This is much faster than typing out the full path.

	- `clear` clears the Terminal Window

	- `cd ~` change directory to your root directory (how to "go back")

	- `-o` tag to create an object file

	- `say` for fun

## CLI Exersize
	Find a [Haiku](https://www.poetryfoundation.org/learn/glossary-terms/haiku-or-hokku) or other very short poem, or a song lyric refrain. Record an .aiff audio file of your computer "saying" the poem with the CLI
		- Hints:
			- You'll need to use pwd, ls, and cd to make sure you create the .aiff file in a place you can easily find
			- You'll need to use -o:
				`say "hi" -o hi.aiff`

***More advanced commands***

	- `cp` Makes a copy of a file ("cp file.txt filecopy.txt" makes a copy of file.txt and names it filecopy.txt)

	- `mkdir` Makes a new directory (`mkdir NewDirectory` makes a new folder called `NewDirectory`)

	- `&&` Means "and also do this", helpful for inputing multiple commands in the same line

	- `man` opens the manual for Terminal commands ("man man" will open up the manual for the manual!)

	- `~` means home directory

	- `nano` is a text editor within Command-line Interface (isn't VSC great!)

**Additional resources for Terminal and CLI**
- [GNU Bash reference](http://www.gnu.org/software/bash/manual/bashref.html)
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
- [101 Bash Commands and Tips for Beginners to Experts](https://dev.to/awwsmm/101-bash-commands-and-tips-for-beginners-to-experts-30je)

**MAKE SURE your Macintosh HD is visible in your "Finder" Preferences**

**Integrated Development Environments (IDE)**
- Most commonly used for interpreted languages
- Interpreter helps you debug within the IDE

**Install the Python Extension in Pulsar**
- Packages>Open Package Manager>language-python?

**Running Python: hands.py**
  - CLI
  - IDE

## Debugging in general

- Frustrating
- Most of what programming is
- ALWAYS BE DOCUMENTING YOUR DEBUGGING!!! (ABDYD!!!)
- Think of it as detective work
	- You're given evidence  and have to infer what happened
- Or think of it as a science experiment
	- Analyze the error message + code together
	- Draft a theory as to why you got the bug (with notes!)
		- record of what you've tried to fix it
	- Make a test of your theory
	- Monitor your code with printing functions and breakpoints

## Bugs in the Wild

**Syntax**

- Your code broke a structure/expectation rule
- Classic problems:
	- keyword is a variable name
	- colon after for, while, if, and def statements
	- matching quotation marks in Strings
	- matching brackets
	- = instead of ==
	- indentation
	- ASCII issues

**Runtime**

- Something broke while it was running/just didn't run at all
- Classic problems:
	- Control Flow issues
	- Recursion

**Semantic**

- Something is not right and your computer doesn't know it but you do
- Hardest to figure out!
- Go back to Pseudocoding
- Break everything down into the smallest unit you can
