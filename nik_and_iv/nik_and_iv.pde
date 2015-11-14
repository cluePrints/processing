x=250;
y=250;
direction = 5;
def setup():
  size(500, 500);
  
def draw():
  global x, y
  x = x+0
  y = y+5
  if (100 < y < 300):
      y = y+direction
      
  background(70,60,190);
  fill(63);
  rect(10,10,480,480);
  eclipse(x,y, 50, 50);
  rect(150,50,200,20);
  rect(150,430,200,20);
