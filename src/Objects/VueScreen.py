import pygame

pygame.init()

class VueScreen:
    def __init__(self,size):
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption('Le Prince Des Fleurs')
        self.clock = pygame.time.Clock()
