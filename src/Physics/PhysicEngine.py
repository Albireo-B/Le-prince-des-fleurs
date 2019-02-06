import pygame
from pygame.locals import *

class PhysicEngine:

    def __init__(self):
        self.physicObjects=[]

    def updatePhysics(self):
        #if prince.parent == None:
        #    PrinceFlight(prince)
        for obj in self.physicObjects:
            if obj.rotationSpeed != 0:
                obj.rotationAngle += obj.rotationSpeed
                obj.img=pygame.transform.rotozoom(obj.imgCopie,obj.rotationAngle,1)
                obj.imgCenter = obj.img.get_rect(center=obj.rect.center)

    def areColliding(self, obj1, obj2):
        pass

    def addPhysicObject(self,obj):
        self.physicObjects.append(obj)
