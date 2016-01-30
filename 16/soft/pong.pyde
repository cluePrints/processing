field_width = 400
field_height = 200
player_1_y = 100
player_width = 50

# kody klavish dlya upravlinnya
player_1_up_keycode = 87
player_1_down_keycode = 83

# zminni dlya kylky
ball_x = 1
ball_y = player_1_y
ball_speed_x = 2
ball_speed_y = 2

def setup():
    size(field_width, field_height);
    strokeWeight(5);
    
def draw():
    global ball_x, ball_y
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y
    background(255, 255, 255);
    line(0, player_1_y, 0, player_1_y + player_width)
    ellipse(ball_x, ball_y, 5, 5)
    
def keyPressed():
    print(keyCode)
    global player_1_y
    if (keyCode == player_1_up_keycode):
        player_1_y = player_1_y - 5;
    if (keyCode == player_1_down_keycode):
        player_1_y = player_1_y + 5;
        
        
        
        
        
        
        
        
        
        
