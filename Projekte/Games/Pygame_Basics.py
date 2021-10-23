import pygame, sys
from pygame.constants import QUIT

screen_width = 600
screen_height = 600

''' 1 -  pygame Initialisieren '''
pygame.init()
pygame.display.set_caption("Pygame") # Titel setzen
screen = pygame.display.set_mode((screen_width, screen_height))

''' 2 - fps einstellen
Je höher die fps umso "schneller" bewegt sich ein OBjekt im Screen
  '''
clock = pygame.time.Clock()
fps = 120

''' 3 - Surface erstellen (s. unten Beschreibung) '''
bg_surface = pygame.image.load('assets/background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface) # multipliziert das Bild um den Faktor 2
bg_surface = pygame.transform.scale(bg_surface, (screen_width, screen_height)) # skaliert auf screen Groesse

def game_loop():
  ''' 4 -  gameloop erstellen
  Hier wird das Canvas repainted und die Logik des Spiels ist dort enthalten '''
  while True:
      ''' 4a: Event-Loop, d.h. Events abfragen z.B. Key Klicks'''
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.KEYDOWN: # alle Tastendrücke abfangen
              if event.key == pygame.K_SPACE:
                print("Space gedrückt")

      ''' 3 - Surface auf das Display Surface packen '''
      screen.blit(bg_surface,(0,0)) # (0,0) Koordinatenursprung

      ''' 4b: Canvas updaten '''
      pygame.display.update()

      clock.tick(fps)

if __name__ == "__main__":
    game_loop()

''''
Surfaces:
In pygame gibt es ein "Display Surface (DS)" und "(regular) Surface (rS)"
Das DS gibt es nur einmal und wird immer angezeigt. Eine Art Hauptframe.

rS kann man so viele wie gewünscht erstellen.
Ein rS wird nur angezeigt, wenn es dem DS zugeorndet wird.
Will man z.B. ein Bild einfügen. Nimmt man für das Bild ein neues rS.

Rectangles:
Quadrate werden bevorzugt benutzt, um Objekte im Spiel zu simulieren,
wie z.B. den Hauptcharakter.
Vorteil: Kollisionen lassen sich einfacher berechnen und die Position
eines Objekts lässt sich besser ansetzen. Auch z.B. Rotation.
Bsp: 
pygame.Rect(width, height,x,y)
oder besser surface.get_rect(rect_position) # hier wird ein Rect um das
Objekt gelegt.

Text in pygame: (Achtung: fonts immer nach pygame.init angeben!)
1. create a font (style,size) z.B. game_font = pygame.font.Font('048_19.ttf',40) oder game_font = pygame.font.SysFont('Arial',40) # (style,size)
2. render the font (text,colour) to a surface z.B. surface = game_font.render('Score',True,(255,255,255))
3. use the resulting text surface

Sound:
flap_sound = pygame.mixer.Sound('assets/audio/wing.wav')
flap_sound.play()
# Um delay vom Sound zu verhindern, muss vor:
pygame.init()
pygame.mixer.pre_init(...Parameter) hin
'''