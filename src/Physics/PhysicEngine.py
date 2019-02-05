from CollisionShape import *

class PhysicEngine:

    def __init__(self):
        self.planetes=[]

    def updatePhysics(self,prince):
        if prince.parent == None:
            PrinceFlight(prince)


    def areColliding(self, obj1, obj2):
        pass


    def addPlanet(self,Planet):
        self.planetes.append(Planet)
