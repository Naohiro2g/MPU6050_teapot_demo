#!/usr/bin/python

import pygame
import urllib
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import radians
from pygame.locals import *
import sys

SCREEN_SIZE = (800, 600)
SCALAR = .5
SCALAR2 = 0.2

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / height, 0.001, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 1.0, -5.0,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0)

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_BLEND)
    glEnable(GL_POLYGON_SMOOTH)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.3, 0.3, 1.0));

def read_values():
    link = "http://127.0.0.1:8080" # Change this address to your settings
    f = urllib.urlopen(link)
    myfile = f.read()
    return myfile.split(" ")

def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | OPENGL | DOUBLEBUF)
    resize(*SCREEN_SIZE)
    init()
    clock = pygame.time.Clock()
    angle = 0
    glutInit(sys.argv)

    while True:
        then = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                return

        values = read_values()
        x_angle = values[0]
        y_angle = values[1]
        z_angle = values[2]

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor((1.,1.,1.))
        glLineWidth(1)
        glBegin(GL_LINES)
        for x in range(-20, 25, 5):
            glVertex3f(x/10.,-1,-1)
            glVertex3f(x/10.,-1,1)

        for x in range(-20, 25, 5):
            glVertex3f(x/10.,-1, 1)
            glVertex3f(x/10., 1, 1)

        for z in range(-10, 15, 5):
            glVertex3f(-2, -1, z/10.)
            glVertex3f( 2, -1, z/10.)

        for z in range(-10, 15, 5):
            glVertex3f(-2, -1, z/10.)
            glVertex3f(-2,  1, z/10.)

        for z in range(-10, 15, 5):
            glVertex3f( 2, -1, z/10.)
            glVertex3f( 2,  1, z/10.)

        for y in range(-10, 15, 5):
            glVertex3f(-2, y/10., 1)
            glVertex3f( 2, y/10., 1)

        for y in range(-10, 15, 5):
            glVertex3f(-2, y/10., 1)
            glVertex3f(-2, y/10., -1)

        for y in range(-10, 15, 5):
            glVertex3f(2, y/10., 1)
            glVertex3f(2, y/10., -1)
        glEnd()

        glPushMatrix()
        glRotate(float(x_angle), 1, 0, 0)
        glRotate(-float(y_angle), 0, 0, 1)
#        glRotate(-float(z_angle), 0, 1, 0)
        glutWireTeapot(1)
        #glutSolidTeapot(1)
        glPopMatrix()

        pygame.display.flip()

if __name__ == "__main__":
    run()
