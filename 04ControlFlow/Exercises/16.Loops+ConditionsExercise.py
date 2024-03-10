'''
- Ask the user to enter a number. 
- If they enter a value under 10, display the message “Too low” and ask them to try again. 
- If they enter a value above 20, display the message “Too high”  and ask them to try again. 
- Keep repeating this until they enter a value between 10 and 20 and then display the  message “Thank you”. 
'''

num = int(input("Enter a number between 10 and 20: "))

while num < 10 or num > 20:
  if num < 10:
    print("Too Low")
  else:
    print("Too High")
  num = int(input("Enter a number between 10 and 20: "))