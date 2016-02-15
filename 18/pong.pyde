import random
import math

field_width = 400
field_height = 200

player_1_y = 50
player_2_y = 50
player_width = 50

player_1_keycode_up = 87
player_1_keycode_down = 83

player_2_keycode_up = 38
player_2_keycode_down = 40

score_1 = 0
score_2 = 0

def setup():
    size(field_width, field_height + 50)
    next_round(0)
    
def draw():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y
    
    if (ball_y < 0):
        bounce_y()
    if (ball_y > field_height):
        bounce_y()
    if (ball_x >= field_width):
        if (ball_y > player_2_y + player_width):
            next_round(2)
        elif (ball_y < player_2_y):
            next_round(2)
        else:
            bounce_x()
    if (ball_x < 0):
        if (ball_y > player_1_y + player_width):
            next_round(1)
        elif (ball_y < player_1_y):
            next_round(1)
        else:
            bounce_x()

    # R G B
    background(255, 255, 255)
    strokeWeight(1)
    fill(255, 255, 255)
    rect(0,0,field_width, field_height);
    strokeWeight(5)
    line(0, player_1_y, 0, player_1_y + player_width)
    line(field_width, player_2_y, field_width, player_2_y + player_width)
    ellipse(ball_x, ball_y, 5, 5)
    fill(0,0,0);
    text(str(score_1) + ":" + str(score_2), 50, field_height + 20);
    
def next_round(looser):
    global score_1, score_2
    if (looser == 1):
        score_2 = score_2 + 1;
    if (looser == 2):
        score_1 = score_1 + 1;
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    if (looser == 2):
        ball_x = field_width
        ball_y = player_2_y
        ball_speed_x = -2
        ball_speed_y = 2
    else:
        ball_x = 1
        ball_y = player_1_y
        ball_speed_x = 2
        ball_speed_y = -2

def keyPressed():
    global player_1_y, player_2_y, ball_speed_y
    if (keyCode == player_1_keycode_up):
        player_1_y = player_1_y - 10
    if (keyCode == player_1_keycode_down):
        player_1_y = player_1_y + 10
    if (player_1_y < 0):
        player_1_y = 0
    if (player_1_y > field_height - player_width):
        player_1_y = field_height - player_width
        
    if (keyCode == player_2_keycode_up):
        player_2_y = player_2_y - 10
    if (keyCode == player_2_keycode_down):
        player_2_y = player_2_y + 10
    if (player_2_y < 0):
        player_2_y = 0
    if (player_2_y > field_height - player_width):
        player_2_y = field_height - player_width
        
def bounce_x():
    global ball_speed_x
    ball_speed_x = - ball_speed_x
    ball_speed_x = ball_speed_x + math.copysign(random.randint(0, 2), ball_speed_x)
    
def bounce_y():
    global ball_speed_y
    ball_speed_y = - ball_speed_y