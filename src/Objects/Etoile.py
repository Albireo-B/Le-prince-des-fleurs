
import pygame
from pygame.math import Vector2
from Objects.PhysicObject import *

class Etoile(PhysicObject):

    def __init__(self,imgPath,positionx, positiony,rotationAngle):
        super().__init__(Vector2(positionx, positiony), None, imgPath, (50,50))
        self.rotationSpeed = rotationAngle
        self.isHere=True

        def removeEtoile():
            self.isHere=False
            #Recréer l'étoile mais a une position différente
