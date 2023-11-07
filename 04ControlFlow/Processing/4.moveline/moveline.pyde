y = 0.0

def draw():
    global y
    background(204)
    line(0, y, 100, y)
    y = y + 0.5
    if y >= 100:
        y = 0
