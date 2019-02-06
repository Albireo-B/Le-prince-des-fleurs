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
        elif self.eruptionCycle < 490:
            image = self.p2
        else:
            image=self.p3
        self.img = pygame.transform.scale(self.imgCopie.subsurface(image), (self.size[0]+self.eruptionCycle%10, self.size[1]+self.eruptionCycle%10))
        self.img = pygame.transform.rotate(self.img,-85)
