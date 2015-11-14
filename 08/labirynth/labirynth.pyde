sprite_width = 64
sprite_height = 64

labirynth_map = [
                 "#########",
                 "# #     #",
                 "# #     #",
                 "# #     #",
                 "#       #",
                 "#########"
                 ]


labirynth_height = len(labirynth_map)
labirynth_width = len(labirynth_map[0])


hero_x = 1
hero_y = 1

def setup():
    size(800, 600);

def draw():
    global hero_x, hero_y
    
    wall_image = loadImage("wall.jpeg")
    hero_image = loadImage("hero.png")
    water_image = loadImage("water.jpeg")
    blank_image = loadImage("blank.png")

    for y in range(0, labirynth_height):
        for x in range(0, labirynth_width):
            screen_x = sprite_width * x;
            screen_y = sprite_height * y;
            if (labirynth_map[y][x] == '#'):
                image(wall_image, screen_x, screen_y, sprite_width, sprite_height)
                
    hero_screen_x = sprite_width * hero_x;
    hero_screen_y = sprite_height * hero_y
    image(hero_image, hero_screen_x, hero_screen_y, sprite_width, sprite_height)
