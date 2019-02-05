import pygame

class Volcano:

    def __init__(self,imgPath,positionX,positionY):
        self.imgVolcano=pygame.image.load(imgPath)
        self.isCleaned=True
        self.rectVolcano = self.volcano.imgVolcano.get_rect(center=(self.positionX+math.cos(math.radians(-angle))*200,self.positionY+math.sin(math.radians(-angle))*200))
        self.volcanoCenter = self.volcano.imgVolcano.get_rect(center=self.volcano.rectVolcano.center)
