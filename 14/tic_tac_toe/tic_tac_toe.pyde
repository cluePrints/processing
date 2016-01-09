field_size = 3
cell_size = 70
field_map = [ 
             [' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']
            ]
current_turn_symbol = 'x'
mode = "in_progress"

def setup():
    size(cell_size*field_size, cell_size*field_size);
    
def draw():
    draw_field_and_checks()
    if (mode == "game_over"):
        draw_game_over()
        
def draw_field_and_checks():
    for row in range(0, field_size):
        for col in range(0, field_size):
            fill(255, 255, 255)
            rect(col*cell_size, row*cell_size, cell_size, cell_size)
            
            color(0, 0, 0) 
            if (field_map[row][col] == 'x'):
                line(col*cell_size, row*cell_size, col*cell_size+cell_size, row*cell_size+cell_size)
                line(col*cell_size+cell_size, row*cell_size, col*cell_size, row*cell_size+cell_size)
            elif (field_map[row][col] == 'o'):
                ellipse(col*cell_size+cell_size/2, row*cell_size+cell_size/2, cell_size, cell_size)

def draw_game_over():
    fill(0, 0, 0);
    text("Game over. '" + str(current_turn_symbol) + "' won", 20, 20)

def mousePressed():
    global current_turn_symbol
    global mode
    if (mode == "in_progress"):
        row = mouseY / cell_size
        col = mouseX / cell_size
        
        # exit the function early so we do nothing if the cell is already occupied
        if (field_map[row][col] != ' '):
            return;
        
        field_map[row][col] = current_turn_symbol
        
        if is_game_over():
            mode = "game_over"
        else:
            next_turn()
            
def next_turn():
    global current_turn_symbol
    if (current_turn_symbol == 'o'):
        current_turn_symbol = 'x'
    elif (current_turn_symbol == 'x'):
        current_turn_symbol = 'o'

def is_game_over():
    if (check_is_winner('x')):
        return True
    if (check_is_winner('o')):
        return True
    return False

def check_is_winner(elem0):
    for i in range(0, field_size):
        if has_horizontal_row(elem0, i):
            print 'has row ' + str(i)
            return True;
        if has_vertical_row(elem0, i):
            print 'has col ' + str(i)
            return True;
        
    if has_diagonal(elem0):
        print 'has diag'
        return True
    
    if has_antidiagonal(elem0):
        print 'has_anti'
        return True
    
    return False

def has_horizontal_row(elem0, column_idx):
    return has_consequent_elements(elem0, 0, column_idx, 1, 0)

def has_vertical_row(elem0, row_idx):
    return has_consequent_elements(elem0, row_idx, 0, 0, 1)

def has_diagonal(elem0):
    return has_consequent_elements(elem0, 0, 0, 1, 1)

def has_antidiagonal(elem0):
    return has_consequent_elements(elem0, field_size-1, 0, -1, 1)

def has_consequent_elements(elem0, row_start, col_start, row_increment, col_increment):
    row = row_start
    col = col_start

    for i in range(0, field_size):
        current_elem = field_map[row][col]
        if (elem0 != current_elem):
            return False
        else:
            print "current_elem " + str(row) + ", " + str(col) + ":" + current_elem
        
        row = row + row_increment
        col = col + col_increment
            
    return True
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
