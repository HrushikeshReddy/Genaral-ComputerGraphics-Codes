x=60;
xd=10;
y=60;
yd=10;
    
def setup():
    size(500,500);
    background(0);
    
def draw():
    global x;
    fill(255,0,0);
    rect(0,480,500,70);
    fill(255);
    ellipse(x,y,20,20);
    rect(200,445,40,30);
    fill(255);
    
def keyReleased():
    global x;
    global y;
    if(key==CODED):
        if(keyCode==RIGHT):
            if(x==500):
                x=500;
            elif(x<500):
                background(0);
                x=x+10;
        elif(keyCode==LEFT):
            if(x==20):
                x=20;
            elif(x>20):
                background(0);
                x=x-10;
        if(keyCode==DOWN):
            if(y==500):
                y=500;
            elif(y<500):
                background(0);
                y=y+10;
        elif(keyCode==UP):
            if(y==20):
                y=20;
            elif(y>20):
                background(0);
                y=y-10;
