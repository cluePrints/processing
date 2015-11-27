def setup():
    global state
    state = "game_over"
    size(500, 500);
    background(0)
    
def draw():
    global state
    if (state == "game_in_progress"):
        draw_game_in_progress()
    if (state == "game_over"):
        draw_game_over_screen()
    
def draw_game_over_screen():
    fill(204, 204, 204)
    rect(100, 100, 250, 50)
    fill(255, 0,0)
    text("Game over\nPress ENTER key to start again...", 115, 120)
    
def keyPressed():
    global state
    if (state == "game_over"):
        process_game_over_keys()
        
    if (state == "game_in_progress"):
        process_game_in_progress_keys()
        
def draw_game_in_progress():
    background(0)
    fill(0)
    rect(0,0,width, height)
        
def process_game_over_keys():
    key_enter = 10
    global state
    if (keyCode == key_enter):
        print(keyCode)
        restart_game()
        state = "game_in_progress"
        
def restart_game():
    background(0)
    
def process_game_in_progress_keys():
    pass
        
        
