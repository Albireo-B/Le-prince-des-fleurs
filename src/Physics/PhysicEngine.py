import pygame
from pygame.locals import *
import math
from Objects.Prince import *
class PhysicEngine:

    def __init__(self):
        self.physicObjects=[]

    def updatePhysics(self):
        for obj in self.physicObjects:
            if obj.rotationSpeed != 0:
                obj.rotationAngle += obj.rotationSpeed
                obj.setRotation(obj.rotationAngle)
            if obj.parent != None:
                obj.angleToParent += obj.rotationSpeed
                obj.imgCenter = obj.img.get_rect(
                    center=(obj.parent.position.x+math.cos(math.radians(-obj.angleToParent))*obj.distanceToParent*1.1,
                    obj.parent.position.y+math.sin(math.radians(-obj.angleToParent))*obj.distanceToParent*1.1)
                )
                obj.position = Vector2(obj.parent.position.x+math.cos(math.radians(-obj.angleToParent))*obj.distanceToParent*1.1,
                    obj.parent.position.y+math.sin(math.radians(-obj.angleToParent))*obj.distanceToParent*1.1
                )
                obj.maskCenter = Vector2(obj.imgCenter[0], obj.imgCenter[1])

    def areColliding(self, obj1, obj2):
        pass

    def addPhysicObject(self,obj):
        self.physicObjects.append(obj)
