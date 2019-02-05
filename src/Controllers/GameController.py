import sys
from pygame.math import Vector2
sys.path.insert(0, "../Objects")
try:
    import Planet
    from  Object import *
    from Volcano import *
    from  VueScreen import *
    from  Prince import *
    from  PhysicObject import *
except ImportError:
    print('No Import')

sys.path.insert(0, "../Draw")
try:
    from VolcanoEruption import *
except ImportError:
    print('No Import')

import pygame
pygame.init()

class GameController:




    def __init__(self):
        self.vueScreen=VueScreen((1500,750))
        self.planetes=[]
        self.prince=Prince("../../images/animIntro/1.png")
        #self.prince=Prince()
        self.createPlanet("../../images/Planet.png",50,50,375,100,2)
        self.createPlanet("../../images/Planet.png",500,500,750,300,4)
        self.createPlanet("../../images/Planet.png",300,300,1200,600,1)
        self.createPlanet("../../images/Planet.png",200,200,375,600,10)
        self.createPlanet("../../images/Planet.png",100,100,1350,150,7)
        self.display()
        self.play()

    def PrinceFlight(self, prince):
        for planet in self.planetes:
            distance = prince.position.distance_to(Vector2(planet.positionx,planet.positiony))
            acceleration = planet.gravityForce/(distance*distance)
            normaVect = ((planet.positionx,planet.positiony) - prince.position).normalize()
            temps = 1
            prince.speedVector += normaVect * acceleration * temps
        prince.position += prince.speedVector
        self.prince.rectPrinc = self.prince.imgPrince.get_rect(center=self.prince.position)
        self.prince.princeCenter = self.prince.imgPrince.get_rect(center=self.prince.rectPrinc.center)
        print(prince.princeCenter)


    def createPlanet(self,imgPath,width,height,centerPositionx,centerPositiony,rotationAngle):
        planet = Planet.Planet(imgPath,width,height,centerPositionx,centerPositiony,rotationAngle)
        self.planetes.append(planet)

    def addPrinceOnPlanet(self,planet):
        planet.addPrince(prince)

    def removePrinceFromPlanet(self,planet):
        planet.removePrince(prince)





    def display(self):
        #couleur blanche a virer
        self.vueScreen.window.fill((255,255,255))
        for planet in self.planetes:
            self.vueScreen.window.blit(planet.volcano.imgVolcano,planet.volcano.volcanoCenter)
            self.vueScreen.window.blit(planet.imgPlanet,planet.planetCenter)
        self.vueScreen.window.blit(self.prince.imgPrince,self.prince.princeCenter)

    def play(self):
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    done=True
            self.rotate()
            self.PrinceFlight(self.prince)
            self.display()
            pygame.display.update()
            self.vueScreen.clock.tick(30)

    def rotate(self):
<<<<<<< HEAD
        for planet in self.planetes:
            planet.rotationAngle += planet.rotationSpeed
            planet.imgPlanet=pygame.transform.rotozoom(planet.imgPlaneteCopie,planet.rotationAngle,1)
            planet.volcano.imgVolcano=pygame.transform.rotozoom(planet.volcano.imgVolcanCopie,planet.rotationAngle,1)
            planet.planetCenter = planet.imgPlanet.get_rect(center=planet.rectplanet.center)
            planet.volcano.rectVolcano = planet.volcano.imgVolcano.get_rect(center=(planet.positionx+math.cos(math.radians(-planet.rotationAngle))*planet.width/1.8,planet.positiony+math.sin(math.radians(-planet.rotationAngle))*planet.width/1.8))
            planet.volcano.volcanoCenter = planet.volcano.imgVolcano.get_rect(center=planet.volcano.rectVolcano.center)



controleur=GameController()
=======
        for key in self.planetes:
            self.planetes[key].rotationAngle += self.planetes[key].rotationSpeed
            self.planetes[key].imgPlanet=pygame.transform.rotozoom(self.planetes[key].imgPlaneteCopie,self.planetes[key].rotationAngle,1)
            self.planetes[key].volcano.imgVolcano=pygame.transform.rotozoom(self.planetes[key].volcano.imgVolcanCopie,self.planetes[key].rotationAngle,1)
            self.planetes[key].planetCenter = self.planetes[key].imgPlanet.get_rect(center=self.planetes[key].rectplanet.center)
            self.planetes[key].volcano.rectVolcano = self.planetes[key].volcano.imgVolcano.get_rect(center=(self.planetes[key].positionx+math.cos(math.radians(-self.planetes[key].rotationAngle))*self.planetes[key].width/1.8,self.planetes[key].positiony+math.sin(math.radians(-self.planetes[key].rotationAngle))*self.planetes[key].width/1.8))
            self.planetes[key].volcano.volcanoCenter = self.planetes[key].volcano.imgVolcano.get_rect(center=self.planetes[key].volcano.rectVolcano.center)
>>>>>>> e1172be0b7985d13682ac45d11e506a917f7f331
