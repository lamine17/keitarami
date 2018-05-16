from gl_lib.sim.geometrie.Objet3D import *
from gl_lib.sim.geometrie.point import Point, Vecteur
from gl_lib.sim.geometrie.Polygone3D import Polygone3D
from math import *


class Pave(Polygone3D):
    """
    Classe definissant un pave dans un repere en 3D
    """

    def __init__(self, longueur, hauteur, largeur,centre=None):
        """
        Constructeur ajoutant les 8 sommets autour du centre par defaut: (0,0,0)
        """
        
        Polygone3D.__init__(self,centre)
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        
        self.addSommet(Point(self.centre.x - longueur / 2, self.centre.y - largeur / 2, self.centre.z + hauteur / 2))
        self.addSommet(Point(self.centre.x + longueur / 2, self.centre.y - largeur / 2, self.centre.z + hauteur / 2))
        self.addSommet(Point(self.centre.x + longueur / 2, self.centre.y + largeur / 2, self.centre.z + hauteur / 2))
        self.addSommet(Point(self.centre.x - longueur / 2, self.centre.y + largeur / 2, self.centre.z + hauteur / 2))
        self.addSommet(Point(self.centre.x - longueur / 2, self.centre.y - largeur / 2, self.centre.z - hauteur / 2))
        self.addSommet(Point(self.centre.x + longueur / 2, self.centre.y - largeur / 2, self.centre.z - hauteur / 2))
        self.addSommet(Point(self.centre.x + longueur / 2, self.centre.y + largeur / 2, self.centre.z - hauteur / 2))
        self.addSommet(Point(self.centre.x - longueur / 2, self.centre.y + largeur / 2, self.centre.z - hauteur / 2))

    #a modifier
    def tournerPave(self,angle):
        for i in range (0,4):
            self.sommets[i].x=self.centre.x+cos(radians(angle))/100
            self.sommets[i].y=self.centre.y+sin(radians(angle))/100
        for i in range (4,8):
            self.sommets[i].x+=cos(radians(angle))/100
            self.sommets[i].y+=sin(radians(angle))/100  


    def tournerSelon(self, axe, teta):
        if axe=='z':
            self.tournerZ(self.centre,radians(teta))
        elif axe=='y':
            self.tournerY(radians(teta))
        elif axe=='x':
            self.tournerX(radians(teta))
        pass
    
    def tournerAutourSelon(self, point, axe, teta):
        if axe=='z':
            self.tournerAutour(point, teta)
        elif axe=='y':
            self.tournerAutourY(point, teta)
        elif axe=='x':
            self.tournerAutourX(point, teta)
    
    def tournerAutourX(self, point, teta):
        """
        tourne le pave autour de point selon x d'un angle teta
        """
        for i in range(0, len(self.sommets)):
            # v: Vecteur
            v = (self.sommets[i]-point).toVect() # vecteur point->s
            v.rotationX(teta)
            self.sommets[i] = point+v # apres rotation, on actualise les coords du sommet

        if point != self.centre:
            v = (self.centre-point).toVect() # meme chose pour le centre
            v.rotationX(teta)
            self.centre = point+v
            
    def tournerAutourY(self, point, teta):
        """
        tourne le pave autour de point selon y d'un angle teta
        """
        for i in range(0, len(self.sommets)):
            # v: Vecteur
            v = (self.sommets[i]-point).toVect() # vecteur point->s
            v.rotationY(teta)
            self.sommets[i] = point+v # apres rotation, on actualise les coords du sommet

        if point != self.centre:
            v = (self.centre-point).toVect() # meme chose pour le centre
            v.rotationY(teta)
            self.centre = point+v
    
    def tournerAutour(self, point, teta):
        """
        tourne le pave autour de point selon z d'un angle teta
        """
        for i in range(0, len(self.sommets)):
            # v: Vecteur
            v = (self.sommets[i]-point).toVect() # vecteur point->s
            v.rotation2D(teta)
            self.sommets[i] = point+v # apres rotation, on actualise les coords du sommet

        if point != self.centre:
            v = (self.centre-point).toVect() # meme chose pour le centre
            v.rotation2D(teta)
            self.centre = point+v

    def tournerZ(self, teta):
        self.tournerAutour(self.centre, teta)
        
    def tournerX(self, teta):
        self.tournerAutourX(self.centre, teta)
        
    def tournerY(self, teta):
        self.tournerAutourY(self.centre, teta)
