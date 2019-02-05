import pygame
import math
import Planet

class Volcano:

    def __init__(self,imgPath,positionX,positionY):
        self.angle=0
        self.imgVolcano=pygame.image.load(imgPath)
        self.isCleaned=False
        self.timeToEruption=45
        self.rectVolcano = self.imgVolcano.get_rect(center=(positionX+math.cos(math.radians(-self.angle))*200,positionY+math.sin(math.radians(-self.angle))*200))
        self.volcanoCenter = self.imgVolcano.get_rect(center=self.rectVolcano.center)

    def cleaning(self):
        self.isCleaned=True
