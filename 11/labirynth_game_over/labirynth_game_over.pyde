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

game_state = "in_progress"

def setup():
    size(500, 500)
    
def draw():
    if (game_state == "in_progress"):
        draw_in_progress()
    else:
        draw_game_over()
        
def keyPressed():
    if (game_state == "in_progress"):
        process_keys_in_progress()
    if (game_state == "game_over"):
        process_keys_game_over()
        
def process_keys_game_over():
    enter_key_code = 10
    if (keyCode == enter_key_code):
        restart_game()
        
def restart_game():    
    global game_state, hero_x, hero_y
    game_state = "in_progress"
    hero_x = 1
    hero_y = 1
        
def process_keys_in_progress():
    move_hero()
    game_over_when_hero_in_water()
    
def game_over_when_hero_in_water():
    global game_state
    if (labirynth_map[hero_y][hero_x] == '~'):
        game_state = "game_over"
        
def draw_in_progress():
    cleanup()
    draw_labirynth()
    draw_hero()
    
def draw_hero():
    hero_image = loadImage("hero.png")
    draw_image(hero_image, hero_x, hero_y)
    
def draw_game_over():
    background(0)
    text("Game is over. Press ENTER key to restart", 50, 50)
    
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
