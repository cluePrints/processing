food_x_list = [14, 100]
food_y_list = [51, 62]
hero_x = 50
hero_y = 50
hero_radius = 5
food_color = 0xff00c000
hero_color = 0xffc00000
frames_per_sec = 30
create_food_every = 1

def setup():
    size(600, 600);
    frameRate(frames_per_sec);
    
def draw():
    background(255, 255, 255)
    
    global hero_radius
    fill(hero_color)
    ellipse(hero_x, hero_y, hero_radius, hero_radius)
    
    grabbed_food_idx = -1
    
    # draw the food
    for food_number in range(len(food_x_list)):
        food_x = food_x_list[food_number]
        food_y = food_y_list[food_number]        
        fill(food_color)
        ellipse(food_x, food_y, 5, 5);
        
    # find food grabbed by the player
    for food_number in range(len(food_x_list)):
        food_x = food_x_list[food_number]
        food_y = food_y_list[food_number] 
        if (abs(hero_x-food_x) < 5 and abs(hero_y-food_y) < 5):
            hero_radius = hero_radius + 5
            grabbed_food_idx = food_number
        
    # remove the food if the hero grabbed any
    if (grabbed_food_idx != -1):    
        foood_x_list.pop(grabbed_food_idx)
        food_y_list.pop(grabbed_food_idx)
        
    # add new food if some time has passed
    if (frameCount % (frames_per_sec*create_food_every) == 0):
        food_x_list.append(random(400));
        food_y_list.append(random(400));
        
def keyPressed():
    global hero_x, hero_y
    if (keyCode == LEFT):
        hero_x = hero_x - 3;
    if (keyCode == RIGHT):
        hero_x = hero_x + 3;
    if (keyCode == UP):
        hero_y = hero_y - 3;
    if (keyCode == DOWN):
        hero_y = hero_y + 3;
        
