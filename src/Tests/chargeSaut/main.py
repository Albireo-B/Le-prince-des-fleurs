import pygame
import math

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
     super(Player, self).__init__()
     self.image = pygame.Surface((width, height))
     self.image.fill((230, 200, 40))
     self.rect = self.image.get_rect(center=(x, y))
     self.y_change = 0


pygame.init()
GRAVITY = .9
window_height = 600
screen = pygame.display.set_mode((800, window_height))
player = Player(200, 50, 40, 30)
all_sprites_list = pygame.sprite.Group(player)
clock = pygame.time.Clock()

pui = 0
angle = 35
done=False
volcanoCenter = 100,500
move = False
while not done:
    pui -= 20
    if pui < 0:
        pui = 0
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done=True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            pui += 40
            if pui > 1000:
                pui = 1000
        elif event.key == pygame.K_SPACE:
            if player.y_change == 0:
                move = True


    print("jump : " + str(pui))

    if move: # Fly upwards.
     player.y_change = -pui/25
     move = False
    else: # Add the gravity to the y-velocity.
     player.y_change += GRAVITY
    player.rect.move_ip(0, player.y_change)
    # Clamp the rect.y value to the range 50 to 450-rect.h.
    # You could also use rect.clamp_ip((0, 50, 800, 450)).
    if player.rect.y < 50:
     player.rect.y = 50
     player.y_change = 0
    elif player.rect.bottom >= window_height-150:
     player.rect.bottom = window_height-150
     player.y_change = 0

    screen.fill((30, 100, 140))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
