from robot2I013 import *
from Strategie import * 
import time
from PIL import Image
from ntrait import *
COMPTEUR_ARRET = 60

""" 
            Boucle principale du robot. Elle appelle controler.update() fps fois par seconde 
            et s'arrete quand controler.stop() rend vrai.

            :verbose: booleen pour afficher les messages de debuggages
"""
class Simulation:
   def __init__(self, robot, fps=25, v_l=50):
       self.robot = robot
       self.strategie = Strategie(robot,v_l)
       self.fps=25
       #v_l est la vitesse limite de rotation des moteurs
       self.v_l = v_l
       self.tps = 0
       

   def lancement(self, vitesse, distance):
       #la distance et la vitesses sont a donner en cm
       distance = distance / 0.3
       vitesse  = vitesse / 0.3

       self.strategie.lancement(vitesse,distance)
       while not self.strategie.stop():
           time.sleep(1./self.fps)
       self.robot.stop()
   def lancement_sp(self, vitesse, distance):
       #la distance et la vitesses sont a donner en cm
       distance = distance / 0.3
       vitesse  = vitesse / 0.3

       self.strategie.lancement(vitesse,distance)

   def tourner_droite2(self, degres):

       degres = self.conversion_en_degres(degres)

       self.robot.set_motor_limits(self.robot.MOTOR_RIGHT, self.v_l)
       self.robot.set_motor_limits(self.robot.MOTOR_LEFT, self.v_l)
       gauche , droite = self.robot.get_motor_position()
       print("droite = ",droite,"gauche = ",gauche)
       self.robot.set_motor_position(self.robot.MOTOR_LEFT, (degres+gauche)/2)
       self.robot.set_motor_position(self.robot.MOTOR_RIGHT, (degres+droite)/2*-1)
       time.sleep(degres/self.v_l)

   def tourner_gauche2(self, degres):

       degres = self.conversion_en_degres(degres)

       self.robot.set_motor_limits(self.robot.MOTOR_RIGHT, self.v_l)
       self.robot.set_motor_limits(self.robot.MOTOR_LEFT, self.v_l)
       gauche , droite = self.robot.get_motor_position()
       self.robot.set_motor_position(self.robot.MOTOR_LEFT, degres/2*-1+gauche)
       self.robot.set_motor_position(self.robot.MOTOR_RIGHT, degres/2+droite)
       time.sleep(degres/self.v_l)
   def carre(self):

       self.lancement(90,50)
       self.tourner_gauche2(90)
       self.lancement(90,50)
       self.tourner_gauche2(90)

       self.lancement(90,50)
       self.tourner_gauche2(90)
       self.lancement(90,50)
       self.tourner_gauche2(90)

   def conversion_en_degres(self, nombre):
       #conversion en degres 90 degres = 400
       degres = nombre * (40/9)
       return nombre

   def afficher_image(self):
       
       self.robot.get_image().show()
   
   def save_img(self, file_name):
       img = self.robot.get_image()
       img.save(file_name)

       print(img.getpixel((1,5)))
 
   def trouver_balise(self):
       
       ratio_centre = 0.20
       x , y = Analyse(self.robot.get_image(),TAILLE).calcul(PARASITE)

       if(x<0):
           if(self.tps==0):
             self.tps = time.time()
           elif(self.tps<time.time()-COMPTEUR_ARRET):
             return False

           lancement_sp(0,0)
           return True

       self.tps = 0
       width , height = robot.get_image().size
       difference = x - width/2

       if(difference<(width*ratio_centre*-1)):
           self.tourner_droite2(45)

       elif(difference>(width*ratio_centre)):
           self.tourner_gauche2(45)
        
       else:
           self.lancement_sp(5,20)

       return True
    
   def suivre_balise(self):
       #On continue de suivre la balise, jusqu'au moment où il se passe un temps
       #de durée COMPTEUR_ARRET.

       while(cpt):
         cpt=trouver_balise(self)
       
       
       

"""
simulation = Simulation(Robot2I013())
#simulation.lancement(30,60)
start = time.time()
while(time.time()<start+30):
  simulation.trouver_balise()

#simulation.carre()"""
