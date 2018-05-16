import math
from gl_lib.sim.geometrie import Objet3D
from gl_lib.sim.geometrie.point import Vecteur, Point
from gl_lib.sim.geometrie.Pave import *
from gl_lib.sim.geometrie.Polygone3D import *


class Robot3D():    
    def __init__(self,pos): #position,direction
        self.WBW=117.0/100
        self.WD= 66.5/100
        self.WBC=self.WBW*math.pi/100
        self.WC=self.WD*math.pi/100
        #self.Position=Point(Position.x,Position.y,self.WD/2)
        self.Position=Point(pos.x,pos.y,self.WD/2)
        self.Direction=0
        self.Corps=Pave(3*self.WBW,self.WBW,self.WD)
        self.Corps.deplacer(Vecteur(-self.WBW/2,self.Position.z+self.WD/2,0))
        #Pavé du corps du robot
        self.Face=Pave(self.WBW/2,self.WBW,self.WBW*1.5)  
        #self.Face.deplacer(Vecteur(0,self.WBW,self.Position.z+1.5*self.WBW))
        self.Face.deplacer(Vecteur(0.875*self.WBW,1.75*self.WD,0))
        #Pavé de la face du robot
        #P:Point R:Roue g:Gauche d:Droite

        self.PgRg=Point(self.Position.x+self.WBW/4,self.Position.y+self.WBW/2,self.Position.z)
        self.PdRg=Point(self.Position.x+self.WBW/4+5,self.Position.y+self.WBW/2,self.Position.z)
        self.PgRd=Point(self.Position.x-self.WBW/4,self.Position.y+self.WBW/2,self.Position.z)
        self.PdRd=Point(self.Position.x-self.WBW/4-5,self.Position.y+self.WBW/2,self.Position.z)
       
        self.FaceColor=(1,0,0)
        #self.Tete=Tete3D(None,None)
        #Tete du robot
        #self.Tete.Direction=self.Direction
        self.Vitesse=1000*self.WC/360 #100dps
        self.Arret=False
        #tourner le robot et lancer la fenetre avec le robot tourné

    
    def Deplacer(self,step):
        self.Corps.deplacer(Vecteur(step*cos(radians(self.Direction)),0,step*sin(radians(self.Direction))))    
        self.Face.deplacer(Vecteur(step*cos(radians(self.Direction)),0,step*sin(radians(self.Direction)))) 
                 
    def Tourner(self,teta):
        self.Corps.tournerSelon('y',teta)
        self.Face.tournerAutourY(self.Corps.centre,radians(teta))

    
    def Avancer(self,vitesse,distance):
        self.vitesse=vitesse 
        step=SA/10
        dist=0
        while(dist<distance):
            sleep(0.1)
            self.Deplacer(step)
            dist+=step  


    


        
