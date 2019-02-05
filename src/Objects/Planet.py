
import pygame

class Planet:

    def __init__(self,imgPath,size,centerPositionx,centerPositiony,rotationAngle):
        self.imgPath=imgPath
        self.size=size
        self.imgPlanet=pygame.image.load(self.imgPath)
        self.rotationAngle=rotationAngle
        self.withPrince=False
        self.volcano=Volcano("../../../images/volcan.png",centerPositionx,centerPositiony)
        self.gravityForce = 100

        #change la taille de l'image
        self.imgPlanet=pygame.transform.scale(self.imgPlanet,self.size)
        self.volcano.imgVolcano=pygame.transform.scale(self.volcano.imgVolcano,(250,250))

        self.volcano.imgVolcano=pygame.transform.rotate(self.volcano.imgVolcano,-85)





    def addPrince():


        self.withPrince=True


    def removePrince():


        self.withPrince=False
