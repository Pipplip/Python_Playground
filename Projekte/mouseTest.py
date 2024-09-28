import mouse
import time
import sys

current_pos = mouse.get_position()
print(current_pos)


count = 10

while True:
    #print(mouse.get_position())
    
    posX = 500 + count
    mouse.move(str(posX), "500")
    count = count + 10
    
    if count == 100:
        count = 10

    time.sleep(0.5)

    if mouse.is_pressed(button='left'):
        print('exit')
        sys.exit()