import sys
sys.path.append("./robot")


from . import Simulation
VITESSE = 20

class Lancementrobot:

  def __init__(self, robot = None):
    if(robot == None):
      self.robot = Robot()
      self.simulation = Simulation(self.robot)
    else:
      self.robot = robot
      self.simulation = Simulation(self.robot)
    
   def avancer(self, distance):
      
     lancement(VITESSE, distance)
     
   def tourner(self, angle):

     #Si l'angle est negatif on tourne à gauche, a droite sinon

     if(anle>0):
       simulation.tourner_gauche2(angle)
     if(angle<0):
       simulation.tourner_droite2(angle*-1)
     
