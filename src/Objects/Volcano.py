import pygame
import math
import Planet

class Volcano:

    def __init__(self,imgPath,positionX,positionY,width,height):
        self.angle=0
        self.imgVolcano=pygame.image.load(imgPath)
        self.isCleaned=False
        self.timeToEruption=45
        self.rectVolcano = self.imgVolcano.get_rect(center=(positionX+math.cos(math.radians(-self.angle))*200,positionY+math.sin(math.radians(-self.angle))*200))
        self.volcanoCenter = self.imgVolcano.get_rect(center=self.rectVolcano.center)
        self.imgVolcano=pygame.transform.scale(self.imgVolcano,(int(width/1.5),int(height/1.5)))
        self.imgVolcano=pygame.transform.rotate(self.imgVolcano,-85)
        self.imgVolcanCopie=self.imgVolcano.copy()

    def cleaning(self):
        self.isCleaned=True
