
a=False
p=False
l=False 
e=False
    
def setup():
    size(500,500)
def draw():
    global a, p, l, e
    background(255)
    fill(255,0,0)
    textSize(32)
    text("apple",25,35)
    if a :
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'a' or key == 'A':
            a=True
    rect(25, 10, 18, 30)
    
    if p :
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'p' or key == 'P':
            p=True
    rect(43, 10, 20, 30)
    
    if p :
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'p' or key == 'P':
            p=True
    rect(63, 10, 20, 30)
    
    if l :
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'l' or key == 'L':
            l=True
    rect(83, 10, 10, 30)
    
    if e :
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'e' or key == 'E':
            e=True
    rect(93, 10, 20, 30)
