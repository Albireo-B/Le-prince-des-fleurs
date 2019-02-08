import pygame

class ScoreController:

    def __init__(self, score,screen):
        self.saisie=False
        self.screen = screen
        self.myFont = pygame.font.SysFont('arial',40)
        self.background=pygame.image.load("../images/background.jpg").convert()
        self.background=pygame.transform.scale(self.background,(1024,768))
        self.planet = pygame.image.load('../images/Planet4.png').convert_alpha()
        self.planet = pygame.transform.scale(self.planet, (1020,1020))
        self.back   = self.myFont.render("Retour",True,[135,206,235])
        self.button_rect_back=self.back.get_rect(topleft=(50,700))
        self.saveb   = self.myFont.render("Enregistrer",True,[135,206,235])
        self.button_rect_saveb=self.saveb.get_rect(topleft=(825,700))
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.back,[10,700])
        self.screen.blit(self.planet, (25,-50))
        self.score = score
        self.lastchar=''
        fichier = open("save.txt", "r")
        self.save=fichier.read().split("\n")
        self.save.pop()
        fichier.close()

        self.nom = None
        self.showScore()
        if self.score!=None:
            self.checkScore()

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if self.nom != None:
                        if self.lastchar!=event.unicode:
                            if event.key == pygame.K_BACKSPACE:
                                if len(self.nom)>0:
                                    self.nom= self.nom[0:len(self.nom)-1]

                            else:
                                if len(self.nom)<10:
                                    if event.unicode.isalpha() or event.unicode.isdigit():
                                        self.nom+= event.unicode
                            self.lastchar=event.unicode
                        self.screen.blit(self.background,(0,0))
                        self.screen.blit(self.back,[10,700])
                        self.screen.blit(self.planet, (25,-50))
                        self.screen.blit(self.myFont.render("Votre score : " + str(self.score), True, [255,255,255]),[340, 550])
                        self.screen.blit(self.myFont.render("Vous êtes à la place " + str(self.pos), True, [255,255,255]),[340, 590])
                        self.screen.blit(self.saveb,[825,700])
                        self.screen.blit(self.myFont.render(self.nom, True, [255,255,255]),[340, 670])
                        self.showScore()
                        pygame.display.update()
                else:
                    self.lastchar=''


                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if self.button_rect_back.collidepoint(event.pos):#event to be changed
                        return
                    if self.button_rect_saveb.collidepoint(event.pos):#event to be changed
                        if self.nom != None:
                            self.addscore()
                            self.nom = None
                            self.screen.blit(self.background,(0,0))
                            self.screen.blit(self.back,[10,700])
                            self.screen.blit(self.planet, (25,-50))
                            self.screen.blit(self.myFont.render("Votre score : " + str(self.score), True, [255,255,255]),[340, 550])
                            self.screen.blit(self.myFont.render("Vous êtes à la place " + str(self.pos), True, [255,255,255]),[340, 590])
                            self.showScore()

    def showScore(self):
        i=0
        while i <len(self.save):
            self.screen.blit(self.myFont.render(str(self.save[i]), True, [255,255,255]),[340, 150+20*i])
            self.screen.blit(self.myFont.render(str(self.save[i+1]), True, [255,255,255]), [680, 150+20*i])
            i+=2
        pygame.display.update()

    def checkScore(self):
        self.screen.blit(self.myFont.render("Votre score : " + str(self.score), True, [255,255,255]),[340, 550])
        pygame.display.update()
        i=1
        while i<len(self.save):
            if int(self.save[i])< self.score:
                break
            i+=2
        if i < 20:
            self.pos=int((i-1)/2)+1
            self.saisieNom()



    def saisieNom(self):
        self.screen.blit(self.myFont.render("Vous êtes à la place " + str(self.pos), True, [255,255,255]),[340, 590])
        self.screen.blit(self.myFont.render("saisissez votre nom :", True, [255,255,255]),[340, 630])
        self.screen.blit(self.saveb,[825,700])
        pygame.display.update()
        self.saisie=True
        self.nom = ""
        self.screen.blit(self.myFont.render(self.nom, True, [255,255,255]),[340, 670])
        pygame.display.update()



    def addscore(self):
        for i in range(len(self.save)-1,self.pos*2-2,-2):
            if i == len(self.save)-1:
                if i < 20:
                    self.save.append(self.save[i-1])
                    self.save.append(self.save[i])
            else:
                self.save[i+1]=self.save[i-1]
                self.save[i+2]=self.save[i]
        if self.pos*2-1 > len(self.save):
            self.save.append(self.nom)
            self.save.append(self.score)
        else:
            self.save[self.pos*2-1] = self.score
            self.save[self.pos*2-2] = self.nom
        with open('save.txt', 'w') as f:
            for item in self.save:
                f.write("%s\n" % item)
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.back,[10,700])
        self.screen.blit(self.planet, (25,-50))
        self.screen.blit(self.myFont.render("Votre score : " + str(self.score), True, [255,255,255]),[340, 550])
        self.screen.blit(self.myFont.render("Vous êtes à la place " + str(self.pos), True, [255,255,255]),[340, 590])
        self.showScore()
