from gl_lib.sim.geometrie import Objet3D
from gl_lib.sim.geometrie.point import *

#Creation d'un carre de cote 1 et deplacement de celui-ci du vecteur v
v=Point(1,1,1)
o = Objet3D()


print(o)

#deplacement puis affichage
print("deplacement de {}".format(v))
o.deplacer(v)
print(o)

