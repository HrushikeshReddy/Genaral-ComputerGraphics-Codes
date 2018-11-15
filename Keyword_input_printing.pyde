def setup():
    global viewport;
    size(800,800,P3D);
    background('#33C2F2');
    
def draw():
    fill(40,20);
    rect(0,0,width,height);
    
def keyPressed():
    fill('#FFE200');
    textSize(random(20,200));
    text(key,random(300),random(100,400));
