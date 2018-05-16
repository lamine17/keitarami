from gl_lib.sim.robot import *
from gl_lib.sim.geometrie.point import *
from gl_lib.sim.geometrie import *
from gl_lib.sim.robot.strategie.deplacement import *
from math import pi

a = Arene()
r = RobotAutonome(Pave(50,50,0), Objet3D(), Objet3D(), Vecteur(0,-1,0))
r.stratDeplacement=DeplacementSimple(r)
r.vitesse=2.0
r.vitesseRot=pi/100

a.add(r)

dest=Point(300, 300, 0)
print(dest.toVect().getAngle2D())
r.deplacerVers(dest)

while not r.destination is None:
    r.update()
    print(r.direction.getAngle2D())
    print(r)
    
    