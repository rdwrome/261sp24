'''
- Ask the user to enter a number and then enter another number. 
- Add these two numbers together and then ask if they want to add another. 
- If they enter `"y"`, ask them to enter  another number and keep adding numbers until they do not answer "y". 
- Once the loop has stopped, display the total.
'''

num = int(input("Enter a number: "))
total = num
again = 'y'

while again == 'y':
  num = int(input("Enter another number: "))
  total += num
  again = input("Do you want to add another number? (y/n)")

print(f"The total is {total}")
