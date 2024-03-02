import pygame
import time
from dependencies import *
from objects import *
from pygame.locals import K_a, K_s, K_d, K_w, K_SPACE

intial_screen = window()

my_ship = Ship(400, 450, 'burnwing', 3)

bullets = []#aca se alamacenan las balas

pygame.init() #Se inicializa pygame

pressed_keys = pygame.key.get_pressed()

def controls(pressed_keys):
        my_ship.movement(pressed_keys)
        my_ship.attack(intial_screen, bullets)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(event.pos)
        elif event.type == pygame.QUIT:
            running = False
    
    
    pressed_keys = pygame.key.get_pressed()
    intial_screen.fill((0, 0, 0)) 
    my_ship.draw(intial_screen)
    controls(pressed_keys)
    
    for bullet in bullets[:]:  # Hacer una copia para poder modificar la lista
        bullet.shoot()
        if bullet.position_y < 0:  # Remueve la bala si sale de la pantalla
            bullets.remove(bullet)
        else:
            bullet.draw_bullet(intial_screen)

    pygame.display.flip()

pygame.quit() 