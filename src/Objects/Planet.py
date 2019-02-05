
import pygame

class Planet:

    def __init__(self,imgPath,size,centerPositionx,centerPositiony,rotationAngle):
        self.imgPath=imgPath
        self.size=size
        self.imgPlanet=pygame.image.load(self.imgPath)
        self.rotationAngle=rotationAngle
        self.imgVolcan=None
        self.volcanoCenter=None
        #change la taille de l'image
        self.imgPlanet=pygame.transform.scale(self.imgPlanet,self.size)

        imgPlaneteCopie=self.imgPlanet.copy()

        rectplanet = self.imgPlanet.get_rect(center=(centerPositionx,centerPositiony))

        angle = 0

        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    done=True
            angle += self.rotationAngle
            self.imgPlanet=pygame.transform.rotozoom(imgPlaneteCopie,angle,1)
            planetCenter = self.imgPlanet.get_rect(center=rectplanet.center)

    def addVolcanoOnPlanet(imgPath,imgPlanet):
        self.imgVolcan=pygame.image.load(imgPath)
        self.imgVolcan=pygame.transform.rotate(self.imgVolcan,-85)

        #change la taille de l'image
        self.imgVolcan=pygame.transform.scale(self.imgVolcan,(250,250))

        imgVolcanCopie=self.imgVolcan.copy()

        angle = 0
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    done=True
            angle += self.rotationAngle
            self.imgVolcan=pygame.transform.rotozoom(imgVolcanCopie,angle,1)
            rectVolcano = self.imgVolcan.get_rect(center=(self.centerPositionx+math.cos(math.radians(-angle))*200,self.centerPositiony+math.sin(math.radians(-angle))*200))
            self.volcanoCenter = self.imgVolcan.get_rect(center=rectVolcano.center)
