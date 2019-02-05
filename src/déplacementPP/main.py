import pygame
import math

pygame.init()
window = pygame.display.set_mode((750,750))
pygame.display.set_caption('Le Prince Des Fleurs')
clock = pygame.time.Clock()
imgVolcan=pygame.image.load("../perso.png")
imgVolcan=pygame.transform.rotate(imgVolcan,-85)
imgPlanete=pygame.image.load("../../images/planèteTest.jpg")

#change la taille de l'image
imgVolcan=pygame.transform.scale(imgVolcan,(66,66))
imgPlanete=pygame.transform.scale(imgPlanete,(320,320))

imgPlaneteCopie=imgPlanete.copy()
imgVolcanCopie=imgVolcan.copy()
rectplanet = imgPlanete.get_rect(center=(375,375))
pos = 0
angle = 0
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done=True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pos += 6
        elif event.key == pygame.K_RIGHT:
            pos -= 6
    angle += 1
    imgPlanete=pygame.transform.rotozoom(imgPlaneteCopie,angle,1)
    imgVolcan=pygame.transform.rotozoom(imgVolcanCopie,angle+pos,1)
    planetCenter = imgPlanete.get_rect(center=rectplanet.center)
    rectVolcano = imgVolcan.get_rect(center=(375+math.cos(math.radians(-angle-pos))*200,375+math.sin(math.radians(-angle-pos))*200))
    volcanoCenter = imgVolcan.get_rect(center=rectVolcano.center)
    window.fill((255,255,255))
    window.blit(imgVolcan,(volcanoCenter))
    window.blit(imgPlanete,(planetCenter))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
