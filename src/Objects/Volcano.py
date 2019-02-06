from pygame.math import Vector2
from Objects.Volcano import *
from Objects.PhysicObject import *
from Objects.Planet import *
import math

class Volcano(PhysicObject):

    def __init__(self, imgPath, position, size, parent):
        super().__init__(position, parent, imgPath, size)
        self.distanceToParent = parent.size[0]*.5
        self.eruptionCycle = 0
        self.rotationSpeed = parent.rotationSpeed
        self.imgCenter = self.img.get_rect(center=(self.position.x+math.cos(math.radians(-self.angleToParent))*200,self.position.y+math.sin(math.radians(-self.angleToParent))*200))
        self.imgCopie = pygame.transform.rotate(self.imgCopie,-85)

    def clean(self):
        self.eruptionCycle=0

    def chauffe(self):
        self.eruptionCycle+=1
        f=128
        if self.eruptionCycle < 360:
            image = pygame.image.load("../images/volcan0.png")
            i=f/2
        elif self.eruptionCycle < 650:
            image = pygame.image.load("../images/volcan1.png")
            i=f/4
        else:
            image = pygame.image.load("../images/volcan2.png")
            i=f/8
        if self.eruptionCycle%(2*i)<i:
            self.imgVolcano = pygame.transform.scale(image, (int(self.size[0]+self.eruptionCycle%i*f/i), int(self.size[1]+self.eruptionCycle%i*f/i)))
            print(self.imgVolcano)
            self.imgVolcano=pygame.transform.rotate(image,-85)
        else:
            self.imgVolcano = pygame.transform.scale(image, (int(self.size[0]+f-self.eruptionCycle%i*f/i), int(self.size[1]+f-self.eruptionCycle%i*f/i)))
            print(self.imgVolcano)
            self.imgVolcano=pygame.transform.rotate(image,-85)
        self.imgVolcanCopie=self.imgVolcano.copy()
