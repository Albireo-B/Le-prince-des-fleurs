
class Object:
    def __init__(self):
        self.position = (0,0)
        self.parent = None

    def __init__(self, position):
        self.position = position
        self.parent = None

    def __init__(self, position, parent):
        self.position = position
        self.parent = parent
