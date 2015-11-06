tail_y_min = 50
tail_x_min = 100
max_saturation = 255
max_brightness = 255
tail_segments_count = 9

def setup():
    size(500, 500);
    frameRate(3)
    
def draw():
    colorMode(RGB)
    background(0, 0, 0);
    x = tail_x_min;
    y = tail_y_min;
    if (frameCount % 2 == 0):
        y = y + 2;
        
    segment_w = 20
    segment_h = 20
    for segment_number in range(tail_segments_count):
        vertical_tail_segment(x, y, segment_w, segment_h)
        x = x + segment_w;
        if (segment_number % 2 == 0):
            y = y + 4;
        else:
            y = y - 4;
            
def vertical_tail_segment(x_left, y_left, segment_width, segment_height):
    colorMode(HSB)
    y = y_left;
    for color_number in [0, 42, 85, 171, 213]:
        noStroke()
        fill(color_number, max_saturation, max_brightness)
        rect(x_left, y, segment_width, segment_height)
        y = y + segment_height
