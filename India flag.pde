int radius=20;
int pointAngle=360/24;
 
void setup(){
     size(600,600);
 }
 
void draw(){
     fill(255,165,0);
     rect(300,300,200,40);
  
     fill(255);
     rect(300,340,200,40);
  
     fill(0,238,0);
     rect(300,380,200,40);
  
  noFill();
  ellipseMode(CENTER);
  ellipse(400,360,40,40);
  
  
  for(float angle = 0; angle < 360; angle = angle+pointAngle) { 
  float x = cos(radians(angle)) * radius; 
  float y = sin(radians(angle)) * radius;
  line(x+400, y+360, 400, 360); 
  
   }  
}
