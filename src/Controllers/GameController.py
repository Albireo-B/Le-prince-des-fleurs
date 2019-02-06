import pygame
from pygame.math import Vector2


from Objects.Planet import *
from Objects.Object import *
from Objects.Volcano import *
from Objects.VueScreen import *
from Objects.Prince import *
from Objects.PhysicObject import *
from Objects.Etoile import *

from Physics.PhysicEngine import *

import time

class GameController:

    def __init__(self):
        self.vueScreen=VueScreen((1680,980))
        self.PhysicEngine = PhysicEngine()
        self.planetes=[]
        self.etoiles=[]
        self.nbFlowers=0
        self.prince=Prince("../images/animIntro/1.png")
        #self.prince=Prince()
        self.createPlanet("../images/Planet0.png",50,50,375,100,-0.2)
        self.createPlanet("../images/Planet0.png",500,500,750,300,0.4)
        self.createPlanet("../images/Planet1.png",300,300,1200,600,-0.1)
        self.createPlanet("../images/Planet2.png",200,200,375,600,1, 160)
        self.createPlanet("../images/Planet2.png",100,100,1350,150,-0.7, 160)
        self.createEtoile("../images/Etoile.png",600,600,-1)
        self.createEtoile("../images/Etoile.png",1200,350,1)
        self.createEtoile("../images/Etoile.png",200,250,-0.5)
        self.createEtoile("../images/Etoile.png",1400,750,0.5)
        self.addPrinceOnPlanet(self.planetes[1])
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


    def createPlanet(self,imgPath,width,height,centerPositionx,centerPositiony,rotationAngle, radius = -1):
        planet = Planet(imgPath,(width,height),Vector2(centerPositionx,centerPositiony),rotationAngle, radius)
        self.planetes.append(planet)
        self.PhysicEngine.addPhysicObject(planet)
        self.PhysicEngine.addPhysicObject(planet.volcano)

    def createEtoile(self,imgPath,centerPositionx,centerPositiony,rotationAngle):
        etoile = Etoile(imgPath,centerPositionx,centerPositiony,rotationAngle)
        self.etoiles.append(etoile)

    def addPrinceOnPlanet(self,planet):
        planet.addPrince(self.prince)

    def removePrinceFromPlanet(self,planet,initialSpeed):
        planet.removePrince(initialSpeed)


    def display(self):
        #couleur blanche a virer
        self.vueScreen.window.fill((255,255,255))
        for planet in self.planetes:
            self.vueScreen.window.blit(planet.volcano.img, planet.volcano.imgCenter)
            self.vueScreen.window.blit(planet.img, planet.imgCenter)
        self.vueScreen.window.blit(self.prince.imgPrince, self.prince.princeCenter)
        for etoile in self.etoiles:
            self.vueScreen.window.blit(etoile.imgEtoile,etoile.etoileCenter)

    def play(self):
        done=False
        counter,text=10,"10".rjust(3)
        pygame.time.set_timer(pygame.USEREVENT,1000)
        myfont=pygame.font.SysFont("Consolas",30)
        #stockage de 2 position   MOUSEBUTTONDOWN et MOUSEBUTTONUP
        start = time.time()
        score=0
        down = False
        posMouse = Vector2(0,0)
        while not done:
            for event in pygame.event.get():
                if down == False:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        down = True
                        posMouse = pygame.mouse.get_pos()

                elif down == True:
                    if event.type==pygame.MOUSEBUTTONUP:
                        down = False
                        pos2 = pygame.mouse.get_pos()
                        distance = posMouse.distance_to(pos2)
                        vitesse = distance*2
                        self.removePrinceFromPlanet(self.prince.volcano, vitesse)

                if event.type == pygame.quit:
                    done=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.prince.princeAnglePlanet += 6
                        print("left pressed")
                    elif event.key == pygame.K_RIGHT:
                        print("right pressed")
                        self.prince.princeAnglePlanet -= 6
                    elif event.key == pygame.K_SPACE:
                        if not self.prince.isFlying:
                            self.removePrinceFromPlanet()

            if time.time()-start>=180:
                print("Time's up:")
                done=True
            else:
                text=myfont.render(str(int(180 -(time.time() -start)))+" seconds left !",True, (0, 0, 0), (32, 48))
            score+=self.nbFlowers
            self.update_etoiles()
            self.PhysicEngine.updatePhysics()
            score+=self.nbFlowers
            self.update_flight(self.prince)
            self.update_planet()
            self.display()
            self.vueScreen.window.blit(text,(1450,25))
            textScore=myfont.render("Score :"+str(score),True,(0,0,0),(32,48))
            self.vueScreen.window.blit(textScore,(1450,80))
            pygame.display.update()
            self.vueScreen.clock.tick(100)

    def update_etoiles(self):
        for etoile in self.etoiles:
                etoile.rotationAngle += etoile.rotationSpeed
                etoile.imgEtoile=pygame.transform.rotozoom(etoile.imgEtoileCopie,etoile.rotationAngle,1)
                etoile.etoileCenter = etoile.imgEtoile.get_rect(center=etoile.rectEtoile.center)


    def update_flight(self,prince):
        if prince.isFlying:
            self.PrinceFlight(self.prince)
            if prince.speedVector.length()!= 0:
                prince.princeAngle=Vector2(0,1).angle_to(Vector2(prince.speedVector.x,-prince.speedVector.y))
            prince.imgPrince=pygame.transform.rotozoom(prince.imgPrinceCopie,prince.princeAngle,1)


    def update_planet(self):
        for planet in self.planetes:
            planet.volcano.chauffe()
            #planet.volcano.img = pygame.transform.rotozoom(planet.volcano.imgCopie, planet.rotationAngle, 1)

            #planet.volcano.rectVolcano = planet.volcano.img.get_rect(center=(planet.position.x+math.cos(math.radians(-planet.rotationAngle))*planet.size[0]/1.8,planet.position.y+math.sin(math.radians(-planet.rotationAngle))*planet.size[0]/1.8))
            #planet.volcano.volcanoCenter = planet.volcano.img.get_rect(center=planet.volcano.rectVolcano.center)
            if planet.prince!=None:
                planet.prince.princeAngle = planet.rotationAngle -90 +self.prince.princeAnglePlanet
                self.prince.imgPrince=pygame.transform.rotozoom(self.prince.imgPrinceCopie,self.prince.princeAngle,1)
                self.prince.rectPrince = self.prince.imgPrince.get_rect(center=(planet.position.x+math.cos(math.radians(-planet.rotationAngle-self.prince.princeAnglePlanet))*planet.size[0]/1.8,planet.position.y+math.sin(math.radians(-planet.rotationAngle-self.prince.princeAnglePlanet))*planet.size[0]/1.8))
                self.prince.princeCenter = self.prince.imgPrince.get_rect(center=self.prince.rectPrince.center)
