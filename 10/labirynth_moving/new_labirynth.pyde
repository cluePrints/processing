sprite_width = 64
sprite_height = 64
hero_x = 1
hero_y = 1
labirynth_map = [
                 "########",
                 "#      #",
                 "##   ~ #",
                 "#      #",
                 "#      #",
                 "########"
                 ]
labirynth_width = len(labirynth_map[0])
labirynth_height = len(labirynth_map)

def setup():
    size(500, 500)
    
def draw():
    cleanup()
    draw_labirynth()
    draw_hero()
    
def keyPressed():
    move_hero()
    
def draw_hero():
    hero_image = loadImage("hero.png")
    draw_image(hero_image, hero_x, hero_y)
    
def cleanup():
    background(0)

def draw_labirynth():    
    wall_image = loadImage("wall.jpeg")
    water_image = loadImage("water.jpeg")
    for pos_x in range(labirynth_width):
        for pos_y in range(labirynth_height):
            if labirynth_map[pos_y][pos_x] == '#':
                draw_image(wall_image, pos_x, pos_y)
    
            if labirynth_map[pos_y][pos_x] == '~':
                draw_image(water_image, pos_x, pos_y)

def draw_image(img, game_x, game_y):
    image(img, game_x*sprite_width, game_y*sprite_height, sprite_width, sprite_height)
    
def move_hero():
    global hero_x, hero_y
    if (keyCode == UP):
        if (labirynth_map[hero_y - 1][hero_x] != '#'):
            hero_y = hero_y - 1
    if (keyCode == DOWN):
        if (labirynth_map[hero_y + 1][hero_x] != '#'):
            hero_y = hero_y + 1
    if (keyCode == RIGHT):
        if (labirynth_map[hero_y][hero_x + 1] != '#'):
            hero_x = hero_x + 1
    if (keyCode == LEFT):
        if (labirynth_map[hero_y][hero_x - 1] != '#'):
            hero_x = hero_x - 1
