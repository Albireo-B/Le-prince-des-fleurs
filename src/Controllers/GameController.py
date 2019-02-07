import pygame
from pygame.math import Vector2
from pygame.locals import *

from Objects.Planet import *
from Objects.Object import *
from Objects.Volcano import *
from Objects.Prince import *
from Objects.PhysicObject import *
from Objects.Etoile import *

from Physics.PhysicEngine import *
from Draw.DrawEngine import *

import time

MIN_SPEED_TO_LEAVE_PLANET = 8
MAX_SPEED = 15
IMMUNITY_THRESHOLD = 10
HINT_SIZE = 5

WIDTH = 1024
HEIGHT = 768

class GameController:

    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.PhysicEngine = PhysicEngine()
        self.DrawEngine = DrawEngine(window)
        self.planetes=[]
        self.etoiles=[]
        self.trajectory = []
        self.score=0
        self.nbEtoile=0
        self.peutPoserFleur=True
        self.nbFlowers=0
        pygame.mixer.music.load ('../Sounds/jeu.wav')
        pygame.mixer.music.play()
        self.prince=Prince("../images/animIntro/1.png",(100,100))
        self.PhysicEngine.addPhysicObject(self.prince)
        maskPath = "../images/planetMask.png"
        self.createPlanet("../images/Planet0.png",500,500,900,350,0.4, maskPath)
        self.createPlanet("../images/Planet1.png",300,300,375,750,-0.1, maskPath)
        self.createPlanet("../images/Planet3.png",200,200,100,200,1, maskPath)
        self.createPlanet("../images/Planet4.png",100,100,400,500,-2, maskPath, -2000)
        self.createEtoile("../images/Etoile.png",600,600,-1)
        self.createEtoile("../images/Etoile.png",750,50,1)
        self.createEtoile("../images/Etoile.png",200,325,-0.5)
        self.createEtoile("../images/Etoile.png",1000,600,0.5)
        self.createEtoile("../images/Etoile.png",900,300,3)
        self.createEtoile("../images/Etoile.png",750,300,-2)
        self.createEtoile("../images/Etoile.png",100,300,0.2)


        self.etoileExt1=pygame.image.load("../images/planetMask.png")
        self.etoileExt2=pygame.image.load("../images/planetMask.png")
        self.etoileExt1=pygame.transform.scale(self.etoileExt1,(40,40))
        self.etoileExt2=pygame.transform.scale(self.etoileExt2,(40,40))
        self.roseExterieure=pygame.image.load("../images/rose.png")
        self.roseExterieure=pygame.transform.scale(self.roseExterieure,(75,75))
        self.addPrinceOnPlanet(self.planetes[0])
        self.play()


    def PrinceFlight(self, prince):
        prince.position = self.computeObjectTrajectory(prince.position, prince.speedVector)
        prince.position.x = prince.position.x % 1680
        prince.position.y = prince.position.y % 980
        self.prince.rect = self.prince.img.get_rect(center=self.prince.position)
        self.prince.imgCenter = self.prince.img.get_rect(center=self.prince.rect.center)
        self.prince.maskCenter = Vector2(self.prince.imgCenter[0],self.prince.imgCenter[1])


    def createPlanet(self, imgPath,width,height,centerPositionx,centerPositiony,rotationSpeed, imgMaskPath, gf = -1):
        planet = Planet(imgPath,(width,height),Vector2(centerPositionx,centerPositiony),rotationSpeed, imgMaskPath, gravityForce=gf)
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

    def removePrinceFromPlanet(self,planet):
        planet.removePrince()

    def display(self):
        self.window.fill((255,255,255))
        for planet in self.planetes:
            self.DrawEngine.draw(planet.volcano)
            if planet.withFlower :
                self.DrawEngine.draw(planet.flower)
            self.DrawEngine.draw(planet)
        self.DrawEngine.draw(self.prince)
        for etoile in self.etoiles:
            if etoile.isHere :
                self.DrawEngine.draw(etoile)
        self.window.blit(self.etoileExt1,(1580,880))
        self.window.blit(self.etoileExt2,(1630,880))
        self.window.blit(self.roseExterieure,(1580,800))
        for pos in self.trajectory:
            fade = (1 - pos[1]/MAX_SPEED)*255
            fade1 = 0
            if (fade < 0):
                fade1 = - fade
                fade = 0
            else:
                fade1 = fade
            if fade1 > 255:
                fade1 = 255
            pygame.draw.circle(self.window, (fade, fade1, 255), (int(pos[0].x), int(pos[0].y)), HINT_SIZE)

    def scaling_volcano(self,planet):
        if planet.volcano.eruptionCycle%(2*planet.volcano.i)<planet.volcano.i:
            planet.volcano.img = pygame.transform.scale(planet.volcano.img, (int(planet.volcano.size[0]+planet.volcano.eruptionCycle%planet.volcano.i*planet.volcano.f/planet.volcano.i), int(planet.volcano.size[1]+planet.volcano.eruptionCycle%planet.volcano.i*planet.volcano.f/planet.volcano.i)))
        else:
            planet.volcano.img = pygame.transform.scale(planet.volcano.img, (int(planet.volcano.size[0]+planet.volcano.f-planet.volcano.eruptionCycle%planet.volcano.i*planet.volcano.f/planet.volcano.i), int(planet.volcano.size[1]+planet.volcano.f-planet.volcano.eruptionCycle%planet.volcano.i*planet.volcano.f/planet.volcano.i)))


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
            if len(positionHistory) > 1:
                if (objPosition - positionHistory[-1][0]).length() > 100:
                    break
                elif (objPosition - positionHistory[-1][0]).length() > 50:
                    positionHistory.append([Vector2(objPosition), initialSpeed.length()])
            else:
                positionHistory.append([Vector2(objPosition), initialSpeed.length()])

        if steps == 1:
            return positionHistory[0][0]
        else:
            return positionHistory

    def computeInitialSpeed(self, pos1, posPrince, planet):
        pos2 = Vector2(pygame.mouse.get_pos())
        distance = pos2.y - pos1.y
        if distance < 0:
            distance = 0
        absSpeed = distance*0.08
        if absSpeed > MAX_SPEED:
            absSpeed = MAX_SPEED
        speed = (posPrince - planet.position).normalize()*absSpeed
        return speed

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
                        posMouse = Vector2(pygame.mouse.get_pos())
                    elif event.type==pygame.MOUSEBUTTONUP:
                        down = False
                        self.trajectory = []
                        speed = self.computeInitialSpeed(posMouse, self.prince.imgCenter.center, self.prince.parent)
                        if speed.length() > MIN_SPEED_TO_LEAVE_PLANET:
                            self.removePrinceFromPlanet(self.prince.parent)
                            self.prince.speedVector = speed
                            self.immunity = 0

                    pygame.draw.circle(self.window, (0,0,255), (200, 200), 100)

                    if event.type == QUIT:
                        done=True
                    elif event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_DOWN:
                            self.update_sweeping()
                        elif event.key == pygame.K_LEFT:
                            self.prince.rotateAroundParent(6)
                        elif event.key == pygame.K_RIGHT:
                            self.prince.rotateAroundParent(-6)
                        elif event.key == pygame.K_SPACE:
                            if self.peutPoserFleur and self.prince.parent != None:
                                self.prince.putFlower()
                    #bloc a rajouter dans le cas de la collision avec une étoile:
                    #    etoile.removeEtoile
            if down:
                speed = self.computeInitialSpeed(posMouse, self.prince.imgCenter.center, self.prince.parent)
                if speed.length() > MIN_SPEED_TO_LEAVE_PLANET:
                    self.trajectory = self.computeObjectTrajectory(Vector2(self.prince.imgCenter.center[0], self.prince.imgCenter.center[1]), speed, 60)
                else:
                    self.trajectory = []

            self.immunity += 1


            if time.time()-start>=180:
                done=True
            else:
                text=myfont.render(str(int(180 -(time.time() -start)))+" seconds left !",True, (0, 0, 0), (32, 48))
            textEtoiles=myfont.render("Stars : " + str(self.nbEtoile),True,(0,0,0),(32,48))
            if self.nbEtoile>=2:
                self.peutPoserFleur=True
                while (self.nbEtoile>2):
                    self.nbEtoile-=1
                    self.score+=200

            if self.nbEtoile==1:
                self.etoileExt1=pygame.image.load("../images/Etoile.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(40,40))
                self.etoileExt2=pygame.image.load("../images/planetMask.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(40,40))
                self.roseExterieure=pygame.image.load("../images/planetMask.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(75,75))
            elif self.nbEtoile==2:
                self.etoileExt1=pygame.image.load("../images/Etoile.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(40,40))
                self.etoileExt2=pygame.image.load("../images/Etoile.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(40,40))
                self.roseExterieure=pygame.image.load("../images/rose.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(75,75))
            else:
                self.etoileExt1=pygame.image.load("../images/planetMask.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(40,40))
                self.etoileExt2=pygame.image.load("../images/planetMask.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(40,40))
                self.roseExterieure=pygame.image.load("../images/planetMask.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(75,75))
            self.update_prince(self.prince)
            self.update_etoiles()
            for planet in self.planetes:
                planet.volcano.chauffe()
                self.update_flowers(planet)

            self.PhysicEngine.updatePhysics()
            self.score+=self.nbFlowers
            self.display()
            self.window.blit(textEtoiles,(1450,135))
            self.window.blit(text,(1450,25))
            textScore=myfont.render("Score : "+str(self.score),True,(0,0,0),(32,48))
            self.window.blit(textScore,(1450,80))
            pygame.display.update()
            self.clock.tick(60)

    def update_sweeping(self):
        for planet in self.planetes:
            if self.prince.isColliding(planet.volcano) and planet.volcano.eruptionCycle<900:
                planet.volcano.clean()

    def update_etoiles(self):
        for etoile in self.etoiles:
            if self.prince.isColliding(etoile) and etoile.isHere:
                self.nbEtoile+=1
                etoile.removeEtoile()

    def update_flowers(self,planet):
        if planet.withFlower:
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
