
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from gl_lib.sim.robot.Robot3D import *
from gl_lib.sim.geometrie.Arene3D import *
from gl_lib.sim.geometrie.Pave import *
from gl_lib.sim.geometrie.point import *
from gl_lib.sim.geometrie.point.Vecteur import *
from gl_lib.sim.geometrie.Polygone3D import *


ground_vertices = (
    (150,-1,150),
    (150,-1,-150),
    (-150,-1,-150),
    (-150,-1,150),
    )

d=0
cpt=0
a=0

def DrawArene(Arene):
    DrawGround()
    for o in Arene.Objets3D:
        DrawCube(o)
    DrawRobot(Arene.Robot)


def DrawCube(pave):
    for i in range (0,4):
        pave.sommets[i].z=pave.hauteur
    for i in range (4,8):
        pave.sommets[i].z=0
    DrawPave(pave,(1,0,1))

def DrawPave(pave,color):
    vertices=list()
    edges=list()
    for s in pave.sommets:
        vertices.append((s.x,s.y,s.z))
        #vetices contient les coordonnées de chaque point du pavé rangés
        
    edges=((0,1),(0,3),(0,4),(1,2),(1,5),(2,3),(2,6),(7,3),(7,4),(7,6),(5,4),(5,6))
    #les segments qui délimitent le pavé
    surfaces=((0,1,2,3),(4,5,6,7),(0,1,4,5),(1,2,5,6),(2,3,6,7),(3,0,7,4))
    #les surfaces (réctangles) qui constituient le pavé

    glBegin(GL_QUADS)
    for surface in surfaces: 
        x = 0
        for vertex in surface:
            glColor3fv(color) #désigne la couleur du déssin
            glVertex3fv(vertices[vertex])#dessine le récltangle
            x+=1
    glEnd()

def DrawWheel():
    pass

def DrawGround():
    glBegin(GL_QUADS)
    x = 0
    for vertex in ground_vertices:
        x+=1
        glColor3fv((0,1,1))
        glVertex3fv(vertex)  
    glEnd()

def DrawRobot(Robot3D):
    DrawPave(Robot3D.Corps,(0,0,1))
    DrawPave(Robot3D.Face,Robot3D.FaceColor)
    
def FirstPerson(robot):
    glTranslatef(-3,-10,-5)
    glRotatef(robot.Direction, 0, 0,0)
    
def ThirdPerson(robot):
    #glTranslatef(0,-10,-30)
    #glRotatef(robot.Direction+90, 0, 15,0)
    gluLookAt(robot.Face.centre.x-30,15,robot.Face.centre.z,robot.Face.centre.x,1,robot.Face.centre.z,robot.Face.centre.x,1,robot.Face.centre.z)
    #-sin(radians(robot.Direction))+cos(radians(robot.Direction))
    print("x=",robot.Face.centre.x," y=",robot.Face.centre.y," z=",robot.Face.centre.z)
def ScreenShot(filename):
    pass
        
