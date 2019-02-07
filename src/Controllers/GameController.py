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

MIN_SPEED_TO_LEAVE_PLANET = 8
MAX_SPEED = 15
IMMUNITY_THRESHOLD = 10

class GameController:

    def __init__(self):
        self.vueScreen=VueScreen((1680,980))
        self.PhysicEngine = PhysicEngine()
        self.planetes=[]
        self.etoiles=[]
        self.score=0
        self.nbFlowers=0
        self.prince=Prince("../images/animIntro/1.png",(100,100))
        self.PhysicEngine.addPhysicObject(self.prince)

        self.createPlanet("../images/Planet0.png",50,50,500,350,-2)
        self.createPlanet("../images/Planet0.png",500,500,1100,350,0.4)
        self.createPlanet("../images/Planet1.png",300,300,375,750,-0.1)
        self.createPlanet("../images/Planet0.png",200,200,200,150,1, 160)
        self.createPlanet("../images/Planet1.png",100,100,1150,800,-0.7, 160)

        self.createEtoile("../images/Etoile.png",600,600,-1)
        self.createEtoile("../images/Etoile.png",750,50,1)
        self.createEtoile("../images/Etoile.png",200,325,-0.5)
        self.createEtoile("../images/Etoile.png",1400,750,0.5)
        self.createEtoile("../images/Etoile.png",1650,300,3)
        self.createEtoile("../images/Etoile.png",750,920,-2)
        self.createEtoile("../images/Etoile.png",100,900,0.2)

        self.addPrinceOnPlanet(self.planetes[1])
        self.play()

    def PrinceFlight(self, prince):
        prince.position = self.computeObjectTrajectory(prince.position, prince.speedVector)
        prince.position.x = prince.position.x % 1680
        self.prince.rect = self.prince.img.get_rect(center=self.prince.position)
        self.prince.imgCenter = self.prince.img.get_rect(center=self.prince.rect.center)


    def createPlanet(self,imgPath,width,height,centerPositionx,centerPositiony,rotationSpeed, radius = -1):
        planet = Planet(imgPath,(width,height),Vector2(centerPositionx,centerPositiony),rotationSpeed, radius)
        self.planetes.append(planet)
        self.PhysicEngine.addPhysicObject(planet)
        self.PhysicEngine.addPhysicObject(planet.volcano)
        self.PhysicEngine.addPhysicObject(planet.flower)

    def createEtoile(self,imgPath,centerPositionx,centerPositiony,rotationSpeed):
        etoile = Etoile(imgPath,centerPositionx,centerPositiony,rotationSpeed)
        self.etoiles.append(etoile)
        self.PhysicEngine.addPhysicObject(etoile)

    def addPrinceOnPlanet(self,planet):
        planet.addPrince(self.prince)

    def removePrinceFromPlanet(self,planet,initialSpeed):
        planet.removePrince(initialSpeed)

    def display(self):
        self.vueScreen.window.fill((255,255,255))
        for planet in self.planetes:
            self.vueScreen.window.blit(planet.volcano.img, planet.volcano.imgCenter)
            if planet.withFlower :
                self.vueScreen.window.blit(planet.flower.img, planet.flower.imgCenter)
            self.vueScreen.window.blit(planet.img, planet.imgCenter)
        self.vueScreen.window.blit(self.prince.img, self.prince.imgCenter)
        for etoile in self.etoiles:
            if etoile.isHere :
                self.vueScreen.window.blit(etoile.img,etoile.imgCenter)

    def computeObjectTrajectory(self, objPosition, initialSpeed, steps=1):
        positionHistory = []

        for i in range(steps):
            for planet in self.planetes:
                distance = objPosition.distance_to(planet.position)
                acceleration = planet.gravityForce/(distance*distance)
                normaVect = (planet.position - objPosition).normalize()
                temps = 1
                initialSpeed += normaVect * acceleration * temps

            objPosition += initialSpeed
            positionHistory.append(objPosition)

        if steps == 1:
            return positionHistory[0]
        else:
            return positionHistory

    def play(self):
        done=False
        counter,text=10,"10".rjust(3)
        pygame.time.set_timer(pygame.USEREVENT,1000)
        myfont=pygame.font.SysFont("Consolas",30)
        start = time.time()
        while time.time() - start < .5:
            a = pygame.event.get()
        down = False
        posMouse = Vector2(0,0)
        pygame.key.set_repeat(True)

        self.immunity = 100 # immunity to planet collisions
        while not done:
            self.nbFlowers=0
            for event in pygame.event.get():
                if self.prince.parent != None:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        down = True
                        print("sss")
                        #
                        posMouse = Vector2(pygame.mouse.get_pos())
                    elif event.type==pygame.MOUSEBUTTONUP:
                        down = False
                        pos2 = Vector2(pygame.mouse.get_pos())
                        distance = posMouse.distance_to(pos2)
                        vitesse = distance*0.08
                        #vitesse = computeInitialSpeed(posMouse, pos2)
                        if vitesse > MAX_SPEED:
                            vitesse = MAX_SPEED
                        if vitesse > MIN_SPEED_TO_LEAVE_PLANET:
                            self.removePrinceFromPlanet(self.prince.parent, vitesse)
                            self.immunity = 0

                    #if down == True:
                    #    pygame.draw.circle(self.vueScreen, BLUE, pos, 20)

                    if event.type == QUIT:
                        done=True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.prince.rotateAroundParent(6)
                        elif event.key == pygame.K_RIGHT:
                            self.prince.rotateAroundParent(-6)
                    #bloc a rajouter dans le cas de la collision avec une étoile:
                    #    etoile.removeEtoile
            self.immunity += 1

            if time.time()-start>=180:
                done=True
            else:
                text=myfont.render(str(int(180 -(time.time() -start)))+" seconds left !",True, (0, 0, 0), (32, 48))

            self.update_prince(self.prince)
            for planet in self.planetes:
                planet.volcano.chauffe()
                self.update_flowers(planet)
            self.PhysicEngine.updatePhysics()
            self.score+=self.nbFlowers
            self.display()
            self.vueScreen.window.blit(text,(1450,25))
            textScore=myfont.render("Score : "+str(self.score),True,(0,0,0),(32,48))
            self.vueScreen.window.blit(textScore,(1450,80))
            pygame.display.update()
            self.vueScreen.clock.tick(60)


    def update_flowers(self,planet):
        if planet.withFlower :
            self.nbFlowers+=1

    def update_prince(self,prince):
        if prince.parent == None:
            if prince.speedVector.length() != 0:
                prince.rotationAngle=Vector2(1,0).angle_to(Vector2(prince.speedVector.x,-prince.speedVector.y))

            if self.immunity > IMMUNITY_THRESHOLD:
                for planet in self.planetes:
                    if self.prince.isColliding(planet):
                        planet.addPrince(self.prince)
                        prince.rotateAroundParent(-Vector2(1,0).angle_to(prince.position - planet.position))
                        break
            self.PrinceFlight(self.prince)
