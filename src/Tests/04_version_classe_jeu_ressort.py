## README : moteur de jeu avec ressort
##
## la classe ressort permet de representer un ressort entre deux objets
## la classe objet permet de reprÃ©senter un objet et ses grandeurs physiques
##
## la classe jeu represente un jeu simple
##      - avec une attache fixe
##      - une balle
##      - un ressort

"""
# classe qui represente un ressort
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
	#retourne force exercee sur a
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
# un objet capable d'evoluer
"""
class Objet():

    """
    # initialise l'objet en dx, dy
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
    # modifie l'acceleration de l'objet
    """
    def accelerer(self,accX,accY):
        self.ax=accX
        self.ay=accY

    """
    # fait evoluer les grandeurs physiques de l'objet
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
    # affichage textule de l'objet
    """
    def afficher(self):
        print("(x,y): "+str(self.x)+","+str(self.y)+"  vx,vy: "+str(self.vx)+","+str(self.vy))

    """
    #calcul distance en self et objet o
    """
    def distance(self,O):
        dx=(O.x-self.x)
        dy=(O.y-self.y)
        d2=dx*dx+dy*dy
        from math import sqrt
        return sqrt(d2)

"""
# la classe jeu represente ce jeu
"""
class Jeu():

    """
    # initialisation des elements de jeu
    """
    def __init__(self):
        #creation des elements
        self.balle=Objet(100,100)
        self.point=Objet(200,200)
        self.ressort=Ressort(self.balle,self.point,10)

    """
    #evolution du jeu (force gravite et le ressort)
    """
    def evoluer(self):
        # calcule force balle
        f=self.ressort.forceA()
        g=(0,-9)
        ax=f[0]+g[0]
        ay=f[1]+g[1]
        print(ax,ay)
        self.balle.accelerer(ax,ay)
        self.balle.evoluer()

    """
    #dessiner le jeu
    """
    def dessiner(self):
        WHITE = (0xFF, 0xFF, 0xFF)
        RED = (0xFF, 0x00, 0x00)
        BLUE = (0x00, 0x00, 0xFF)
        BLACK = (0x00, 0x00, 0xFF)

        #reinitialise l'ecran
        screen.fill(WHITE)

        #affichage des objets
        coord=self.changerCoordonnes(self.balle.x,self.balle.y)
        pygame.draw.ellipse(screen,RED,(coord[0]-5,coord[1]-5,10,10))
        coord2=self.changerCoordonnes(self.point.x,self.point.y)
        pygame.draw.rect(screen,BLUE,(coord2[0]-5,coord2[1]-5,10,10))

        #dessin ressort
        pygame.draw.line(screen,BLACK,coord,coord2,2)

        #dessin vitesse entre pos_balle et pos_balle+vitesse
        xvitesse=self.balle.x+self.balle.vx
        yvitesse=self.balle.y+self.balle.vy
        coordV=self.changerCoordonnes(xvitesse,yvitesse)
        pygame.draw.line(screen,BLACK,coord,coordV,1)

        # on inverse les affichages (double buffering)
        pygame.display.flip()


    """
    # permet de changer de repere pour l'affichage
    """
    def changerCoordonnes(self,dx,dy):
        nx = dx
        ny= 400-dy
        return( (nx,ny))



##############
# jeu
##############

# creation du jeu
jeu=Jeu()

# pygame
import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moteur")
done = False

# on creer une horloge pour rÃ©guler la vitesse de la boucle de jeu
clock = pygame.time.Clock()

# -------- Boucle principale -----------
# tant que le jeu n'est pas fini
while not done:

    # --- on traite les evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- on fait evoluer le jeu
    jeu.evoluer()

    # --- on dessine le jeu
    jeu.dessiner()

    # --- on demande d'attendre ce qu'il faut pour un FPS de 60
    clock.tick(60)
# -------- Fin Boucle principale -----------


pygame.quit()
