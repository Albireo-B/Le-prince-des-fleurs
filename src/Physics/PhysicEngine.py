import pygame
from pygame.locals import *
import math
from Objects.Prince import *
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
            if obj.parent != None:
                obj.angleToParent += obj.rotationSpeed
                obj.imgCenter = obj.img.get_rect(
                    center=(obj.parent.position.x+math.cos(math.radians(-obj.angleToParent))*obj.distanceToParent*1.1,
                    obj.parent.position.y+math.sin(math.radians(-obj.angleToParent))*obj.distanceToParent*1.1)
                )
            elif isinstance(obj,Prince):
                obj.img=pygame.transform.rotozoom(obj.imgCopie,obj.rotationAngle,1)
                obj.imgCenter = obj.img.get_rect(center=obj.rect.center)

    def areColliding(self, obj1, obj2):
        pass

    def addPhysicObject(self,obj):
        self.physicObjects.append(obj)
