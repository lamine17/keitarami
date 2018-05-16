

class Tete3D():
    def __init__(self,):
        self.Front=Front
        #Point avant du Cylindre qui représente la tete du robot
        self.Back=Back
        #Point arriére du Cylindre qui représente la tete du robot
        self.Largeur=20
        #Largeur du Cylindre qui représente la tete du robot
        self.Direction=0
        #Direction vers laquelle est tournée la tete du robot
        
    def tourner(self,angle):
        if(self.Direction+angle>Self.Direction+90):
            self.Direction+=90
        elif (self.Direction+angle<Self.Direction-90):
            self.Direction-=90
        else:
            self.Direction+=angle
            
    def shoot(self):
        pass
        #déplace la caméra a la place de la tete et prend une screenshot
        
    
        
