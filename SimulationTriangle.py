import sys
sys.path.append("./GurrenLagann")

from gl_lib.sim.affichage.d3.OutilsSimulation import *

def SimulationTriangle():
    Robot=Robot3D(Point(0,0,0))
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(30, (display[0]/display[1]), 3.0, 50.0)
    ThirdPerson(Robot)
    
    while True:
        #glRotatef(1,1,0,0) #tourne le robot (angle,x,y,z)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)#efface se qui a sur la fenetre "profondement" ;) 
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
        if(Robot.Arret==False):
            global cpt
            if cpt%2==0:
                Robot.Deplacer(Robot.Vitesse)
                #glTranslatef(Robot.Vitesse,0,0)
                glTranslatef(-Robot.Vitesse*cos(radians(Robot.Direction)),0,-Robot.Vitesse*sin(radians(Robot.Direction)))
                global d
                d=d+Robot.Vitesse
                if(d>=10):
                    d=0
                    cpt=cpt+1
            if cpt%2==1:
                Robot.Tourner(10)
                #ThirdPerson(Robot)
                #glRotatef(-10,0,0,0)
                global a
                a=a+10
                Robot.Direction-=10
                if(a>120):
                    a=0
                    cpt=cpt+1
            if(cpt==5):
                Robot.Arret=True
                #FirstPerson(Robot)
                #ScreenShot('im')
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
SimulationTriangle()
