
m=False

    
def setup():
    size(500,500)
def draw():
    fill(255,0,0)
    text("B",25,25)
    global m
    background(255)
    if m:
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'b' or key == 'B':
            m=True
    rect(25, 25, 50, 50)
