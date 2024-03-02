import pygame
#import time

WIDTH = 800
HEIGHT = 600
'''
stars = pygame.image.load('sprites/background/stars_1.png')
star_background = pygame.transform.scale(stars, (800, 600))
'''
def window():
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    return screen
'''
def background(screen):
    screen.blit(star_background, (0, 0))
    pygame.time.delay(30)
    pygame.display.flip()
'''