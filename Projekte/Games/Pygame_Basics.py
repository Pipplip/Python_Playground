''' https://www.youtube.com/watch?v=UZg49z76cLw 
22 min
'''

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

''' 4 -  gameloop erstellen
Hier wird das Canvas repainted und die Logik des Spiels ist dort enthalten '''
while True:
    ''' 4a: Event-Loop, d.h. Events abfragen z.B. Key Klicks'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ''' 3 - Surface auf das Display Surface packen '''
    screen.blit(bg_surface,(0,0)) # (0,0) Koordinatenursprung

    ''' 4b: Canvas updaten '''
    pygame.display.update()

    clock.tick(fps)

''''
Surfaces:
In pygame gibt es ein "Display Surface (DS)" und "(regular) Surface (rS)"
Das DS gibt es nur einmal und wird immer angezeigt. Eine Art Hauptframe.

rS kann man so viele wie gewünscht erstellen.
Ein rS wird nur angezeigt, wenn es dem DS zugeorndet wird.
Will man z.B. ein Bild einfügen. Nimmt man für das Bild ein neues rS.


'''