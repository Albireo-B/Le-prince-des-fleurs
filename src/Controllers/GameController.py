import sys
sys.path.insert(0, "../Objects")
try:
    import Planet
    from  Object import *
    from Volcano import *
    from  VueScreen import *
except ImportError:
    print('No Import')

import pygame
pygame.init()

class GameController:



    def __init__(self):
        self.vueScreen=VueScreen((1500,750))
        self.planetes={}
        #self.prince=Prince()
        self.createPlanet("../../images/Planet.png",200,200,375,375,2)
        self.init_display()
        self.init_rotate()




    def createPlanet(self,imgPath,width,height,centerPositionx,centerPositiony,rotationAngle):
        planet = Planet.Planet(imgPath,width,height,centerPositionx,centerPositiony,rotationAngle)
        self.planetes[len(self.planetes)]=planet

    def addPrinceOnPlanet(self,planet):
        planet.addPrince(prince)

    def removePrinceFromPlanet(self,planet):
        planet.removePrince(prince)





    def init_display(self):
        #couleur blanche a virer
        self.vueScreen.window.fill((255,255,255))
        for key in self.planetes:
            self.vueScreen.window.blit(self.planetes[key].volcano.imgVolcano,self.planetes[key].volcano.volcanoCenter)
            self.vueScreen.window.blit(self.planetes[key].imgPlanet,self.planetes[key].planetCenter)


    def init_rotate(self):
        done=False
        angle=0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    done=True
            for key in self.planetes:
                imgPlaneteCopie=self.planetes[key].imgPlanet.copy()
                imgVolcanCopie=self.planetes[key].volcano.imgVolcano.copy()
                angle += self.planetes[key].rotationAngle
                self.planetes[key].imgPlanet=pygame.transform.rotozoom(imgPlaneteCopie,angle,1)
                self.planetes[key].planetCenter = self.planetes[key].imgPlanet.get_rect(center=self.planetes[key].rectplanet.center)
                self.planetes[key].volcano.imgVolcano=pygame.transform.rotozoom(imgVolcanCopie,angle,1)
                self.planetes[key].volcano.volcanoCenter = self.planetes[key].volcano.imgVolcano.get_rect(center=self.planetes[key].volcano.rectVolcano.center)
            pygame.display.update()
            self.vueScreen.clock.tick(30)

controleur=GameController()
