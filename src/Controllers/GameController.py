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
        self.vueScreen=VueScreen((1680,980))
        self.planetes=[]
        self.prince=Prince("../images/animIntro/1.png")
        #self.prince=Prince()
        self.createPlanet("../images/Planet0.png",50,50,375,100,-0.2)
        self.createPlanet("../images/Planet0.png",500,500,750,300,0.4)
        self.createPlanet("../images/Planet1.png",300,300,1200,600,-0.1)
        self.createPlanet("../images/Planet2.png",200,200,375,600,0.10)
        self.createPlanet("../images/Planet1.png",100,100,1350,150,-0.7)
        self.planetes[1].addPrince(self.prince)
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
        counter,text=10,"10".rjust(3)
        pygame.time.set_timer(pygame.USEREVENT,1000)
        font=pygame.font.SysFont("Consolas",30)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    done=True
            if event.type == pygame.USEREVENT:
                counter-=1
                text=str(counter).rjust(3) if counter > 0 else 'boom!'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.prince.princeAnglePlanet += 6
                    print("left pressed")
                elif event.key == pygame.K_RIGHT:
                    print("right pressed")
                    self.prince.princeAnglePlanet -= 6
            self.update_flight(self.prince)
            self.update_planet()
            self.updateTimer()
            self.display()
            self.vueScreen.window.blit(font.render(text,True,(0,0,0)),(32,48))
            pygame.display.update()
            self.vueScreen.clock.tick(60)

    def update_flight(self,prince):
        if prince.isFlying:
            prince.princeAngle=Vector2(0,0).angle_to(prince.speedVector)
            prince.imgPrince=pygame.transform.rotozoom(prince.imgPrinceCopie,prince.princeAngle,1)
            self.PrinceFlight(self.prince)

    def update_planet(self):
        for planet in self.planetes:
            planet.volcano.chauffe()
            planet.rotationAngle += planet.rotationSpeed
            planet.imgPlanet=pygame.transform.rotozoom(planet.imgPlaneteCopie,planet.rotationAngle,1)
            planet.volcano.imgVolcano=pygame.transform.rotozoom(planet.volcano.imgVolcanCopie,planet.rotationAngle,1)
            planet.planetCenter = planet.imgPlanet.get_rect(center=planet.rectplanet.center)
            planet.volcano.rectVolcano = planet.volcano.imgVolcano.get_rect(center=(planet.positionx+math.cos(math.radians(-planet.rotationAngle))*planet.width/1.8,planet.positiony+math.sin(math.radians(-planet.rotationAngle))*planet.width/1.8))
            planet.volcano.volcanoCenter = planet.volcano.imgVolcano.get_rect(center=planet.volcano.rectVolcano.center)
            if planet.prince!=None:
                planet.prince.princeAngle = planet.rotationAngle -90 +self.prince.princeAnglePlanet
                self.prince.imgPrince=pygame.transform.rotozoom(self.prince.imgPrinceCopie,self.prince.princeAngle,1)
                self.prince.rectPrince = self.prince.imgPrince.get_rect(center=(planet.positionx+math.cos(math.radians(-planet.rotationAngle-self.prince.princeAnglePlanet))*planet.width/1.8,planet.positiony+math.sin(math.radians(-planet.rotationAngle-self.prince.princeAnglePlanet))*planet.width/1.8))
                self.prince.princeCenter = self.prince.imgPrince.get_rect(center=self.prince.rectPrince.center)
