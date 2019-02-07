from pygame.math import Vector2
from Objects.Volcano import *
from Objects.PhysicObject import *
from Objects.Planet import *
import math

class Volcano(PhysicObject):

    def __init__(self, imgPath, position, size, parent, eruptionCycle):
        super().__init__(position, parent, imgPath, (int(size[0]*.7), int(size[1]*.7)))
        self.parent=parent
        self.i=1
        self.f=128
        self.eruptionCycle=eruptionCycle

    def clean(self):
        self.eruptionCycle=0

    def chauffe(self):
        self.eruptionCycle+=1
        self.f=128
        self.i=1
        if self.eruptionCycle == 1:
            self.parent.flower.loadImage("../images/rose.png")
            self.loadImage("../images/volcan0.png")
            self.i=self.f/2
        elif self.eruptionCycle == 360:
            self.loadImage("../images/volcan1.png")
            self.i=self.f/4
        elif self.eruptionCycle == 650:
            self.loadImage("../images/volcan2.png")
            self.i=self.f/8
        elif self.eruptionCycle == 900:
            self.loadImage("../images/volcan2Eruption.png")
            self.parent.flower.loadImage("../images/roseBrulee.png")
            self.i=self.f/8
        elif self.eruptionCycle == 1000:
            self.eruption()


    def eruption(self):
        self.parent.removeFlower()
        self.clean()
