import time
import math
from robot2I013 import *

class Strategie:

     def  __init__(self, robot, v_l):
          self.cpt = 0
          self.tps = 0
          self.robot = robot
          self.vitesse(0)
          self.v_l = v_l

     def lancement(self, vitesse , distance):
          self.avancer(vitesse,distance)

     def avancer(self, vitesse, distance):
     
         self.vitesse(vitesse)
         self.cpt = time.time()
         self.tps = distance/((vitesse/360.0)*self.robot.WHEEL_DIAMETER)
         self.set_led((255,255,255))

     def vitesse(self, vitesse):
         
         self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT,vitesse )

     def set_led(self, col):
         self.robot.set_led(self.robot.LED_LEFT_EYE+self.robot.LED_RIGHT_EYE,*col)
       
     def stop(self):

         if(time.time()-self.cpt>=self.tps):
             self.vitesse(0)
             self.tps = 0
             self.cpt = 0
             self.set_led((0,0,0))
             return True

         #On ralenti le robot a la vitesse limite v_l
         #une fois arrivé a 80% de l'objectif

         elif(time.time()-self.cpt>=(self.tps-(self.tps/5))):
             self.vitesse(self.v_l)
         
         return False
