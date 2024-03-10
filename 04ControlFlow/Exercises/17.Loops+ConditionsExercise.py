'''
- Ask which direction the user wants to count with `‘u’` or `‘d’` (up or down). 
- If they select `‘u’`, ask them for the top number and count from 1 to that number. 
- If they select `‘d’`, ask them to enter a number below 20 and then count down from 20 to that number. 
- If they entered something other than up or down, display the message “I don’t understand”.
'''

direction = input("Do you want to count up or down? (u/d)")

if direction == 'u':
  num = int(input("What is the top number?"))
  for index in range(1, num + 1):
    print(index)
elif direction == 'd':
  num = int(input("Enter a number below 20: "))
  for index in range(20, num - 1, -1):
    print(index)
else:
  print("I don't understand")

