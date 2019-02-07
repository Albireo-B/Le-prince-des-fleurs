
import pygame
from pygame.math import Vector2
from Objects.PhysicObject import *

RESPAWN_THRESHOLD = 50
class Etoile(PhysicObject):

    def __init__(self,imgPath,positionx, positiony,rotationAngle):
        super().__init__(Vector2(positionx, positiony), None, imgPath, (50,50))
        self.respawnCptr = RESPAWN_THRESHOLD
        self.rotationSpeed = rotationAngle
        self.isHere=True

    def updateRespawnCptr(self):
        self.respawnCptr += 1
        if self.respawnCptr >= RESPAWN_THRESHOLD:
            self.isHere = True

    def removeEtoile(self):
        self.isHere=False
        self.respawnCptr = 0
        #Recréer l'étoile mais a une position différente
