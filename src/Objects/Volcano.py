import pygame
import math
import Objects.Planet

class Volcano:

    def __init__(self,imgPath,positionX,positionY,width,height):
        self.angle=0
        self.cycle=0
        #self.inflate=(0,0)
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


    def cleaning(self):
        self.cycle=0

    def chauffe(self):
        self.cycle+=1
        #print(self.compteur)
        #lwidth = self.width+inflate[0]
        #lheight = self.height+inflate[1]
        f=128
        if self.cycle < 360:
            image = self.p1
            i=f/2
        elif self.cycle < 650:
            image = self.p2
            i=f/4
        else:
            image=self.p3
            i=f/8
        print(self.cycle%(2*i))
        if self.cycle%(2*i)<i:
            self.imgVolcano = pygame.transform.scale(self.base.subsurface(image), (int(self.width+f/i), int(self.height+f/i)))
            self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)
        else:
            self.imgVolcano = pygame.transform.scale(self.base.subsurface(image), (int(self.width-f/i), int(self.height-f/i)))
            self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)

        self.imgVolcanCopie=self.imgVolcano.copy()
        #inflate[0]++
        #inflate[1]++
