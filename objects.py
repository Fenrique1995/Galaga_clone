import pygame

class Ship:
    def __init__(self, position_x, position_y, name, health):
        self.position_x = position_x
        self.position_y = position_y
        self.sprite = pygame.transform.scale(pygame.image.load('sprites/blackwing.png'), (70, 70))
        self.name = name
        self.health = health
    def draw(self, screen):
        screen.blit(self.sprite, (self.position_x, self.position_y))
        self.hitbox = (self.position_x, self.position_y, 70, 70)
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 2)