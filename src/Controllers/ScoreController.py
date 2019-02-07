import pygame

class ScoreController:

    def __init__(self, score,screen):
        self.background = pygame.image.load('../images/Planet4.png').convert_alpha()
        i=420
        self.background = pygame.transform.scale(self.background, (600+i,592+i))
        screen.blit(self.background, (0,-140))
        self.myFont = pygame.font.SysFont('arial',40)
        self.screen = screen
        self.score = score
        fichier = open("save.txt", "r")
        self.save=fichier.read().split("\n")
        self.save.pop()
        fichier.close()
        self.showScore()
        if self.score!=None:
            self.checkScore()
        back   = self.myFont.render("Retour",True,[135,206,235])
        button_rect_back=back.get_rect(topleft=(50,700))
        self.screen.blit(back,(10,700))
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_back.collidepoint(event.pos):#event to be changed
                        return

    def showScore(self):
        print(self.save)
        for i in range(0,20,2):
            self.screen.blit(self.myFont.render(str(self.save[i]), True, [255,255,255]),[340, 192+20*i])
            self.screen.blit(self.myFont.render(str(self.save[i+1]), True, [255,255,255]), [680, 192+20*i])
        pygame.display.update()

    def checkScore(self):
        print("Votre score : " + str(self.score))
        i=1
        while i<len(self.save):
            if int(self.save[i])< self.score:
                break
            i+=2
        if i < 20:
            self.addScore(int((i-1)/2)+1)



    def addScore(self, pos):
        print("Vous êtes à la place " + str(pos))
        print("saisissez votre nom")
        nom = "patate"
        for i in range(len(self.save)-1,pos*2-2,-2):
            if i == len(self.save)-1:
                if i < 18:
                    self.save.append(self.save[i-1])
                    self.save.append(self.save[i])
            else:
                self.save[i+1]=self.save[i-1]
                self.save[i+2]=self.save[i]
        self.save[pos*2-1] = self.score
        self.save[pos*2-2] = nom
        with open('save.txt', 'w') as f:
            for item in self.save:
                f.write("%s\n" % item)
        self.showScore()
