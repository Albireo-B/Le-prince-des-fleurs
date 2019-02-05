import sys
sys.path.insert(0, "../Draw")
try:
    from VolcanoEruption import *
except ImportError:
    print('No Import')

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
        self.createPlanet("../../images/Planet.png",50,50,375,100,2)
        self.createPlanet("../../images/Planet.png",500,500,750,300,4)
        self.createPlanet("../../images/Planet.png",300,300,1200,600,1)
        self.createPlanet("../../images/Planet.png",200,200,375,600,10)
        self.createPlanet("../../images/Planet.png",100,100,1350,150,7)
        self.display()
        self.init_rotate()




    def createPlanet(self,imgPath,width,height,centerPositionx,centerPositiony,rotationAngle):
        planet = Planet.Planet(imgPath,width,height,centerPositionx,centerPositiony,rotationAngle)
        self.planetes[len(self.planetes)]=planet

    def addPrinceOnPlanet(self,planet):
        planet.addPrince(prince)

    def removePrinceFromPlanet(self,planet):
        planet.removePrince(prince)





    def display(self):
        #couleur blanche a virer
        self.vueScreen.window.fill((255,255,255))
        for key in self.planetes:
            self.vueScreen.window.blit(self.planetes[key].volcano.imgVolcano,self.planetes[key].volcano.volcanoCenter)
            self.vueScreen.window.blit(self.planetes[key].imgPlanet,self.planetes[key].planetCenter)

    def init_rotate(self):
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    done=True
            self.rotate()
            self.display()
            pygame.display.update()
            self.vueScreen.clock.tick(30)

    def rotate(self):
        for key in self.planetes:
            self.planetes[key].rotationAngle += self.planetes[key].rotationSpeed
            self.planetes[key].imgPlanet=pygame.transform.rotozoom(self.planetes[key].imgPlaneteCopie,self.planetes[key].rotationAngle,1)
            self.planetes[key].volcano.imgVolcano=pygame.transform.rotozoom(self.planetes[key].volcano.imgVolcanCopie,self.planetes[key].rotationAngle,1)
            self.planetes[key].planetCenter = self.planetes[key].imgPlanet.get_rect(center=self.planetes[key].rectplanet.center)
            self.planetes[key].volcano.rectVolcano = self.planetes[key].volcano.imgVolcano.get_rect(center=(self.planetes[key].positionx+math.cos(math.radians(-self.planetes[key].rotationAngle))*self.planetes[key].width/1.8,self.planetes[key].positiony+math.sin(math.radians(-self.planetes[key].rotationAngle))*self.planetes[key].width/1.8))
            self.planetes[key].volcano.volcanoCenter = self.planetes[key].volcano.imgVolcano.get_rect(center=self.planetes[key].volcano.rectVolcano.center)


a=GameController()
