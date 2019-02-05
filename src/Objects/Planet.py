
import pygame

from Volcano import *

class Planet:

    def __init__(self,imgPath,width,height,centerPositionx,centerPositiony,rotationAngle):
        self.imgPath=imgPath
        self.positionx=centerPositionx
        self.positiony=centerPositiony
        self.width=width
        self.height=height
        self.size=(width,height)
        self.imgPlanet=pygame.image.load(self.imgPath).convert_alpha()
        self.rotationSpeed=rotationAngle
        self.rotationAngle=0
        self.withPrince=False
<<<<<<< HEAD
        self.gravityForce = 500
=======
        self.volcano=Volcano("../../images/volcan.png",centerPositionx,centerPositiony,width,height)
        self.gravityForce = 100
>>>>>>> e1172be0b7985d13682ac45d11e506a917f7f331

        #change la taille de l'image
        self.imgPlanet=pygame.transform.scale(self.imgPlanet,self.size)

        self.rectplanet = self.imgPlanet.get_rect(center=(centerPositionx,centerPositiony))
        self.planetCenter=self.imgPlanet.get_rect(center=self.rectplanet.center)

        self.volcano=Volcano("../../images/volcan.png",centerPositionx,centerPositiony,width,height)
        self.imgPlaneteCopie=self.imgPlanet.copy()




    def addPrince(self):


        self.withPrince=True


    def removePrince(self):


        self.withPrince=False
