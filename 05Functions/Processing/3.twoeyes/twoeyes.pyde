def setup():
    size(100, 100)
    noStroke()
    
def draw():
    background(204)
    # Right Eye
    fill(255)
    ellipse(65, 44, 60, 60)
    fill(0)
    ellipse(75, 44, 30, 30)
    fill(255)
    ellipse(81, 39, 6, 6)
    # Left Eye
    fill(255)
    ellipse(20, 50, 60, 60)
    fill(0)
    ellipse(30, 50, 30, 30)
    fill(255)
    ellipse(36, 45, 6, 6)
