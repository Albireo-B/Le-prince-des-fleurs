import pygame

pygame.init()

class GameController:


    def __init__(self,vueScreen):
        self.vueScreen=vueScreen()
        self.planetes={}
        self.prince=Prince()

    def createAndRotatePlanet(imgPath,size,centerPositionx,centerPositiony,rotationAngle):
        planet = Planet(imgPath,size,centerPosition,rotationAngle)
        self.planetes[self.planetes.get_size()]=planet


    def addPrinceOnPlanet(planet):
        planet.addPrince(prince)

    def removePrinceFromPlanet(planet):
        planet.removePrince(prince)

#createAndRotatePlanet("../../images/planèteTest.jpg",(200,200),375,375,2)



    def init_display():
        #couleur blanche a virer
        vueScreen.fill((255,255,255))
        for key in planetes:
            vueScreen.blit(planetes[key].imgPlanet,(planetes[key].planetCenter))
            vueScreen.blit(planetes[key].imgVolcan,(planetes[key].volcanos.volcanoCenter))
        init_rotate()


    def init_rotate():
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    done=True
            for key in planetes:
                imgPlaneteCopie=planetes[key].imgPlanet.copy()
                imgVolcanCopie=planetes[key].volcano.imgVolcano.copy()
                rectplanet = planetes[key].imgPlanet.get_rect(center=(centerPositionx,centerPositiony))
                angle += planetes[key].rotationAngle
                planetes[key].imgPlanet=pygame.transform.rotozoom(imgPlaneteCopie,angle,1)
                planetCenter = planetes[key].imgPlanet.get_rect(center=rectplanet.center)
                planetes[key].volcano.imgVolcano=pygame.transform.rotozoom(imgVolcanCopie,angle,1)
            pygame.display.update()
            clock.tick(30)
