import sys
sys.path.append("./GurrenLagann")
from OutilsSimulation import *


def SimulationAutonome():
    Robot=Robot3D(Point(0,0,0))
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(30, (display[0]/display[1]), 0.1, 50.0)
    ThirdPerson(Robot)
    while True:
        #glRotatef(1,1,0,0) #tourne le robot (angle,x,y,z)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)#efface se qui a sur la fênetre "profondément" ;) 
        #Cube()
        p1=Pave(3,3,3)
        p2=Pave(2,3,2)
        p3=Pave(2,2,5)
        p1.deplacer(Vecteur(15,1,5))
        p2.deplacer(Vecteur(30,1,-25))
        p3.deplacer(Vecteur(-20,1,20))
        DrawGround()
        DrawCube(p1)
        DrawCube(p2)
        DrawCube(p3)
        DrawRobot(Robot)#dessine et redessine
        pygame.display.flip()#met a jour l'affichage
        pygame.time.wait(10)#temps d'attente entre chaque mise a jour 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(5,0,0)
                    
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-5,0,0)
                    
                if event.key == pygame.K_UP:
                    glTranslatef(0,0,-5.0)
                    
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,0,5.0)
                    
                if event.key == pygame.K_SPACE:
                    pygame.image.save(display,"screenshot.jpeg")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glRotatef(5,0,5,0) 
                    
                if event.button == 5:
                    glRotatef(-5,0,5,0)
                    
SimulationAutonome()

