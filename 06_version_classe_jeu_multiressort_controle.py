"""
represente un ressort
"""
class Ressort():

        """
        # un ressort est defini a partir de deux objets et une elongation
        """
        def __init__(self,a,b,k_elong):
                self.pt_a=a
                self.pt_b=b
                self.k=k_elong
                self.d0=a.distance(b)

        """
        # retourne force exercee sur a
        """
        def forceA(self):
                dis=self.pt_a.distance(self.pt_b)
                f=self.k*(self.d0-dis)
                ax=(self.pt_a.x-self.pt_b.x)*f/dis
                ay=(self.pt_a.y-self.pt_b.y)*f/dis
                return (ax,ay)

        """
        # retourne force exercee sur B
        """
        def forceB(self):
                return(-self.forceA)

        """
        # calcule la longueur entre les objets
        """
        def longueur(self):
                return self.pt_a.distance(self.pt_b)

        """
        # permet de mettre a jour ecceleration des objets sur le ressorts
        """
        def metreAJourAcc(self):
                fa=self.forceA()
                #mise a jour force A
                self.pt_a.ax+=fa[0]
                self.pt_a.ay+=fa[1]
                #mise a jour force B
                self.pt_b.ax-=fa[0]
                self.pt_b.ay-=fa[1]


"""
# un objet capable d'evoluer
"""
class Objet():

        """
        # initialisation de l'objet
        """
        def __init__(self,dx,dy):
                self.x=dx
                self.y=dy
                self.vx=0
                self.vy=0
                self.ax=0
                self.ay=-9
                self.dt=0.1
                self.trajX=[self.x]
                self.trajY=[self.y]


        """
        # met a jour la valeur de l'acceleration
        """
        def accelerer(self,accX,accY):
                self.ax=accX
                self.ay=accY

        """
        # fait evoluer le systeme selon dynamique du point
        """
        def evoluer(self):
                self.vx=self.vx+self.ax*self.dt
                self.vy=self.vy+self.ay*self.dt
                self.x=self.x+self.vx*self.dt
                self.y=self.y+self.vy*self.dt

                #met a jour trajectorie faite
                self.trajX+=[self.x]
                self.trajY+=[self.x]

        """
        # affiche textuelle
        """
        def afficher(self):
                print("(x,y): "+str(self.x)+","+str(self.y)+"  vx,vy: "+str(self.vx)+","+str(self.vy))

        """
        # calcul distance en self et objet o
        """
        def distance(self,O):
                dx=(O.x-self.x)
                dy=(O.y-self.y)
                d2=dx*dx+dy*dy
                from math import sqrt
                return sqrt(d2)


"""
# un systeme constitue d'objets et de ressorts
"""
class Systeme():

        """
        # un systeme est constitue d'objets et des ressorts
        """
        def __init__(self):
                self.ressorts=[]
                self.objets=[]

        """
        # executer les forces sur les objets
        """
        def evoluer(self):
                # initialiser a a g
                for objet in self.objets:
                        objet.ax=0
                        objet.ay=-9

                # pour chaque ressort
                for ressort in self.ressorts:
                        ressort.metreAJourAcc()

                # mettre Ã  jour objet
                for objet in self.objets:
                        objet.evoluer()





# -------- creation du systeme
systeme=Systeme()

balle=Objet(100,100)
balle2=Objet(50,50)
point=Objet(200,200)

systeme.objets=[balle]
systeme.objets+=[balle2]

ressort=Ressort(balle,point,1)
ressort2=Ressort(balle,balle2,1)

systeme.ressorts+=[ressort]
systeme.ressorts+=[ressort2]


#---------- pygame

import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moteur")




#creation des elements
done = False
mousedown=False
mouse=False
sourisX=-1
sourisY=-1


# on creer une horloge pour rÃ©guler la vitesse de la boucle de jeu
clock = pygame.time.Clock()

# -------- Boucle principale -----------
# tant que le jeu n'est pas fini
while not done:
         # --- on traite les evenements
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                #s'il a appuye sur la souris
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse=True
                if event.type == pygame.MOUSEBUTTONUP:
                        mouse=False



        if (mouse):
                balle2.x=pygame.mouse.get_pos()[0]
                balle2.y=400-pygame.mouse.get_pos()[1]
                balle2.vx=0
                balle2.vy=0


        # --- on fait evoluer le jeu
        systeme.evoluer()

        # --- on dessine le jeu
        WHITE = (0xFF, 0xFF, 0xFF)
        RED = (0xFF, 0x00, 0x00)
        BLUE = (0x00, 0x00, 0xFF)
        GREEN = (0x00, 0xFF, 0x00)
        BLACK = (0x00, 0x00, 0xFF)

        screen.fill(WHITE)
        #coordoonees ecran balle
        coordX=balle.x
        coordY=400-balle.y
        pygame.draw.ellipse(screen,RED,(coordX-5,coordY-5,10,10))

        #coordoonees ecran balle2
        coordX2=balle2.x
        coordY2=400-balle2.y
        pygame.draw.ellipse(screen,RED,(coordX2-5,coordY2-5,10,10))

        #dessin ecran point
        coordX3=point.x
        coordY3=400-point.y
        pygame.draw.rect(screen,BLUE,(coordX3-5,coordY3-5,10,10))

        #dessin ecran ressort
        if (ressort.longueur()>ressort.d0):
                coul=RED
        else:
                if (ressort.longueur()<ressort.d0):
                        coul=GREEN
                else:
                        coul=BLACK
        pygame.draw.line(screen,coul,[coordX,coordY],[coordX3,coordY3],2)

        #dessin ecran ressort2
        coul=RED
        pygame.draw.line(screen,coul,[coordX,coordY],[coordX2,coordY2],2)

        # on inverse les affichages (double buffering)
        pygame.display.flip()
        # --- on demande d'attendre ce qu'il faut pour un FPS de 60
        clock.tick(60)
# -------- Fin Boucle principale -----------


pygame.quit()
