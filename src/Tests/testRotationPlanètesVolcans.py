import pygame
import math

pygame.init()

window = pygame.display.set_mode((750,750))
pygame.display.set_caption('Le Prince Des Fleurs')
clock = pygame.time.Clock()
imgVolcan=pygame.image.load("../../images/volcanTest.jpg")
imgVolcan=pygame.transform.rotate(imgVolcan,-85)
imgPlanete=pygame.image.load("../../images/Planet.png")

#change la taille de l'image
imgVolcan=pygame.transform.scale(imgVolcan,(250,250))
imgPlanete=pygame.transform.scale(imgPlanete,(320,320))

imgPlaneteCopie=imgPlanete.copy()
imgVolcanCopie=imgVolcan.copy()
rectplanet = imgPlanete.get_rect(center=(375,375))

angle = 0
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done=True
    angle += 1
    imgPlanete=pygame.transform.rotozoom(imgPlaneteCopie,angle,1)
    imgVolcan=pygame.transform.rotozoom(imgVolcanCopie,angle,1)
    planetCenter = imgPlanete.get_rect(center=rectplanet.center)
    rectVolcano = imgVolcan.get_rect(center=(375+math.cos(math.radians(-angle))*175,375+math.sin(math.radians(-angle))*175))
    volcanoCenter = imgVolcan.get_rect(center=rectVolcano.center)
    window.fill((255,255,255))
    window.blit(imgVolcan,(volcanoCenter))
    window.blit(imgPlanete,(planetCenter))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
