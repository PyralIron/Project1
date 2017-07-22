import pygame
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
vertices= (
    (1, -1, -1),
    (0,1,0),
    (1,0,0),
    (0,0,1),
    (0,0,-1),
    (-1,0,0),
    (0,-1,0),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    #octahedron
    )
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    #octahedron
    (8,10),
    (8,12),
    (8,11),
    (8,13),
    (9,10),
    (9,12),
    (9,11),
    (9,13),
    (10,12),
    (10,13),
    (11,12),
    (11,13)
    )
faces = (
    (1,2,3),
    (4,2,1),
    (4,1,5),
    (1,3,5),
    (6,3,2),
    (5,3,6),
    (2,4,6),
    (4,5,6)
    )
def Cube():
    color = 0
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glColor3f(color,color+0.15,color+0.65)
            glVertex3fv(vertices[vertex])
            color = (color+0.1)%1
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0.0,0.0, -5)
    glFrontFace(GL_CW)
    glCullFace(GL_BACK)
    glEnable(GL_CULL_FACE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
