import pygame

class GameController:


    def __init__(self,vueScreen):
        self.vueScreen=vueScreen()


    def createAndRotatePlanet(imgPath,size,centerPositionx,centerPositiony,rotationAngle):

        planet = Planet(imgPath,size,centerPosition,rotationAngle)
        vueScreen.fill((255,255,255))
        vueScreen.blit(planet.imgPlanet,(planet.planetCenter))
        vueScreen.blit(planet.imgVolcan,(planet.volcanoCenter))
        pygame.display.update()
        clock.tick(30)

    def addVolcanoOnPlanet(imgPath,planet):
        planet.addVolcano(imgPath,planet.imgPlanet)

    
