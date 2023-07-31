def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range (6):
    jump()
