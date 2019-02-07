from pygame.math import Vector2
from Objects.Volcano import *
from Objects.PhysicObject import *
from Objects.Planet import *
import math

class Volcano(PhysicObject):

    def __init__(self, imgPath, position, size, parent):
        super().__init__(position, parent, imgPath, size)
        self.parent=parent
        self.eruptionCycle = 0

    def clean(self):
        self.eruptionCycle=1

    def chauffe(self):
        self.eruptionCycle+=1
        f=128
        i=1
        if self.eruptionCycle < 360:
            self.loadImage("../images/volcan0.png")
            i=f/2
        elif self.eruptionCycle < 650:
            self.loadImage("../images/volcan1.png")
            i=f/4
        elif self.eruptionCycle < 1000:
            self.loadImage("../images/volcan2.png")
            i=f/8
        else:
            self.eruption()
            self.clean()
        if self.eruptionCycle%(2*i)<i:
            self.img = pygame.transform.scale(self.img, (int(self.size[0]+self.eruptionCycle%i*f/i), int(self.size[1]+self.eruptionCycle%i*f/i)))
        else:
            self.img = pygame.transform.scale(self.img, (int(self.size[0]+f-self.eruptionCycle%i*f/i), int(self.size[1]+f-self.eruptionCycle%i*f/i)))

    def eruption(self):
        self.parent.removeFlower()
