import pygame, sys
from pygame.constants import QUIT
from enum import Enum
import time
import random

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

screen_width = 1080
screen_height = 720

''' pygame Initialisieren '''
pygame.init()
pygame.display.set_caption("Snake") # Titel setzen
screen = pygame.display.set_mode((screen_width, screen_height))

''' fps einstellen '''
clock = pygame.time.Clock()
global fps
fps = 10

''' Snake '''
snake_position = [250,250]
snake_body = [[250,250], [240,250], [230,250]]

''' Food '''
food_position = [0,0]
food_position[0] = round(random.randint(5, screen_width - 5), -1)
food_position[1] = round(random.randint(5, screen_height - 5), -1)

global score, dec_count
score = 0 # Punktestand
dec_count = 0 # Hilfsvariable um das Spiel schneller zu machen

def handle_keys(direction):
    new_direction = direction
    for event in [e for e in pygame.event.get() if e.type == pygame.KEYDOWN or e.type == pygame.QUIT]: # nur Tasten-Events abfragen
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_UP and direction != Direction.DOWN: # man darf nur nach oben, wenn man zuvor nicht nach unten laeuft
            new_direction = Direction.UP
        if event.key == pygame.K_DOWN and direction != Direction.UP:
            new_direction = Direction.DOWN
        if event.key == pygame.K_RIGHT and direction != Direction.LEFT:
            new_direction = Direction.RIGHT
        if event.key == pygame.K_LEFT and direction != Direction.RIGHT:
            new_direction = Direction.LEFT
        if event.key == pygame.K_q:
            pygame.quit()
            exit(0)

    return new_direction

def move_snake(direction):
    """ hier werden nur die Koordiaten gesetzt, repaint kuemmert sich um die Anzeige"""
    if direction == Direction.UP:
        snake_position[1] -= 10
    if direction == Direction.DOWN:
        snake_position[1] += 10
    if direction == Direction.LEFT:
        snake_position[0] -= 10
    if direction == Direction.RIGHT:
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

def get_food():
    print("food " + str(food_position))
    print("snake " + str(snake_position))
    print("\n")
    global score, dec_count
    # pruefe ob der Kopf der Snake mit der food position uebereinstimmt
    #if abs(snake_position[0] - food_position[0]) < 20 and abs(snake_position[1] - food_position[1]) < 20:
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        dec_count += 10
        generate_new_food()
    else:
        snake_body.pop() # letzte Element der Snake abnehmen

def generate_new_food():
    food_position[0] = round(random.randint(5, ((screen_width))), -1)
    food_position[1] = round(random.randint(5, ((screen_height))), -1)

def repaint():
    screen.fill(pygame.Color(0,0,0)) # Hintergrundfarbe
    for body in snake_body:
        pygame.draw.circle(screen, pygame.Color(0, 255, 0), (body[0], body[1]), 5)
        # (surface, color, center, radius)
        
    pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(food_position[0]-5, food_position[1]-5, 10, 10))
    # (surface, color, Rect(left, top, width, height))

def game_over():
    """ check if game over"""
    if snake_position[0] < 0 or snake_position[0] > screen_width - 10:
        game_over_message()
    if snake_position[1] < 0 or snake_position[1] > screen_height - 10:
        game_over_message()
    for blob in snake_body[1:]:
        if snake_position[0] == blob[0] and snake_position[1] == blob[1]:
            game_over_message()

def game_over_message():
    font = pygame.font.SysFont('Arial', 30)
    render = font.render(f"Score: {score}", True, pygame.Color(255,255,255))
    rect = render.get_rect()
    rect.midtop = (screen_width / 2, screen_height / 2)
    screen.blit(render, rect)
    pygame.display.flip() # aktualisiert die Anzeige
    time.sleep(2)
    pygame.quit()
    exit(0)

def paint_hud():
    font = pygame.font.SysFont("Arial", 20)    
    render = font.render(f"Score: {score}", True, pygame.Color(255,255,255))
    rect = render.get_rect()
    screen.blit(render, rect)
    pygame.display.flip() # aktualisiert die Anzeige
    #time.sleep(10)


def game_loop():

    direction = Direction.RIGHT # Anfangsrichtung nach rechts
    ''' gameloop erstellen '''
    while True:
        direction = handle_keys(direction)
        move_snake(direction)
        get_food()
        repaint()
        game_over()
        paint_hud()
        global fps, dec_count
        if dec_count == 100:
            fps += 5
            dec_count = 0

        ''' Canvas updaten '''
        pygame.display.update()
        clock.tick(fps)


if __name__ == "__main__":
    game_loop()