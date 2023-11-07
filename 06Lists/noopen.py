#answer with nested function definitions
def get_power(x, n):
    return x**n

def print_grapha():
    for i in range(-8, 9):
        y = get_power(i, 2)
        for j in range(0, y):
            print('*', end='')
        print()

#slightly more efficient answer without x, n and the nested function            
def print_graphb():
    for i in range(-8, 9):
        for j in range(0, i**2):
            print('*', end='')
        print()


    
