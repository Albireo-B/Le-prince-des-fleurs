
import pygame

from Objects.Volcano import *

class Planet:

    def __init__(self,imgPath,width,height,centerPositionx,centerPositiony,rotationAngle):
        self.imgPath=imgPath
        self.positionx=centerPositionx
        self.positiony=centerPositiony
        self.width=width
        self.height=height
        self.size=(width,height)
        self.imgPlanet=pygame.image.load(self.imgPath)
        self.rotationSpeed=rotationAngle
        self.rotationAngle=0
        self.prince=None
        self.volcano=Volcano("../images/volcan.png",centerPositionx,centerPositiony,width,height)
        self.gravityForce = 50*self.width

        #change la taille de l'image
        self.imgPlanet=pygame.transform.scale(self.imgPlanet,self.size)

        self.rectplanet = self.imgPlanet.get_rect(center=(centerPositionx,centerPositiony))
        self.planetCenter=self.imgPlanet.get_rect(center=self.rectplanet.center)

        self.volcano=Volcano("../images/volcan.png",centerPositionx,centerPositiony,width,height)
        self.imgPlaneteCopie=self.imgPlanet.copy()




    def addPrince(self,prince):
        self.prince=prince
        self.prince.isFlying = False

    def removePrince(self):


        self.prince=None
        self.prince.isFlying = True
