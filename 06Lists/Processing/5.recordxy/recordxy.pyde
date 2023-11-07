num = 50
x = []
y = []

def setup():
   size(100, 100)
   for i in range(50):
       x.append(0)
       y.append(0)
   noStroke()
   fill(255, 102)

def draw():
    background(0)
    for i in range(num - 1, 0, -1):
        x[i] = x[i - 1]
        y[i] = y[i - 1]
    
    x[0] = mouseX
    y[0] = mouseY
    
    for i in range(i, num):
        ellipse(x[i], y[i], i / 2, i / 2)
