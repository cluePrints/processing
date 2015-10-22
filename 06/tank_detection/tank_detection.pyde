tank_color = 0xFF9B9878
tree_color = 0xFF5F8050
red_color = 0xFFC00000

def setup():
    size(800, 600);
    tank_image = loadImage("tank.png")
    image(tank_image, 0, 0, width, height);
    
    global tank_x, tank_y
    tank_x = width/2
    tank_y = height/2
    
    search_color = tank_color
    tank_x = -1
    tank_y = -1
    for y in range(0, height):
        for x in range(0, width):
            if (get(x, y) == tree_color):
                tank_x = x;
                tank_y = y;
    
def draw():
    strokeWeight(1);
    stroke(red_color);
    noFill();
    rect(tank_x-30, tank_y-30, 60, 60);
    
    strokeWeight(5);
    point(tank_x, tank_y);
    
def mouseClicked():
    point_color = get(mouseX, mouseY);
    print("You clicked point with color equal to: 0x" + hex(point_color))
