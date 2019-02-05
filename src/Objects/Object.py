
class Object:
    def __init__(self, path):
        self.position = (0,0)
        self.parent = None
        self.imgPath = path

    def __init__(self, position, path):
        self.position = position
        self.parent = None
        self.imgPath = path

    def __init__(self, position, parent, path):
        self.position = position
        self.parent = parent
        self.imgPath = path
