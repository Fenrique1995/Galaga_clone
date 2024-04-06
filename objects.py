import pygame
##########################class ship player####################################
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
    def movement(self, keys):
        keys = pygame.key.get_pressed()
        if self.position_x > 0:
            if keys[pygame.K_a]:#Movimientos rectos
                self.position_x -= 3
        if self.position_x < 750:
            if  keys[pygame.K_d]:
                self.position_x += 3
        if self.position_y > 50:
            if  keys[pygame.K_w]:
                self.position_y -= 3
        if self.position_y < 550:
            if  keys[pygame.K_s]:
                self.position_y += 3

        if self.position_x < 750 and self.position_y < 550:
            if  keys[pygame.K_s] and keys[pygame.K_d]:#Movimientos diagonales
                self.position_y += 3
                self.position_x += 3
        if self.position_x > 0 and self.position_y < 550:
            if  keys[pygame.K_s] and keys[pygame.K_a]:
                self.position_y += 3
                self.position_x -= 3
        if self.position_x > 0 and self.position_y > 50:
            if  keys[pygame.K_w] and keys[pygame.K_a]:
                self.position_y -= 3
                self.position_x -= 3
        if self.position_x < 750 and self.position_y > 50:
            if  keys[pygame.K_w] and keys[pygame.K_d]:
                self.position_y -= 3
                self.position_x += 3
        pygame.display.flip()

    def attack(self, screen, bullets):#Ataque de la nave
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_bullet = Bullets(self.position_x + 35, self.position_y)  # Ajusta según el punto de origen deseado
            bullets.append(new_bullet)
#####################################################################################


#################################Bullets#############################################
class Bullets:#clase de la bala
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.sprite_01 = pygame.transform.scale(pygame.image.load('sprites/bullet_blackwing/M484BulletCollection1.png'), (5, 5))
        self.sprite_02 = pygame.transform.scale(pygame.image.load('sprites/enemy_bullet/M484BulletCollection1.png'), (5, 5))

    def draw_bullet(self, screen):#dibuja la bala 
        screen.blit(self.sprite_01, (self.position_x, self.position_y))
        self.hitbox = (self.position_x, self.position_y, 5, 5)
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 2)

    def shoot_up(self):
        self.position_y -= 1

    def shoot_down(self):
        self.position_y += 1
######################################################################################

##########################class ship enemy####################################
class Enemy:
    def __init__(self, position_x, position_y, health, direction):
        self.position_x = position_x
        self.position_y = position_y
        self.sprite = pygame.transform.scale(pygame.image.load('sprites/enemy_ship.png'), (70, 70))
        self.health = health
        self.direction = direction
    def draw(self, screen):
        screen.blit(self.sprite, (self.position_x, self.position_y))
        self.hitbox = (self.position_x, self.position_y, 70, 70)
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 2)

    def movement(self):
        self.position_x += 0.2 * self.direction
        if self.position_x > 730:  # Ajuste considerando el tamaño del sprite para que no salga de la pantalla
            self.direction = -1
        elif self.position_x < 0:
            self.direction = 1