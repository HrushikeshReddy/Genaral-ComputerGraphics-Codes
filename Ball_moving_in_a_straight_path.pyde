c=color(0)
x=0.0
y=400.0
speed=2.0

def setup():
    size(500,600)
    
def draw():
    background(0)
    move()
    display()
    fill(255,0,0)
    rect(0,500,500,100)
    
def move():
    global x
    x=x+speed
    if x>width:
        x=0
    
def display():
    fill(255)
    ellipse(x+50,y+50,100,100)
