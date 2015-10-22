points = [122, 92, 98, 135, 36, 119, 28, 111, 54, 55, 68, 91, 94]

def setup():
    size(600, 600);
    strokeWeight(5)
    frameRate(1) # draw() byde viklikatys raz na sekundu
    
def draw():
    random_number = random(200)
    points.append(random_number) # dodaemo vypadkove chislo v kinec
     
    # nahodim maximum
    max_value = points[0]
    for point_number in range(len(points)):
        point_value = points[point_number]
        if (point_value > max_value):
            max_value = point_value;
    
    # risuem vse linii        
    for point_number in range(len(points)):
        point_value = points[point_number]
        x_pos = 50 + point_number * 10;
        y_start = 200;
        y_end = y_start - point_value;
        if (point_value == max_value):
           stroke(0, 200, 0);
        else:
            stroke(0, 0, 0);
        line(x_pos, y_start, x_pos, y_end)
