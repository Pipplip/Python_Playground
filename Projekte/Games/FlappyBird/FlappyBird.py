''' https://www.youtube.com/watch?v=UZg49z76cLw 
1:06.48 min
'''

import pygame, sys, random
from pygame.constants import FINGERUP, QUIT

pygame.mixer.pre_init(frequency = 44100, size = 32, channels = 2, buffer = 512) # um Delay beim Sound zu verhindern

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
      death_sound.play()
      return False

  if bird_rect.top <= -50 or bird_rect.bottom >= 488:
    #print("Vogel zu hoch/niedgrig")
    return False

  return True

def rotate_bird(bird):
  ''' Vogel kippt nach unten bei Gravitation - Animation '''
  new_bird = pygame.transform.rotozoom(bird,-bird_movement*3,1)
  return new_bird

def bird_animation():
  new_bird = bird_frames[bird_index]
  new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
  return new_bird,new_bird_rect

def score_display(game_state):
  if game_state == 'main_game':
    score_surface = game_font.render(str(int(score)),True,(255,255,255)) # render alias True
    score_rect = score_surface.get_rect(center = (screen_width/2,100))
    screen.blit(score_surface,score_rect)
  if game_state == 'game_over':
    score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255)) # render alias True
    score_rect = score_surface.get_rect(center = (screen_width/2,100))
    screen.blit(score_surface,score_rect)

    high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255)) # render alias True
    high_score_rect = high_score_surface.get_rect(center = (screen_width/2,140))
    screen.blit(high_score_surface,high_score_rect)

''' 1 -  pygame Initialisieren '''
pygame.init()
pygame.display.set_caption("Pygame") # Titel setzen
screen = pygame.display.set_mode((screen_width, screen_height))

# Fonts immer nach dem init angeben
score = 0
high_score = 0
# Font für den score
#game_font = pygame.font.Font('048_19.ttf',40) # (style,size)
game_font = pygame.font.SysFont('Arial', 40) # (style,size)

def update_score(score, high_score):
  if score > high_score:
    high_score = score
  return high_score

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

# Bird ohne Animation
# bird_surface = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha() # Bild im Alpha Kanal
# bird_rect = bird_surface.get_rect(center = (100, screen_width/2)) # Rectangle um das Objekt 'bird_surface' legen. Parameter ist die Position des rectangles

# Bird mit Animation
bird_downflap = pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha() # Bild im Alpha Kanal
bird_midflap = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha() # Bild im Alpha Kanal
bird_upflap = pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha() # Bild im Alpha Kanal
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, screen_width/2))
BIRDFLAP = pygame.USEREVENT + 1 # weil wir schon ein USEREVENT haben (SPAWNPIPE), muss man 1 hochsetzen
pygame.time.set_timer(BIRDFLAP,200)

pipe_surface = pygame.image.load('assets/sprites/pipe-green.png').convert()
pipe_list = [] # Liste für Pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) # Event wird alle 1,2s automatisch getriggert. In der gameloop wird das Event abgefragt

pipe_height = [400,500,700] # alle möglichen Größen der Pipes

game_over_surface = pygame.image.load('assets/sprites/message.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(screen_width/2,screen_height/2))

# Sound effects
flap_sound = pygame.mixer.Sound('assets/audio/wing.wav')
death_sound = pygame.mixer.Sound('assets/audio/hit.wav')
score_sound = pygame.mixer.Sound('assets/audio/point.wav')
score_sound_count = 100

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
              flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
              # wenn game over und Space wird nochmal gedrückt, für ein reset
              game_active = True
              pipe_list.clear()
              bird_rect.center = (100, screen_width/2)
              bird_movement = 0
              score = 0
        
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            #print(pipe_list)

        if event.type == BIRDFLAP:
            # iteriere durch die Bird Liste
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            
            bird_surface,bird_rect = bird_animation()
            
            


    ''' 3 - Surface auf das Display Surface packen '''
    screen.blit(bg_surface,(0,0)) # (0,0) Koordinatenursprung
    
    if game_active:
      # Bird
      bird_movement += gravity # gravity wird in jedem Frame hinzugerechnet
      rotated_bird = rotate_bird(bird_surface)
      
      bird_rect.centery += bird_movement # und in y Richtung animiert
      screen.blit(rotated_bird, bird_rect)
      game_active = check_collision(pipe_list)

      # Pipes
      pipe_list = move_pipes(pipe_list)
      draw_pipes(pipe_list)

      # Score
      score += 0.01
      score_display('main_game')
      score_sound_count -= 1
      if score_sound_count <= 0:
        score_sound.play()
        score_sound_count = 100

    else:
      screen.blit(game_over_surface,game_over_rect)
      high_score = update_score(score,high_score)
      score_display('game_over')
    
    # Floor
    floor_x_position -= 1
    draw_floor()
    # wenn das Floor Bild ausserhalb des Bildes ist, wird es wieder zurückgesetzt
    if floor_x_position <= -screen_width:
      floor_x_position = 0
    

    pygame.display.update()

    clock.tick(fps)
