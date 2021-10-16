import pygame, sys, time, random
from pygame.constants import QUIT

screen_width = 600
screen_height = 600
block_size = 10 #Set the size of the grid block
grid_line_size = 1
random_blocks = 2000

GREY = (50,50,50)
ORANGE = (200,200,0)
BLACK = (0,0,0)

''' pygame Initialisieren '''
pygame.init()
pygame.display.set_caption("Game of Life") # Titel setzen
screen = pygame.display.set_mode((screen_width, screen_height))

''' fps einstellen '''
clock = pygame.time.Clock()
fps = 15

def draw_grid():
    for x in range(0, screen_width, block_size):
        for y in range(0, screen_height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, GREY, rect, grid_line_size)

def set_block(coordinates,clicked_block_color):
    x = int(coordinates[0] / block_size)
    y = int(coordinates[1] / block_size)
    #print("x=" + str(x) + " y=" +str(y))
    #print("  x="+str(int(x*block_size)) + " y="+str(int(y*block_size)))
    rect = pygame.Rect(int(x*block_size)+grid_line_size, int(y*block_size)+grid_line_size, block_size-grid_line_size, block_size-grid_line_size)
    #rect = pygame.Rect(x*block_size+grid_line_size, y*block_size+grid_line_size, block_size-(grid_line_size*2), block_size-(grid_line_size*2))
    color = change_color(clicked_block_color)
    pygame.draw.rect(screen, color, rect)
    #print("x=" + str(x) + " y=" +str(y))

def change_color(color):
    #print(str(color))
    new_color = color
    if color[0] == BLACK[0] and color[1] == BLACK[1] and color[2] == BLACK[2]:
        new_color = ORANGE
    elif color[0] == ORANGE[0] and color[1] == ORANGE[1] and color[2] == ORANGE[2]:
        new_color = BLACK
    return new_color

def is_alive(block_coord_x, block_coord_y):
    ''' prüft ob eine Zelle lebt oder nicht '''
    x = block_coord_x
    y = block_coord_y
    if (x + grid_line_size) > screen_width:
        return False
    else:
        x = block_coord_x + grid_line_size

    if (y + grid_line_size) > screen_height:
        return False
    else:
        y = block_coord_y + grid_line_size

    color = pygame.Surface.get_at(screen,(x,y))
    #print(f"x={x}, y={y}, color={color}")

    if color[0] == BLACK[0] and color[1] == BLACK[1] and color[2] == BLACK[2]:
        return False
    else:
        #print(f"Alive - x:{x}, y={y}")
        return True


def check_live(block_coord_x, block_coord_y,status):
    ''' prüfe die Nachbarn ob Zelle leben darf '''
    count_of_living_neighbors = 0

    for i in range(8):
        if i == 0:
            x = block_coord_x - block_size
            y = block_coord_y - block_size
        if i == 1:
            x = block_coord_x
            y = block_coord_y - block_size
        if i == 2:
            x = block_coord_x + block_size
            y = block_coord_y - block_size
        if i == 3:
            x = block_coord_x - block_size
            y = block_coord_y
        if i == 4:
            x = block_coord_x + block_size
            y = block_coord_y
        if i == 5:
            x = block_coord_x - block_size
            y = block_coord_y + block_size
        if i == 6:
            x = block_coord_x
            y = block_coord_y + block_size
        if i == 7:
            x = block_coord_x + block_size
            y = block_coord_y + block_size

        if x >= 0 and y >= 0:
            if is_alive(x,y):
                count_of_living_neighbors += 1

    if status == True:
        if count_of_living_neighbors > 2:
            return False
        elif count_of_living_neighbors == 2 or count_of_living_neighbors == 3:
            return True
        elif count_of_living_neighbors > 3:
            return False

    else:
        if count_of_living_neighbors == 3:
            return True

    return status

def create_r_pentomino():
    set_block((304,297),BLACK)
    set_block((304,287),BLACK)
    set_block((314,287),BLACK)
    set_block((294,297),BLACK)
    set_block((304,307),BLACK)

def create_random_blocks():
    amount_of_random_blocks = random.randint(1,random_blocks)
    for i in range(amount_of_random_blocks):
        x_random = random.randint(0+grid_line_size,screen_width-grid_line_size)
        y_random = random.randint(0+grid_line_size,screen_height-grid_line_size)
        set_block((x_random,y_random),BLACK)


''' Grid Linien zeichnen (nur einmal zeichnen) '''
draw_grid()

#create_random_blocks()
create_r_pentomino()


# for test
##set_block((21,1), BLACK)
#set_block((21,21), BLACK)
#set_block((1,21), BLACK)


#calc_block((581,1),BLACK)

''' gameloop'''
while True:
    ''' Event-Loop'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # alle Tastendrücke abfangen
            if event.key == pygame.K_SPACE:
              print("Space gedrückt")
        if event.type == pygame.MOUSEBUTTONUP:
            coordinates = pygame.mouse.get_pos()
            clicked_block_color = pygame.Surface.get_at(screen,(coordinates[0],coordinates[1]))
            # click auf Grid Linien ignorieren
            if clicked_block_color[0] != GREY[0] and clicked_block_color[0] != GREY[0] and clicked_block_color[0] != GREY[0]:
                set_block(coordinates,clicked_block_color)
            
            print("Mouse up"+str(coordinates))



    ''' Berechne Zellen '''
    # 2 Infos werden benötigt - eigene Zellen-Zustand und Anzahl an lebendigen Nachbarn
    
    for y in range(0, screen_height, block_size):
        for x in range(0, screen_width, block_size):
            status = is_alive(x,y)
            widt = block_size-(grid_line_size*2)
            #print(f"x={x}, y={y} - is_alive={status} - {widt}")
            #time.sleep(0.1)
            rect = pygame.Rect(x+grid_line_size, y+grid_line_size, block_size-grid_line_size, block_size-grid_line_size)
            if check_live(x,y,status):
                #print(f"Alive - {x}, {y}")
                pygame.draw.rect(screen, ORANGE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)
    


    ''' Canvas updaten '''
    pygame.display.update()

    clock.tick(fps)


'''
Regeln:
    Bloecke ausserhalb des Grid gelten als tot
    Eine lebendige Zelle stirbt, wenn sie weniger als zwei lebendige Nachbarzellen hat.
    Eine lebendige Zelle mit zwei oder drei lebendigen Nachbarn lebt weiter.
    Eine lebendige Zelle mit mehr als drei lebenden Nachbarzellen stirbt im nächsten Zeitschritt.
    Eine tote Zelle wird wiederbelebt, wenn sie genau drei lebende Nachbarzellen hat.


'''