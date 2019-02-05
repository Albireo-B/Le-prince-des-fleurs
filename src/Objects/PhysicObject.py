
class PhysicObject(Object):
    def __init__(self, collisionShape, position, parent, path):
        super().__init__(position, parent, path)
        self.collisionShape = collisionShape
