
import pygame

from Volcano import *

class Planet:

    def __init__(self,imgPath,width,height,centerPositionx,centerPositiony,rotationAngle):
        self.imgPath=imgPath
        self.size=(width,height)
        self.imgPlanet=pygame.image.load(self.imgPath)
        self.rotationAngle=rotationAngle
        self.rectplanet = self.imgPlanet.get_rect(center=(centerPositionx,centerPositiony))
        self.planetCenter=self.imgPlanet.get_rect(center=self.rectplanet.center)
        self.withPrince=False
        self.volcano=Volcano("../../images/volcan.png",centerPositionx,centerPositiony)

        #change la taille de l'image
        self.imgPlanet=pygame.transform.scale(self.imgPlanet,self.size)
        self.volcano.imgVolcano=pygame.transform.scale(self.volcano.imgVolcano,(250,250))

        self.volcano.imgVolcano=pygame.transform.rotate(self.volcano.imgVolcano,-85)






    def addPrince(self):


        self.withPrince=True


    def removePrince(self):


        self.withPrince=False
