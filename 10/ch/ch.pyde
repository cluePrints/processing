def setup():
    size(300, 300)
    
def draw():
    draw_cherry(100, 100)
    draw_cherry(0, 0)
    
def draw_cherry(x, y):
    # anyone remembers which color this will be? 
    fill(255, 100, 100);
    ellipse(x + 50, y + 50 + 20, 50, 50);
    ellipse(x + 100, y + 50 + 20, 50, 50);
    line(x + 50, y + 25 + 20, x + 90, y);
    line(x + 100, y + 25 + 20, x + 90, y);
    # RGB anyone?
    fill(100, 255, 100);
    translate(x + 90+20, y +20)
    rotate(PI/4);
    ellipse(0, 0, 50, 20);
    rotate(-PI/4);
    translate(-x -90+20, -y -20);
    
