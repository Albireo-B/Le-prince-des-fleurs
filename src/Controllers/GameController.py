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
        self.prince=Prince("../images/animIntro/1.png",Vector2(50,250))
        self.PhysicEngine.addPhysicObject(self.prince)
        self.createPlanet("../images/Planet0.png",50,50,375,100,-0.2)
        self.createPlanet("../images/Planet0.png",500,500,750,300,0.4)
        self.createPlanet("../images/Planet1.png",300,300,1200,600,-0.1)
        self.createPlanet("../images/Planet2.png",200,200,375,600,1, 160)
        self.createPlanet("../images/Planet2.png",100,100,1350,150,-0.7, 160)
        self.createEtoile("../images/Etoile.png",600,600,-1)
        self.createEtoile("../images/Etoile.png",1200,350,1)
        self.createEtoile("../images/Etoile.png",200,250,-0.5)
        self.createEtoile("../images/Etoile.png",1400,750,0.5)
        #self.addPrinceOnPlanet(self.planetes[1])
        self.play()

    def PrinceFlight(self, prince):
        for planet in self.planetes:
            distance = prince.position.distance_to(Vector2(planet.positionx,planet.positiony))
            acceleration = planet.gravityForce/(distance*distance)
            normaVect = ((planet.positionx,planet.positiony) - prince.position).normalize()
            temps = 1
            prince.speedVector += normaVect * acceleration * temps
        prince.position += prince.speedVector
        prince.position.x = prince.position.x % 1680
        self.prince.rect = self.prince.img.get_rect(center=self.prince.position)
        self.prince.imgCenter = self.prince.img.get_rect(center=self.prince.rect.center)


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
        self.vueScreen.window.blit(self.prince.img, self.prince.imgCenter)
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
                if event.type == QUIT:
                    done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.prince.angleToParent += 6
                    print("left pressed")
                elif event.key == pygame.K_RIGHT:
                    print("right pressed")
                    self.prince.angleToParent -= 6
                elif event.key == pygame.K_SPACE:
                    if not self.prince.isFlying:
                        self.removePrinceFromPlanet()

            if time.time()-start>=180:
                done=True
            else:
                text=myfont.render(str(int(180 -(time.time() -start)))+" seconds left !",True, (0, 0, 0), (32, 48))
            score+=self.nbFlowers
            self.update_etoiles()
            self.PhysicEngine.updatePhysics()
            score+=self.nbFlowers

            self.update_prince(self.prince)
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


    def update_prince(self,prince):
        if prince.isFlying:
            #for planet in self.planetes:
            #    if prince.isColliding(planet):
            #        print("touché")
            self.PrinceFlight(self.prince)
            if prince.speedVector.length()!= 0:
                prince.rotationAngle=Vector2(0,1).angle_to(Vector2(prince.speedVector.x,-prince.speedVector.y))
            prince.imgPrince=pygame.transform.rotozoom(prince.imgCopie,prince.rotationAngle,1)
        else:
            self.prince.rotationAngle = self.prince.parent.rotationAngle -90 +self.prince.angleToParent
