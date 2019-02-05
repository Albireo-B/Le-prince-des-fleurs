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
        #lwidth = volcano.width+inflate[0]
        #lheight = volcano.height+inflate[1]
        if self.cycle < 360:
            image = self.p1
        elif self.cycle < 490:
            image = self.p2
        else:
            image=self.p3
        self.imgVolcano = pygame.transform.scale(self.base.subsurface(image), (self.width+self.cycle%10, self.height+self.cycle%10))
        self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)
        self.imgVolcanCopie=self.imgVolcano.copy()
        #inflate[0]++
        #inflate[1]++
