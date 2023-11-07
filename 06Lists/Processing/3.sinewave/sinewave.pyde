sine_wave = []

def setup():
    size(100,100)
    for i in range(width):
        radian = map(i, 0, width, 0, TWO_PI)
        sine_wave.append(abs(sin(radian)))
        
def draw():
    for i in range(width):
        stroke(sine_wave[i] * 255)
        line(i, 0, i, height)
        
