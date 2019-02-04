import pygame

pygame.init()
display_width=800
display_height=600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Le Prince Des Fleurs')
logo_sound = pygame.mixer.Sound('SCREW_GRAVITY.wav')
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()

crashed = False

carImg = pygame.image.load('/users/info/etu-s3/deniaul/Morpion/Jeu_morpion/Morpion/src/morpion/images/jouer.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width / 3)
y = (display_height / 2)

y_change = 0
pygame.mixer.Sound.play(logo_sound)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            ############################
    if pygame.time.get_ticks()>2500:
        y_change = -5
        print('bob')
        ########################
    y += y_change
    ##
    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
