import sys
sys.path.append("./GurrenLagann")

from gl_lib.sim.affichage.d2.interface import AppRobotAutonome
from gl_lib.sim.geometrie.point import *
from gl_lib.sim.robot import *
from gl_lib.sim.geometrie import *
from gl_lib.sim.affichage.d2.vue import *
from gl_lib.sim.robot.capteur import *

"""
Creation et affichage d'un robot basique avec modulateurs de vitesses pour tester
"""

class lancementSimulation:

  def __init__(self, robot = None):
    if(robot == None):
      self.robot = RobotAutonome(Pave(50,50,0),Objet3D(),Objet3D(), Vecteur(0,-1,0))
      self.robot.deplacer(Vecteur(200,100,0))
      self.arene = Arene(width=700 , height=700)
      self.arene.add(self.robot)
    else: 
      self.robot = robot
      self.arene = Arene(width=700 , height=700)
      self.arene.add(self.robot)

    self.app=AppRobotAutonome( self.robot , Vue2DArene(self.arene))
    self.app.init()
 
  def lancer(self):
    self.app.mainloop()

  def avancer(self, distance):
    self.app.avancer(distance)

  def tourner(self, angle):
    self.app.tourner(angle)
    
