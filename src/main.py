<<<<<<< HEAD
=======
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

x =  (display_width / 2)
y = (display_height / 2)
x_change = 0
y_change = 0
car_speed = 0
pygame.mixer.Sound.play(logo_MenuControllersound)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_change = pygame.MOUSEBUTTONDOWN.real
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

        ######################
    ##
    x += x_change
    y += y_change
   ##
    gameDisplay.fill(white)
    car(x,y)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
>>>>>>> 283e7507f71dcaac4ff01e0c925c3493d76140b4
