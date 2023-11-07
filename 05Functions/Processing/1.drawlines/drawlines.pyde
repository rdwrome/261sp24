y = 0

def setup():
    size(300, 300)

def draw():
    global y
    line(0, y, 300, y)
    y = y + 4
