#it is solution for maze from https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

is_facing_north()

while True:

    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
       
    if front_is_clear():
        move()
   
    elif wall_on_right():
        turn_left()
   
    else: 
        turn_left()
        turn_left()
       
    if at_goal():
        done()