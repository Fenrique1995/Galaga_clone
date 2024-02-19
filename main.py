import pygame
from dependencies import *
from objects import *
from pygame.locals import K_a, K_s, K_d, K_w, K_SPACE

intial_screen = window()

my_ship = Ship(100, 100, 'burnwing', 3)

pygame.init() #Se inicializa pygame

pressed_keys = pygame.key.get_pressed()

running = True
while running:
    controls()
    
    intial_screen.fill((0, 0, 0)) 
    my_ship.draw(intial_screen)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(event.pos)
        elif event.type == pygame.QUIT:
            running = False

pygame.quit() 