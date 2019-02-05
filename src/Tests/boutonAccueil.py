import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((1500,750))
pygame.display.set_caption('Le Prince Des Fleurs')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


white = (255,255,255)
black = (0,0,0)
skyblue = (135,206,235)
intro = True

while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro=False
        elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
            if event.button == 1: # 1= clique gauche
                if clickable_area.collidepoint(event.pos):
                    print("bouton bien cliqué")
                    intro=False

    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf',85)
    TextSurf, TextRect = text_objects("Le Prince Des Fleurs", largeText)
    TextRect.center = ((1500/2),(750/2))
    gameDisplay.blit(TextSurf, TextRect)
    clickable_area = pygame.Rect((1500/2-100, 750/2+200), (200, 100))
    rect_surf = pygame.Surface(clickable_area.size)
    rect_surf.fill(skyblue)
    text,text_rect = text_objects("Start",largeText)
    gameDisplay.blit(rect_surf, clickable_area)
    gameDisplay.blit(text,clickable_area)
    pygame.display.update()
    clock.tick(15)
pygame.quit()
quit()
