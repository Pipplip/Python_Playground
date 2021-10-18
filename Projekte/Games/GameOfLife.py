import pygame, sys, time, random
from pygame.constants import QUIT
from copy import deepcopy

screen_width = 600
screen_height = 600
block_size = 10 #Set the size of the grid block
grid_line_size = 1
random_blocks = 1700

count_generation = 0
show_hud = True

dict_cubes = {} # { (0,0) : BLACK, (1,1) : ORANGE}

GREY = (50,50,50)
ORANGE = (200,200,0)
BLACK = (0,0,0)

''' pygame Initialisieren '''
pygame.init()
pygame.display.set_caption("Game of Life") # Titel setzen
screen = pygame.display.set_mode((screen_width, screen_height))

''' fps einstellen '''
clock = pygame.time.Clock()
fps = 10

def draw_grid():
    for x in range(0, screen_width, block_size):
        for y in range(0, screen_height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, GREY, rect, grid_line_size)

def is_alive(block_coord_x, block_coord_y):
    ''' prüft ob eine Zelle lebt oder nicht '''
    color = dict_cubes.get((block_coord_x,block_coord_y))
    if color == BLACK:
        return False
    elif color == ORANGE:
        return True
    else:
        return False


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
        if count_of_living_neighbors == 2 or count_of_living_neighbors == 3:
            return True
        elif count_of_living_neighbors > 2:
            return False
        else:
            return False

    else:
        if count_of_living_neighbors == 3:
            return True

    return status

def create_r_pentomino():
    dict_cubes[(300,300)] = ORANGE
    dict_cubes[(300,290)] = ORANGE
    dict_cubes[(310,290)] = ORANGE
    dict_cubes[(290,300)] = ORANGE
    dict_cubes[(300,310)] = ORANGE

def create_queen_bee():
    dict_cubes[(280,270)] = ORANGE

    dict_cubes[(280,280)] = ORANGE
    dict_cubes[(300,280)] = ORANGE

    dict_cubes[(290,290)] = ORANGE
    dict_cubes[(310,290)] = ORANGE

    dict_cubes[(290,300)] = ORANGE
    dict_cubes[(320,300)] = ORANGE

    dict_cubes[(290,310)] = ORANGE
    dict_cubes[(310,310)] = ORANGE

    dict_cubes[(280,320)] = ORANGE
    dict_cubes[(300,320)] = ORANGE

    dict_cubes[(280,330)] = ORANGE

def calc_round_to_fix_int(coord):
    return int(coord / block_size) * block_size

def create_random_blocks():
    amount_of_random_blocks = random.randint(1,random_blocks)
    list_random_coord = []
    for i in range(amount_of_random_blocks):
        x_random = random.randint(0+grid_line_size,screen_width-grid_line_size)
        y_random = random.randint(0+grid_line_size,screen_height-grid_line_size)
        list_random_coord.append([calc_round_to_fix_int(x_random),calc_round_to_fix_int(y_random)])
    
    for list_item in list_random_coord:
        dict_cubes[(list_item[0],list_item[1])] = ORANGE

def init_empty_dict():
    for y in range(0, screen_height, block_size):
        for x in range(0, screen_width, block_size):
            dict_cubes[(x,y)] = BLACK

def update_screen():
    # Zeichne die Liste list_cubes
    for y in range(0, screen_height, block_size):
        for x in range(0, screen_width, block_size):
            rect = pygame.Rect(x+grid_line_size, y+grid_line_size, block_size-grid_line_size, block_size-grid_line_size)
            cube_color = dict_cubes.get((x,y))
            if cube_color == None:
                print("ERROR")
            #print(f"{x}, {y} - {cube_color}")
            pygame.draw.rect(screen, cube_color, rect)

def paint_hud():
    font = pygame.font.SysFont("Arial", 28)    
    render = font.render(f"Generation: {count_generation}", True, pygame.Color(255,255,255))
    rect = render.get_rect()
    screen.blit(render, rect)
    pygame.display.flip()

''' Grid Linien zeichnen (nur einmal zeichnen) '''
draw_grid()
init_empty_dict()
create_random_blocks()
#create_r_pentomino()
#create_queen_bee()


''' gameloop'''
while True:
    count_generation += 1

    ''' Event-Loop'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # alle Tastendrücke abfangen
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
              #print("Space gedrückt")
                if show_hud == True:
                    show_hud = False
                elif show_hud == False:
                    show_hud = True

        if event.type == pygame.MOUSEBUTTONUP:
            coordinates = pygame.mouse.get_pos()
            clicked_block_color = pygame.Surface.get_at(screen,(coordinates[0],coordinates[1]))
            # click auf Grid Linien ignorieren
            if clicked_block_color[0] != GREY[0] and clicked_block_color[0] != GREY[0] and clicked_block_color[0] != GREY[0]:
                x = calc_round_to_fix_int(coordinates[0])
                y = calc_round_to_fix_int(coordinates[1])
                color = dict_cubes.get((x,y))
                if color[0] == BLACK[0] and color[1] == BLACK[1] and color[1] == BLACK[1]:
                    color = ORANGE
                else:
                    color = BLACK
                dict_cubes[(x,y)] = color
            
            print("Mouse up"+str(coordinates))


    # Zeichne die Liste list_cubes
    draw_grid()
    update_screen()

    ''' Berechne Zellen '''
    # 2 Infos werden benötigt - eigene Zellen-Zustand und Anzahl an lebendigen Nachbarn
    dict_cubes_tmp = deepcopy(dict_cubes)
    for y in range(0, screen_height, block_size):
        for x in range(0, screen_width, block_size):
            status = is_alive(x,y)
            #print(f"x={x}, y={y}, {dict_cubes_tmp.get((x,y))}")
            if check_live(x,y,status):
                #print(f"Alive - {x}, {y}")
                dict_cubes_tmp[(x,y)] = ORANGE
            else:
                dict_cubes_tmp[(x,y)] = BLACK

    dict_cubes = dict_cubes_tmp

    
    if show_hud:
        paint_hud()
    
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