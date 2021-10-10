''' https://www.youtube.com/watch?v=UZg49z76cLw 
1:06.48 min
'''

import pygame, sys, random
from pygame.constants import FINGERUP, QUIT

screen_width = 400
screen_height = 600

gravity = 0.25
bird_movement = 0

game_active = True # ist das Spiel aktiv oder game over

def draw_floor():
  '''Idee: Man nimmt 2 floor Bilder und lässt sie hintereinander laufen.
    Ist das eine durchgelaufen, wird es wieder ans Ende angehängt.
    So entsteht eine endlose Bewegung.
  '''
  screen.blit(floor_surface, (floor_x_position,488))
  screen.blit(floor_surface, (floor_x_position + screen_width,488))

def create_pipe():
  ''' erstelle ein Pipe im Center des Screens. Dieses rect wird in eine Liste gespeichert '''
  random_pipe_pos = random.choice(pipe_height) # suche beliebig eine Pipe-Höhe aus
  bottom_pipe = pipe_surface.get_rect(midtop = (screen_width+52, random_pipe_pos/2)) # erzeuge Rect in der Mitte vom Screen (52 Breite vom Pipe Bild)
  top_pipe = pipe_surface.get_rect(midbottom = (screen_width+52, (random_pipe_pos/2)-150)) # -150 damit das obere Pipe eine Lücke zum Unteren hat
  return bottom_pipe,top_pipe

def move_pipes(pipes):
  ''' bewege alle pipes um 5 nach links '''
  for pipe in pipes:
    pipe.centerx -= 5
  return pipes

def draw_pipes(pipes):
  ''' zeichne jedes Pipe auf dem Screen '''
  for pipe in pipes:
    if pipe.bottom >= screen_height-100:
      screen.blit(pipe_surface, pipe)
    else:
      # wenn es nicht das bottom Pipe ist, soll das Pipe Bild umgedreht werden
      flip_pipe = pygame.transform.flip(pipe_surface,False,True) # (Surface, flip x, flip y)
      screen.blit(flip_pipe, pipe)

def check_collision(pipes):
  ''' prüfe alle pipe rectangles, ob sie mit dem Bird kollidieren '''
  for pipe in pipes:
    if bird_rect.colliderect(pipe):
      #print("Collision mit Pipe")
      return False

  if bird_rect.top <= -50 or bird_rect.bottom >= 488:
    #print("Vogel zu hoch/niedgrig")
    return False

  return True

''' 1 -  pygame Initialisieren '''
pygame.init()
pygame.display.set_caption("Pygame") # Titel setzen
screen = pygame.display.set_mode((screen_width, screen_height))

''' 2 - fps einstellen
Je höher die fps umso "schneller" bewegt sich ein OBjekt im Screen
  '''
clock = pygame.time.Clock()
fps = 100

''' 3 - Surfaces erstellen '''
bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()
#bg_surface = pygame.transform.scale2x(bg_surface) # multipliziert das Bild um den Faktor 2
bg_surface = pygame.transform.scale(bg_surface, (screen_width, screen_height))

floor_surface = pygame.image.load('assets/sprites/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (screen_width, 112))
floor_x_position = 0 # Varianle um den Floor zu bewegen

bird_surface = pygame.image.load('assets/sprites/bluebird-midflap.png').convert()
#bird_surface = pygame.transform.scale
bird_rect = bird_surface.get_rect(center = (100, screen_width/2)) # Rectangle um das Objekt 'bird_surface' legen. Parameter ist die Position des rectangles

pipe_surface = pygame.image.load('assets/sprites/pipe-green.png').convert()
pipe_list = [] # Liste für Pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) # Event wird alle 1,2s automatisch getriggert. In der gameloop wird das Event abgefragt

pipe_height = [400,500,700] # alle möglichen Größen der Pipes

''' 4 -  gameloop erstellen
Hier wird das Canvas repainted und die Logik des Spiels ist dort enthalten '''
while True:
    ''' 4a: Event-Loop, d.h. Events abfragen z.B. Key Klicks'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # alle Tastendrücke abfangen
            if event.key == pygame.K_SPACE and game_active:
              bird_movement = 0
              bird_movement -= 8 # bewegt den Vogel bei jedem drücken um 8 nach oben
            if event.key == pygame.K_SPACE and game_active == False:
              # wenn game over und Space wird nochmal gedrückt, für ein reset
              game_active = True
              pipe_list.clear()
              bird_rect.center = (100, screen_width/2)
              bird_movement = 0
        
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            #print(pipe_list)


    ''' 3 - Surface auf das Display Surface packen '''
    screen.blit(bg_surface,(0,0)) # (0,0) Koordinatenursprung
    
    if game_active:
      # Bird
      bird_movement += gravity # gravity wird in jedem Frame hinzugerechnet
      bird_rect.centery += bird_movement # und in y Richtung animiert
      screen.blit(bird_surface, bird_rect)
      game_active = check_collision(pipe_list)

      # Pipes
      pipe_list = move_pipes(pipe_list)
      draw_pipes(pipe_list)
    
    # Floor
    floor_x_position -= 1
    draw_floor()
    # wenn das Floor Bild ausserhalb des Bildes ist, wird es wieder zurückgesetzt
    if floor_x_position <= -screen_width:
      floor_x_position = 0
    

    pygame.display.update()

    clock.tick(fps)
