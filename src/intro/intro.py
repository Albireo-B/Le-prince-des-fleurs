import pygame
import time

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

animation = {1:1,2:4,3:2,4:1,3:3,4:1,3:1,4:2,1:8,5:1,6:2,7:1,8:1,9:1,10:2,11:1,12:1,13:1,14:2,15:1,16:1,17:1,18:1,19:2,20:1,21:2,19:2,22:1,21:11}

def readIntro(fenetre):
    width, heigh = pygame.display.get_surface().get_size()
    tabFrame = {1:1,2:4,3:2,4:1,3:3,4:1,3:1,4:2,1:8,5:1,6:2,7:1,8:1,9:1,10:2,11:1,12:1,13:1,14:2,15:1,16:1,17:1,18:1,19:2,20:1,21:2,19:2,22:1,21:11}
    imgList = {}
    for i in range(1,24):
        img = pygame.image.load("img/"+str(i)+".png").convert()
        formattedImg = pygame.transform.scale(img.subsurface((150, 30, 900, 650)), (100, 100))
        imgList[i] = formattedImg

    for key in tabFrame:
        fenetre.blit(imgList[key], (width/2,heigh/2))
        pygame.display.flip()
        time.sleep(tabFrame[key]/24)

pygame.mixer.Sound.play(logo_sound)
readIntro(gameDisplay)
pygame.quit()
quit()
