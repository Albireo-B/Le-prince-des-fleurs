import pygame
from pygame.math import Vector2


from Objects.Planet import *
from Objects.Object import *
from Objects.Volcano import *
from Objects.VueScreen import *
from Objects.Prince import *
from Objects.PhysicObject import *



class GameController:

    def __init__(self):
        self.vueScreen=VueScreen((1500,750))
        self.planetes=[]
        self.prince=Prince("../images/animIntro/1.png")
        #self.prince=Prince()
        self.createPlanet("../../images/Planet.png",50,50,375,100,-0.2)
        self.createPlanet("../../images/Planet.png",500,500,750,300,0.4)
        self.createPlanet("../../images/Planet.png",300,300,1200,600,-0.1)
        self.createPlanet("../../images/Planet.png",200,200,375,600,0.10)
        self.createPlanet("../../images/Planet.png",100,100,1350,150,-0.7)
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


    def createPlanet(self,imgPath,width,height,centerPositionx,centerPositiony,rotationAngle):
        planet = Planet(imgPath,width,height,centerPositionx,centerPositiony,rotationAngle)
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
            self.update_planet()
            self.PrinceFlight(self.prince)
            self.display()
            pygame.display.update()
            self.vueScreen.clock.tick(60)

    def update_planet(self):
        for planet in self.planetes:
            planet.volcano.chauffe()
            planet.rotationAngle += planet.rotationSpeed
            planet.imgPlanet=pygame.transform.rotozoom(planet.imgPlaneteCopie,planet.rotationAngle,1)
            planet.volcano.imgVolcano=pygame.transform.rotozoom(planet.volcano.imgVolcanCopie,planet.rotationAngle,1)
            planet.planetCenter = planet.imgPlanet.get_rect(center=planet.rectplanet.center)
            planet.volcano.rectVolcano = planet.volcano.imgVolcano.get_rect(center=(planet.positionx+math.cos(math.radians(-planet.rotationAngle))*planet.width/1.8,planet.positiony+math.sin(math.radians(-planet.rotationAngle))*planet.width/1.8))
            planet.volcano.volcanoCenter = planet.volcano.imgVolcano.get_rect(center=planet.volcano.rectVolcano.center)
