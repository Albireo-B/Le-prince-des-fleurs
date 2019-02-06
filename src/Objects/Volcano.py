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


    def clean(self):
        self.eruptionCycle=0

    def chauffe(self):
<<<<<<< HEAD
        self.cycle+=1
        #print(self.compteur)
        #lwidth = self.width+inflate[0]
        #lheight = self.height+inflate[1]
        f=128
        if self.cycle < 360:
            image = self.p1
            i=f/2
        elif self.cycle < 650:
=======
        self.eruptionCycle+=1
        if self.eruptionCycle < 360:
            image = self.p1
        elif self.eruptionCycle < 490:
>>>>>>> a56b50a03b93d81d5be1c1d05aebc24cf197abe5
            image = self.p2
            i=f/4
        else:
            image=self.p3
<<<<<<< HEAD
            i=f/8
        print(self.cycle%(2*i))
        if self.cycle%(2*i)<i:
            self.imgVolcano = pygame.transform.scale(self.base.subsurface(image), (int(self.width+f/i), int(self.height+f/i)))
            self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)
        else:
            self.imgVolcano = pygame.transform.scale(self.base.subsurface(image), (int(self.width-f/i), int(self.height-f/i)))
            self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)

=======
        self.imgVolcano = pygame.transform.scale(self.base.subsurface(image), (self.width+self.eruptionCycle%10, self.height+self.eruptionCycle%10))
        self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)
>>>>>>> a56b50a03b93d81d5be1c1d05aebc24cf197abe5
        self.imgVolcanCopie=self.imgVolcano.copy()
