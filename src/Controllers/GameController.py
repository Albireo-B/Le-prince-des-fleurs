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
        self.background=pygame.image.load("../images/background.jpg").convert()
        self.background=pygame.transform.scale(self.background,(1024,768))
        self.PhysicEngine = PhysicEngine()
        self.DrawEngine = DrawEngine(window)
        self.planetes = []
        self.etoiles = []
        self.trajectory = []
        self.score=0
        self.nbEtoile=0
        self.peutPoserFleur=True
        self.nbFlowers=0
        pygame.mixer.music.load ('../Sounds/jeu.wav')
        pygame.mixer.music.play()
        self.prince=Prince("../images/walk1.png",(int(74/1.5),int(120/1.5)))
        self.PhysicEngine.addPhysicObject(self.prince)
        maskPath = "../images/planetMask.png"
        self.createPlanet("../images/Planet0.png",250,250,800,250,0.4, maskPath)
        self.createPlanet("../images/Planet1.png",200,200,150,200,-0.1, maskPath)
        self.createPlanet("../images/Planet3.png",175,175,175,600,-0.7, maskPath)
        self.createPlanet("../images/Planet4.png",100,100,450,400,1, maskPath, -2000)
        self.createPlanet("../images/Planet2.png",150,150,750,600,-0.7, maskPath)
        self.createPlanet("../images/Planet1.png",120,120,500,80,-0.7, maskPath)
        self.createEtoile("../images/Etoile.png",300,500,-0.7)
        self.createEtoile("../images/Etoile.png",375,40,0.7)
        self.createEtoile("../images/Etoile.png",100,350,-0.5)
        self.createEtoile("../images/Etoile.png",500,550,0.5)
        self.createEtoile("../images/Etoile.png",450,275,1.5)
        self.createEtoile("../images/Etoile.png",375,260,-1.2)
        self.createEtoile("../images/Etoile.png",50,220,0.2)


        self.etoileExt1=pygame.image.load("../images/planetMask.png")
        self.etoileExt2=pygame.image.load("../images/planetMask.png")
        self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
        self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
        self.roseExterieure=pygame.image.load("../images/rose.png")
        self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))
        self.addPrinceOnPlanet(self.planetes[0])
        self.play()


    def PrinceFlight(self, prince):
        prince.position = self.computeObjectTrajectory(prince.position, prince.speedVector)
        prince.position.x = prince.position.x % 1024
        prince.position.y = prince.position.y % 768
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
        self.window.blit(self.background,(0,0))
        for planet in self.planetes:
            self.DrawEngine.draw(planet.volcano)
            if planet.withFlower :
                self.DrawEngine.draw(planet.flower)
            self.DrawEngine.draw(planet)
        self.DrawEngine.draw(self.prince)
        for etoile in self.etoiles:
            if etoile.isHere :
                self.DrawEngine.draw(etoile)
        self.window.blit(self.etoileExt1,(940,700))
        self.window.blit(self.etoileExt2,(970,700))
        self.window.blit(self.roseExterieure,(945,650))
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
            if down:
                speed = self.computeInitialSpeed(posMouse, self.prince.imgCenter.center, self.prince.parent)
                if speed.length() > MIN_SPEED_TO_LEAVE_PLANET:
                    self.trajectory = self.computeObjectTrajectory(Vector2(self.prince.imgCenter.center[0], self.prince.imgCenter.center[1]), speed, 60)
                else:
                    self.trajectory = []

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
                            self.prince.loadImage(self.prince.imgVol)

                    pygame.draw.circle(self.window, (0,0,255), (200, 200), 100)

                    if event.type == QUIT:
                        done=True
                    elif event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_DOWN:
                            self.update_sweeping()
                        elif event.key == pygame.K_LEFT:
                            self.prince.rotateAroundParent(3)
                            self.prince.nextWalkFrame(True)
                        elif event.key == pygame.K_RIGHT:
                            self.prince.rotateAroundParent(-3)
                            self.prince.nextWalkFrame(False)
                        elif event.key == pygame.K_SPACE:
                            if self.peutPoserFleur and self.prince.parent != None:
                                self.prince.putFlower()
                    #bloc a rajouter dans le cas de la collision avec une étoile:
                    #    etoile.removeEtoile


            self.immunity += 1


            if time.time()-start>=180:
                done=True
            else:
                text=myfont.render(str(int(180 -(time.time() -start)))+" seconds left !",True, (0, 0, 0), (32, 48))
            if self.nbEtoile>=2:
                self.peutPoserFleur=True
                while (self.nbEtoile>2):
                    self.nbEtoile-=1
                    self.score+=200

            if self.nbEtoile==1:
                self.etoileExt1=pygame.image.load("../images/Etoile.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
                self.etoileExt2=pygame.image.load("../images/planetMask.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
                self.roseExterieure=pygame.image.load("../images/planetMask.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))
            elif self.nbEtoile==2:
                self.etoileExt1=pygame.image.load("../images/Etoile.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
                self.etoileExt2=pygame.image.load("../images/Etoile.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
                self.roseExterieure=pygame.image.load("../images/rose.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))
            else:
                self.etoileExt1=pygame.image.load("../images/planetMask.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
                self.etoileExt2=pygame.image.load("../images/planetMask.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
                self.roseExterieure=pygame.image.load("../images/planetMask.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))

            self.PhysicEngine.updatePhysics()
            self.update_prince(self.prince)
            self.update_etoiles()
            for planet in self.planetes:
                planet.volcano.chauffe()
                self.update_flowers(planet)


            self.score+=self.nbFlowers
            self.display()

            self.window.blit(text,(850,10))
            textScore=myfont.render("Score : "+str(self.score),True,(0,0,0),(32,48))
            self.window.blit(textScore,(850,35))
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
            etoile.updateRespawnCptr()

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
