y = []

def setup():
    size(100, 100)
    for i in range(width):
        y.append(height/2)
    
def draw():
    background(204)
    for i in range(len(y) - 1, 0, -1):
        y[i] = y[i - 1]
    
    y[0] = mouseY
    for i in range(1, width):
        line(i, y[i], i - 1, y[i - 1])
