from gl_lib.sim.geometrie.Pave import *
from gl_lib.sim.geometrie.point import *
from gl_lib.sim.geometrie.point.Vecteur import *
from gl_lib.sim.geometrie.Polygone3D import *
from gl_lib.sim.geometrie.Objet3D import *
from gl_lib.sim.robot.Robot3D import *

class Arene3D():
    def __init__(self,width,length,objets3D,posRobot):
        if width > 0 :
            self.width=width
        else:
            self.width=800
        if length > 0:
            self.length=length
        else:
            self.length=800
        if objets3D==None:
            self.Objets3D=list()
        else:
            self.Objets3D=objets3D
        if posRobot==None:
            posRobot=Point(0,0,0)
        self.Robot=Robot3D(posRobot)
        
    def add(self, objet3D):
        if issubclass(type(objet3D), Objet3D):
            self.objets3D.append(objet3D)
    
    
