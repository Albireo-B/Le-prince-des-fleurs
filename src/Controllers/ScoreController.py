import pygame

class ScoreController:

    def __init__(self, score):
        self.score = score
        fichier = open("save.txt", "r")
        self.save=fichier.read().split("\n")
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
            self.addScore(i)



    def addScore(self, pos):
        print("Vous êtes à la place " + str(int((pos-1)/2)+1))
        print("saisissez votre nom")
