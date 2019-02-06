import pygame
import math
import Objects.Planet

class Volcano:

    def __init__(self,imgPath,positionX,positionY,width,height):
        self.angle=0
        self.eruptionCycle=0
        self.p1 = (160, 16, 750, 200)
        self.p2 = (160, 226, 750, 240)
        self.p3 = (160, 360, 750, 260)
        self.base=pygame.image.load(imgPath)
        self.width=width
        self.height=height
        self.imgVolcano = pygame.transform.scale(self.base.subsurface(self.p1), (self.width, self.height))
        self.rectVolcano = self.imgVolcano.get_rect(center=(positionX+math.cos(math.radians(-self.angle))*200,positionY+math.sin(math.radians(-self.angle))*200))
        self.volcanoCenter = self.imgVolcano.get_rect(center=self.rectVolcano.center)
        self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)
        self.imgVolcanCopie=self.imgVolcano.copy()
        self.f = 50

    def clean(self):
        self.eruptionCycle=0

    def chauffe(self):
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
