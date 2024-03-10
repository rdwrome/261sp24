def get_radius(circumference):
  return circumference / 3.14 / 2

number = int(input("Enter a circumference of circle: "))
print(f"The radius of circle with circumference of {number} is {get_radius(number)}")