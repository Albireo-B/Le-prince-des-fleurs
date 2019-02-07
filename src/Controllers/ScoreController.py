import pygame

class ScoreController:

    def __init__(self, score):
        self.score = score
        fichier = open("save.txt", "r")
        self.save=fichier.read().split("\n")
        self.save.pop()
        fichier.close()
        self.showScore()
        if self.score!=None:
            self.checkScore()

    def showScore(self):
        print(self.save)

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

        while i in range(10):
                screen.blit(myscores.render(str(self.score[i]+self.score[i+1]), True, [135,206,235]), [20, 20*i])
            i+=2

        pygame.display.update()
