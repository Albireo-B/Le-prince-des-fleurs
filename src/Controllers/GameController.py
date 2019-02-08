import pygame
from pygame.math import Vector2
from pygame.locals import *

from Objects.Planet import *
from Objects.Object import *
from Objects.Volcano import *
from Objects.Prince import *
from Objects.PhysicObject import *
from Objects.Etoile import *
import sys
from Physics.PhysicEngine import *
from Draw.DrawEngine import *

import time

MIN_SPEED_TO_LEAVE_PLANET = 5
MAX_SPEED = 9
IMMUNITY_THRESHOLD = 10
HINT_SIZE = 5

PRINCE_SPEED = 1.5

WIDTH = 1024
HEIGHT = 768

OUT_OF_BOUND_MARGIN = 300

HINT_ARROW_SIZE = 60

MAX_MOUSE_DRAG_DISTANCE = 400

class GameController:

    def __init__(self, window, withVolcanos, niv):
        self.niveau=niv
        self.window = window

        self.jumpSound = pygame.mixer.Sound('../Sounds/jump.wav')
        self.landSound = pygame.mixer.Sound('../Sounds/land.wav')
        self.starSound = pygame.mixer.Sound('../Sounds/bell.wav')
        self.sweepSound = pygame.mixer.Sound('../Sounds/sweep.wav')

        self.princeHideHint = Object(Vector2(0,0), None, "../images/arrow.png", (HINT_ARROW_SIZE, HINT_ARROW_SIZE))
        self.arrowVisible = False
        self.withVolcanos=withVolcanos
        self.clock = pygame.time.Clock()
        self.background=pygame.image.load("../images/background.jpg").convert()
        self.background=pygame.transform.scale(self.background,(1024,768))
        self.PhysicEngine = PhysicEngine()
        self.DrawEngine = DrawEngine(window)
        self.planetes = []
        self.etoiles = []
        self.trajectory = []
        self.score = 0
        self.nbEtoile = 0
        self.peutPoserFleur=True
        self.nbFlowers=0
        pygame.mixer.music.load ('../Sounds/jeu.wav')
        pygame.mixer.music.play()
        self.prince=Prince("../images/walk1.png",(int(74/1.5),int(120/1.5)))
        self.PhysicEngine.addPhysicObject(self.prince)
        maskPath = "../images/planetMask.png"

        if self.niveau==3:
            self.createPlanet("../images/Planet0.png",250,250,800,250,0.4, maskPath)
            self.createPlanet("../images/Planet1.png",200,200,150,200,-0.1, maskPath)
            self.createPlanet("../images/Planet3.png",175,175,175,600,-0.7, maskPath)
            self.createPlanet("../images/Planet4.png",100,100,450,400,1, maskPath, -2000)
            self.createPlanet("../images/Planet2.png",150,150,750,600,-0.7, maskPath)
            self.createPlanet("../images/Planet1.png",120,120,500,80,-0.7, maskPath)
            self.createEtoile("../images/Etoile.png",330,570,-0.7)
            self.createEtoile("../images/Etoile.png",375,40,0.7)
            self.createEtoile("../images/Etoile.png",100,350,-0.5)
            self.createEtoile("../images/Etoile.png",550,650,0.5)
            self.createEtoile("../images/Etoile.png",800,100,1.5)
            self.createEtoile("../images/Etoile.png",375,260,-1.2)
            self.createEtoile("../images/Etoile.png",580,375,0.2)
            self.createEtoile("../images/Etoile.png",900,550,0.3)
            self.etoileExt1=pygame.image.load("../images/planetMask.png")
            self.etoileExt2=pygame.image.load("../images/planetMask.png")
            self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
            self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
            self.roseExterieure=pygame.image.load("../images/rose.png")
            self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))
        elif self.niveau==1:
            self.withVolcanos=False
            self.createPlanet("../images/Planet0.png",250,250,800,250,0.4, maskPath)
            self.createPlanet("../images/Planet1.png",200,200,150,200,-0.1, maskPath)
            self.createPlanet("../images/Planet3.png",175,175,450,600,-0.7, maskPath)
            self.createEtoile("../images/Etoile.png",330,570,-0.7)
            self.createEtoile("../images/Etoile.png",375,40,0.7)
            self.createEtoile("../images/Etoile.png",100,350,-0.5)
            self.createEtoile("../images/Etoile.png",550,650,0.5)
            self.createEtoile("../images/Etoile.png",800,100,1.5)
            self.createEtoile("../images/Etoile.png",375,260,-1.2)
            self.createEtoile("../images/Etoile.png",580,375,0.2)
            self.createEtoile("../images/Etoile.png",900,550,0.3)
            self.etoileExt1=pygame.image.load("../images/EtoileGrisee.png")
            self.etoileExt2=pygame.image.load("../images/EtoileGrisee.png")
            self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
            self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
            self.roseExterieure=pygame.image.load("../images/roseGrisee.png")
            self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))
        else:
            self.withVolcanos=True
            self.createPlanet("../images/Planet0.png",250,250,800,250,0.4, maskPath)
            self.createPlanet("../images/Planet1.png",200,200,150,200,-0.1, maskPath)
            self.createPlanet("../images/Planet4.png",175,175,450,600,-0.7, maskPath,-2000)
            self.createEtoile("../images/Etoile.png",330,570,-0.7)
            self.createEtoile("../images/Etoile.png",375,40,0.7)
            self.createEtoile("../images/Etoile.png",100,350,-0.5)
            self.createEtoile("../images/Etoile.png",550,650,0.5)
            self.createEtoile("../images/Etoile.png",800,100,1.5)
            self.createEtoile("../images/Etoile.png",375,260,-1.2)
            self.createEtoile("../images/Etoile.png",580,375,0.2)
            self.createEtoile("../images/Etoile.png",900,550,0.3)
            self.etoileExt1=pygame.image.load("../images/EtoileGrisee.png")
            self.etoileExt2=pygame.image.load("../images/EtoileGrisee.png")
            self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
            self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
            self.roseExterieure=pygame.image.load("../images/roseGrisee.png")
            self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))

        self.addPrinceOnPlanet(self.planetes[0])
        self.play()

    def PrinceFlight(self, prince):
        prince.setPosition(self.computeObjectTrajectory(prince.position, prince.speedVector))

        if prince.position.y < -OUT_OF_BOUND_MARGIN or prince.position.y > HEIGHT + OUT_OF_BOUND_MARGIN:
            prince.speedVector.y = -prince.speedVector.y*.5

        if prince.position.x < -OUT_OF_BOUND_MARGIN*1.5:
            prince.setPosition(Vector2(WIDTH+OUT_OF_BOUND_MARGIN*1.5, prince.position.y))
            prince.speedVector.x *= .7
        if prince.position.x > WIDTH + OUT_OF_BOUND_MARGIN*1.5:
            prince.setPosition(Vector2(-OUT_OF_BOUND_MARGIN*1.5, prince.position.y))
            prince.speedVector.x *= .3

        self.arrowVisible = True
        if prince.position.x < 0:
            if prince.position.y < 0:
                self.princeHideHint.setPosition(Vector2(HINT_ARROW_SIZE/2, HINT_ARROW_SIZE/2))
                self.princeHideHint.setRotation(135)
            elif prince.position.y > HEIGHT:
                self.princeHideHint.setPosition(Vector2(HINT_ARROW_SIZE/2, HEIGHT - HINT_ARROW_SIZE/2))
                self.princeHideHint.setRotation(-135)
            else:
                self.princeHideHint.setPosition(Vector2(HINT_ARROW_SIZE/2, prince.position.y + HINT_ARROW_SIZE/2))
                self.princeHideHint.setRotation(180)
        elif prince.position.x > WIDTH:
            if prince.position.y < 0:
                self.princeHideHint.setPosition(Vector2(WIDTH - HINT_ARROW_SIZE/2, HINT_ARROW_SIZE/2))
                self.princeHideHint.setRotation(45)
            elif prince.position.y > HEIGHT:
                self.princeHideHint.setPosition(Vector2(WIDTH - HINT_ARROW_SIZE/2, HEIGHT - HINT_ARROW_SIZE/2))
                self.princeHideHint.setRotation(-45)
            else:
                self.princeHideHint.setPosition(Vector2(WIDTH - HINT_ARROW_SIZE/2, prince.position.y + HINT_ARROW_SIZE/2))
                self.princeHideHint.setRotation(0)
        else:
            if prince.position.y < 0:
                self.princeHideHint.setPosition(Vector2(prince.position.x + HINT_ARROW_SIZE/2, HINT_ARROW_SIZE/2))
                self.princeHideHint.setRotation(90)
            elif prince.position.y > HEIGHT:
                self.princeHideHint.setPosition(Vector2(prince.position.x + HINT_ARROW_SIZE/2, HEIGHT - HINT_ARROW_SIZE/2))
                self.princeHideHint.setRotation(-90)
            else:
                self.arrowVisible = False

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
            if planet.withFlower:
                self.DrawEngine.draw(planet.flower)
            self.DrawEngine.draw(planet)
            if planet.prince != None:
                self.DrawEngine.draw(self.prince)
            if self.withVolcanos:
                self.DrawEngine.draw(planet.volcano)
        if self.prince.parent == None:
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
        if self.arrowVisible:
            self.DrawEngine.draw(self.princeHideHint)


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
        if distance > MAX_MOUSE_DRAG_DISTANCE:
            distance = MAX_MOUSE_DRAG_DISTANCE

        absSpeed = (distance/MAX_MOUSE_DRAG_DISTANCE)*MAX_SPEED
        if absSpeed > MAX_SPEED:
            absSpeed = MAX_SPEED
        speed = (posPrince - planet.position).normalize()*absSpeed
        return speed

    def play(self):
        done=False
        counter,text=10,"10".rjust(3)
        pygame.time.set_timer(pygame.USEREVENT,1000)
        myfont=pygame.font.SysFont("Consolas",18)
        start = time.time()
        while time.time() - start < .5:
            a = pygame.event.get()
        down = False
        posMouse = Vector2(0, 0)
        pygame.key.set_repeat(True)
        self.immunity = 100 # immunity to planet collisions
        hasKeyEvent = False
        jump = False
        while not done:
            self.nbFlowers=0
            hasEvents = False
            if down:
                speed = self.computeInitialSpeed(posMouse, self.prince.imgCenter.center, self.prince.parent)
                if speed.length() > MIN_SPEED_TO_LEAVE_PLANET and not hasKeyEvent:
                    self.trajectory = self.computeObjectTrajectory(Vector2(self.prince.imgCenter.center[0], self.prince.imgCenter.center[1]), speed, 60)
                else:
                    self.trajectory = []
            hasKeyEvent = False

            for event in pygame.event.get():
                hasEvents = True
                if self.prince.parent != None:
                    if event.type == QUIT:
                        done=True
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('../Sounds/menu.wav')
                        pygame.mixer.music.play(-1)
                    elif event.type == pygame.KEYDOWN:
                        hasKeyEvent = True
                        if event.key==pygame.K_DOWN:
                            self.update_sweeping()
                        elif event.key == pygame.K_LEFT:
                            self.prince.walkAround(PRINCE_SPEED)
                            self.prince.nextWalkFrame(True)
                        elif event.key == pygame.K_RIGHT:
                            self.prince.walkAround(-PRINCE_SPEED)
                            self.prince.nextWalkFrame(False)
                        elif event.key == pygame.K_UP:
                            for planet in self.planetes:
                                if self.prince.isColliding(planet):
                                    if self.peutPoserFleur and self.prince.parent !=None and not planet.withFlower and planet.volcano.eruptionCycle<1500:
                                        self.prince.putFlower()
                                        self.peutPoserFleur=False
                                        planet.withFlower=True
                                        self.nbEtoile=0
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        down = True
                        posMouse = Vector2(pygame.mouse.get_pos())
                        self.prince.loadImage(self.prince.imgJump)
                    elif event.type==pygame.MOUSEBUTTONUP:
                        down = False
                        jump = True
                    pygame.draw.circle(self.window, (0,0,255), (200, 200), 100)
            #Gestion du saut:
            if jump:
                if not hasKeyEvent:
                    self.trajectory = []
                    speed = self.computeInitialSpeed(posMouse, self.prince.imgCenter.center, self.prince.parent)
                    if speed.length() > MIN_SPEED_TO_LEAVE_PLANET:
                        pygame.mixer.Sound.play(self.jumpSound)
                        self.removePrinceFromPlanet(self.prince.parent)
                        self.prince.speedVector = speed
                        self.immunity = 0
                        self.prince.loadImage(self.prince.imgVol)
                jump = False

            if not hasEvents and down:
                self.prince.loadImage(self.prince.imgJump)
            elif not hasKeyEvent and not down and self.prince.parent != None:
                self.prince.loadImage(self.prince.imgIdle)
            self.immunity += 1

            if time.time()-start>=180:
                done=True
            else:
                text=myfont.render(str(int(180 -(time.time() -start)))+" secondes restantes",True, (255, 255, 255), (32, 48))
            if self.nbEtoile>=2:
                self.peutPoserFleur=True
                while (self.nbEtoile>2):
                    self.nbEtoile-=1
                    self.score+=200

            if self.nbEtoile==1:
                self.etoileExt1=pygame.image.load("../images/Etoile.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
                self.etoileExt2=pygame.image.load("../images/EtoileGrisee.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
                self.roseExterieure=pygame.image.load("../images/roseGrisee.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))
            elif self.nbEtoile==2:
                self.etoileExt1=pygame.image.load("../images/Etoile.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
                self.etoileExt2=pygame.image.load("../images/Etoile.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
                self.roseExterieure=pygame.image.load("../images/rose.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))
            else:
                self.etoileExt1=pygame.image.load("../images/EtoileGrisee.png")
                self.etoileExt1=pygame.transform.scale(self.etoileExt1,(20,20))
                self.etoileExt2=pygame.image.load("../images/EtoileGrisee.png")
                self.etoileExt2=pygame.transform.scale(self.etoileExt2,(20,20))
                self.roseExterieure=pygame.image.load("../images/roseGrisee.png")
                self.roseExterieure=pygame.transform.scale(self.roseExterieure,(37,37))

            self.update_prince(self.prince)
            self.update_etoiles()
            for planet in self.planetes:
                if self.withVolcanos:
                    planet.volcano.chauffe()
                    if planet.withFlower and planet.volcano.eruptionCycle>=1699 :
                            self.score-=500
                            print(';oinms de points')
                self.update_flowers(planet)

            self.PhysicEngine.updatePhysics()

            self.score+=self.nbFlowers
            self.display()

            self.window.blit(text,(800,10))
            textScore=myfont.render("Score : "+str(self.score),True,(255,255,255),(32,48))
            self.window.blit(textScore,(850,35))
            pygame.display.update()
            self.clock.tick(60)

    def update_sweeping(self):
        for planet in self.planetes:
            if self.prince.isColliding(planet.volcano) and planet.volcano.eruptionCycle<1500:
                pygame.mixer.Sound.play(self.sweepSound)
                planet.volcano.clean()

    def update_etoiles(self):
        for etoile in self.etoiles:
            if self.prince.isColliding(etoile) and etoile.isHere:
                self.nbEtoile+=1
                pygame.mixer.Sound.play(self.starSound)
                etoile.removeEtoile()
            etoile.updateRespawnCptr()

    def update_flowers(self,planet):
        if planet.withFlower:
            self.nbFlowers+=1

    def update_prince(self,prince):
        if prince.parent == None:
            if prince.speedVector.length() != 0:
                prince.setRotation(Vector2(1,0).angle_to(Vector2(prince.speedVector.x,-prince.speedVector.y)))
                prince.updateMask(prince.img)

            if self.immunity > IMMUNITY_THRESHOLD:
                for planet in self.planetes:
                    if self.prince.isColliding(planet):
                        pygame.mixer.Sound.play(self.landSound)
                        self.arrowVisible = False
                        planet.addPrince(self.prince)
                        prince.rotateAroundParent(-Vector2(1,0).angle_to(prince.position - planet.position))
                        break
            self.PrinceFlight(self.prince)
