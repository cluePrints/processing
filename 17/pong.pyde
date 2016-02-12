import random

field_width = 400
field_height = 200
player_1_y = 100
player_width = 50
player_2_y = 100
player_1_up_keycode = 87
player_1_down_keycode = 83
player_2_up_keycode = 38
player_2_down_keycode = 40

ball_x = 1
ball_y = player_1_y

# TODO: uncomment this to get random speeds
#ball_total_speed = 5
ball_speed_x = 2#random.randint(1, ball_total_speed - 1)
ball_speed_y = 2#ball_total_speed - ball_speed_x

def setup():
    size(field_width + 1, field_height + 1);
    strokeWeight(5);
    
def draw():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y
        
    # ball bouncing
    if (ball_x <= 0) or (ball_x >= field_width):
        ball_speed_x = - ball_speed_x
    if (ball_y <= 0) or (ball_y >= field_height):
        ball_speed_y = - ball_speed_y
        
    # TODO: check if somebody won here and change the score
    
    background(255, 255, 255);
    line(0, player_1_y, 0, player_1_y + player_width)
    line(field_width, player_2_y, field_width, player_2_y + player_width)
    ellipse(ball_x, ball_y, 5, 5)
    
def keyPressed():
    print(keyCode)
    global player_1_y, player_2_y
    # player movements
    if (keyCode == player_1_up_keycode):
        player_1_y = player_1_y - 5;
    if (keyCode == player_1_down_keycode):
        player_1_y = player_1_y + 5;
    if (keyCode == player_2_up_keycode):
        player_2_y = player_2_y - 5;
    if (keyCode == player_2_down_keycode):
        player_2_y = player_2_y + 5;
    
    # restrict player movements
    if (player_1_y < 0):
        player_1_y = 0
    if (player_2_y < 0):
        player_2_y = 0
    if (player_1_y > field_height - player_width):
        player_1_y = field_height - player_width
    if (player_2_y > field_height - player_width):
        player_2_y = field_height - player_width
        
        
        
        
        
        
        
        
        
