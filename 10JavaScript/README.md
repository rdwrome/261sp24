# JavaScript

## Final Project Proposals?

## Creative Coding Minor Refresher

## JavaScript

**Why?**

- Makes websites dynamic
- Both compiled and OOP
- Browser console
- Chrome Developer Tools
- Helpful:
```javascript
	console.log()
	console.clear()
```

**Values and Operators**

- Numbers
	- 8 bytes of memory each, so can be +/- 9 Quadrillion
	- Decimals (not just integers)

- Simple Unary and Binary Operators

```javascript
	typeof
	- (unary and binary)
	+
	/
	*
	++ (shorthand counter up)
	-- (shorthand counter down)
	%
```
- Strings
	- “Bound by Quotations”
	- Can’t be divided, multiplied, subtracted
	- String literal

	```javascript
	`${9/3} little pigs`
	```
- Comparison Operators

```javascript
	> greater than
	< less than
	>= greater than or equal to
	<= less than or equal to
	== equal to
	!= not equal to
```
- Logical Operators

```javascript
	&& and/both
	|| or/either
	! not (like logical negative sign)
```
- Conditional/Ternary Operator
	 - condition ? expression1 : expression2

		```javascript
		let height = prompt('what is your height in inches?');
		let pass = (height > 48) ? "Yes, you may ride the rollercoaster." : "Sorry, you may not ride the rollercoaster.";
		console.log(pass);
		```
- NaN and Empty Values
	- NaN = not a number but *should* have been a number
	- null, undefined = can't compute

**Some Syntax**

- Automatic Type Conversion
- indentation and semi-colons
- Capitalization
- Commenting

**Expressions and Statements**
- Expression: a piece of code that produces a value
- Statement: expressions nested together to form a whole
- Block: thread of statements

**Bindings**

- Environment
- let (can be rebound anytime) vs const (can't be rebound within a block) vs var (works, is just old-school)
- Naming Bindings and Keywords
- scopes
	- local: created and can only be referenced within a function (accidental)
	- global: defined outside of block and can be referenced anywhere (key signature)
	- scoping scope: can look out into environment

## Subfolder examples

**Debugging in JS**

- "use strict" (use strict example)
- global scope?
- local scope?
- no undeclared bindings
- no escape characters
- [unit testing: a program that verifies part of your code](https://www.smashingmagazine.com/2012/06/introduction-to-javascript-unit-testing/)

## [Propriety JS vs JS](https://www.gnu.org/philosophy/javascript-trap.en.html)
- [Human Rights Watch](https://www.hrw.org/report/2022/05/25/how-dare-they-peep-my-private-life/childrens-rights-violations-governments)
- [UN](https://www.ohchr.org/)

## Processing with JavaScript

## GitHub Branches

- Git manages version control for you.
- GitHub Desktop is an application that manages Git and syncs it between your local server (the harddrive of your computer) and your remote server (GitHub.com's cloud).
- So far, you've only used Git to version control independent projects.
- Now we're going to use a GitHub feature called **branches** to push changes you make to others and pull changes from others so that you can work collaboratively.
- [Anatomy of a Branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
- The central branch is called **main** (this is where your commits will go if no other branch is specified - but we don't want to edit the main branch if we're working collaboratively [used to be called "master"]).
- Branches exist as separate until a `merge` is executed.
- To make a branch in the Github Desktop app, click on "Current Branch" in the top bar and then click "new branch".
- To checkout a branch in the Github Desktop app, click "Current Branch" and then click on the branch you'd like to checkout.
- To merge a branch on GitHub Desktop, click "Current Branch" and then "Choose a branch to merge into...".
- Individual branches: practice time; **main**/

## Rachel makes a branch of the class repository on rdwrome.github.io

## Everyone makes a branch of the class repository
- Before *anything* make sure you have pulled my most up-to-date main branch!
- Create your own branch of the class repository
- Edit under your family name in branchesdemo.md in this folder
- Merge your changes to the main branch!
