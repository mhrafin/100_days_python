# Used this code on this link
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
    
while not at_goal():
    while not wall_on_right():
        if is_facing_north() and not front_is_clear():
            turn_right()
            while front_is_clear():
                move()
        if not is_facing_north() and front_is_clear():
            turn_right()
            if front_is_clear():
                move()
        if front_is_clear():
            move()
        else:
            turn_right()
            if front_is_clear():
                move()
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
            if front_is_clear():
                move()
            
            
        
        
        
        
        
    
    
