from gl_lib.sim.robot.capteur.Capteur import Capteur


class Camera(Capteur):
    """
    cree une classe Camera vide
    """
    def __init__(self, position, orientation):
        """n'ajoute rien a la defnition de la camera"""
        Capteur.__int__(position, orientation)
        pass
