from CollisionShape import *

class PhysicEngine:

    def __init__(self):
        self.planetes=[]

    def updatePhysics(self,prince):
        if prince.parent == None:
            PrinceFlight(prince)


    def areColliding(self, obj1, obj2):
        pass

    def PrinceFlight(self, prince):
        for planet in self.planetes:
            distance = prince.position.distanceTo(planet.position)
            acceleration = planet.gravityForce/(distance*distance)
            normaVect = (planet.position - prince.position).normalize()
            temps = 1
            prince.speedVector += normaVect * acceleration * temps
        prince.position += prince.speedVector

    def addPlanet(self,Planet):
        self.planetes.append(Planet)
