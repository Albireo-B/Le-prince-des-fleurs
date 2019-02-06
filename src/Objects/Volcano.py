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
        print("AAAAAAAAAAAAH")
        self.eruptionCycle+=1
        if self.eruptionCycle < 360:
            image = self.p1
            i=self.f/2
        elif self.eruptionCycle < 650:
            image = self.p2
            i=self.f/4
        else:
            image=self.p3
            i=self.f/8
        if self.eruptionCycle%(2*i)<i:
            self.imgVolcano = pygame.transform.scale(self.base.subsurface(image), (int(self.width+self.eruptionCycle%i*self.f/i), int(self.height+self.eruptionCycle%i*self.f/i)))
            self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)
        else:
            self.imgVolcano = pygame.transform.scale(self.base.subsurface(image), (int(self.width+self.f-self.eruptionCycle%i*self.f/i), int(self.height+self.f-self.eruptionCycle%i*self.f/i)))
            self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)

        self.imgVolcanCopie=self.imgVolcano.copy()
