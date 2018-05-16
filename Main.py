from GurrenLagann.lancementSimulation import lancementSimulation
from robot.lancementRobot import lancementRobot

#La classe Main synchronise les fonctions du robot reel et de la simulation

class Main:
   def __init__(self):
     self.lS = lancementSimulation()
     self.lR = lancementRobot()

   def lancer_simulation(self):
     self.lS.lancer()
   
   def avancer(self, distance): 
     self.lS.avancer(distance)
     self.lR.avancer(distance)

   def tourner(self, angle):
     self.lS.tourner(angle)
     self.lR.tourner(angle)
  
"""
Pour tester la simulation mettre sus commentaire les commandes liées au robot
et mettre sous la classe la commande.
Main().lancer_simulation()
"""
