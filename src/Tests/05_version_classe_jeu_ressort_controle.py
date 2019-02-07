###


class Ressort():

        # un ressort est defini a partir de deux objets et une elongation
        def __init__(self,a,b,k_elong):
                self.pt_a=a
                self.pt_b=b
                self.k=k_elong
                self.d0=a.distance(b)

	#retourne force exercee sur a
        def forceA(self):
                dis=self.pt_a.distance(self.pt_b)
                f=self.k*(self.d0-dis)
                ax=(self.pt_a.x-self.pt_b.x)*f/dis
                ay=(self.pt_a.y-self.pt_b.y)*f/dis
                return (ax,ay)

        #retourne force exercee sur B
        def forceB(self):
                return(-self.forceA)

        def longueur(self):
                return self.pt_a.distance(self.pt_b)


# un objet capable d'évoluer
class Objet():

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



        def accelerer(self,accX,accY):
                self.ax=accX
                self.ay=accY

        def evoluer(self):
                self.vx=self.vx+self.ax*self.dt
                self.vy=self.vy+self.ay*self.dt
                self.x=self.x+self.vx*self.dt
                self.y=self.y+self.vy*self.dt

                #met a jour trajectorie faite
                self.trajX+=[self.x]
                self.trajY+=[self.x]

        def afficher(self):
                print("(x,y): "+str(self.x)+","+str(self.y)+"  vx,vy: "+str(self.vx)+","+str(self.vy))

        #calcul distance en self et objet o
        def distance(self,O):
                dx=(O.x-self.x)
                dy=(O.y-self.y)
                d2=dx*dx+dy*dy
                from math import sqrt
                return sqrt(d2)



import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moteur")


done = False
mousedown=False

#creation des elements
balle=Objet(100,100)
point=Objet(200,200)
ressort=Ressort(balle,point,1)


sourisX=-1
sourisY=-1

mouse=False

# on creer une horloge pour réguler la vitesse de la boucle de jeu
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
                balle.x=pygame.mouse.get_pos()[0]
                balle.y=400-pygame.mouse.get_pos()[1]
                balle.vx=0
                balle.vy=0


        # --- on fait evoluer le jeu
        # calcule force balle
        f=ressort.forceA()
        g=(0,-9)
        ax=f[0]+g[0]
        ay=f[1]+g[1]


        balle.accelerer(ax,ay)
        balle.evoluer()

        # --- on dessine le jeu

        WHITE = (0xFF, 0xFF, 0xFF)
        RED = (0xFF, 0x00, 0x00)
        BLUE = (0x00, 0x00, 0xFF)
        GREEN = (0x00, 0xFF, 0x00)
        BLACK = (0x00, 0x00, 0xFF)

        screen.fill(WHITE)
        #ccordoonees ecran
        coordX=balle.x
        coordY=400-balle.y
        pygame.draw.ellipse(screen,RED,(coordX-5,coordY-5,10,10))

        coordX2=point.x
        coordY2=400-point.y
        pygame.draw.rect(screen,BLUE,(coordX2-5,coordY2-5,10,10))


        if (ressort.longueur()>ressort.d0):
                coul=RED
        else:
                if (ressort.longueur()<ressort.d0):
                        coul=GREEN
                else:
                        coul=BLACK

        pygame.draw.line(screen,coul,[coordX,coordY],[coordX2,coordY2],2)

        # on inverse les affichages (double buffering)
        pygame.display.flip()
        # --- on demande d'attendre ce qu'il faut pour un FPS de 60
        clock.tick(60)
# -------- Fin Boucle principale -----------


pygame.quit()
