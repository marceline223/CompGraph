import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from time import sleep

rot = 0  # угол поворота
n_rot = 0  # номер поворота


def roll_parallelepiped(rotation):
    global n_rot
    if n_rot >= 0:
        glRotatef(rotation if n_rot == 0 else 90, 1.0, 1.0, 0.0)
        glTranslatef(-0.9, 0, 0)

    if n_rot >= 1:
        moving = rotate([0., 0.], [0., -1.0], rotation if n_rot == 1 else 90)
        glTranslatef(moving[0], moving[1], 0.0)
        glRotatef(rotation if n_rot == 1 else 90, 0.0, 0.0, 1.0)

    if n_rot >= 2:
        moving = rotate([0., 0.], [-1.0, 0.0], rotation if n_rot == 2 else 90)
        glTranslatef(moving[0], moving[1], 0.0)
        glRotatef(rotation if n_rot == 2 else 90, 0.0, 0.0, 1.0)

    if n_rot >= 3:
        moving = rotate([0., 0.], [0, 1.0], rotation if n_rot == 3 else 90)
        glTranslatef(moving[0], moving[1], 0.0)
        glRotatef(rotation if n_rot == 3 else 90, 0.0, 0.0, 1.0)

    add_physics()


def add_physics():
    global n_rot, rot
    if n_rot == 0:
        if rot < 20:  # первые 30 градусов падает медленно
            sleep(0.0005 * (91 - rot))
        elif rot < 80:
            sleep(0.0004 * (91 - rot))
        else:
            sleep(0.0004)
    elif n_rot == 1:
        if rot < 20:  # первые 30 градусов падает медленно
            sleep(0.0003 * (91 - rot))
        elif rot < 80:
            sleep(0.0002 * (91 - rot))
        else:
            sleep(0.0002)
    elif n_rot == 2:
        if rot < 20:  # первые 30 градусов падает медленно
            sleep(0.0004 * (91 - rot))
        elif rot < 80:
            sleep(0.0003 * (91 - rot))
        else:
            sleep(0.0003)
    else:
        if rot < 20:  # первые 30 градусов падает медленно
            sleep(0.0005 * (91 - rot))
        elif rot < 80:
            sleep(0.0004 * (91 - rot))
        else:
            sleep(0.0004)


def rotate(p, origin=(0, 0), degrees=0):
    angle = degrees * math.pi / 180  # в радианы
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle), np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    return np.squeeze((R @ (p.T - o.T) + o.T).T)


def draw_plane():  # плоскость
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.5, 0.5, 0.5))
    glBegin(GL_POLYGON)
    glVertex3f(-8, -8, -1.5)
    glVertex3f(8, -8, -1.5)
    glVertex3f(8, 8, -1.5)
    glVertex3f(-8, 8, -1.5)
    glEnd()


def draw_parallelepiped_without_texture():
    global rot, n_rot

    glPushMatrix()

    if rot < 90:
        rot += 1
    else:
        rot = 0
        n_rot += 1

    roll_parallelepiped(rot)
    glTranslatef(0.0, 0.0, 2)

    glRotate(45, 0, 0, 1)
    glScale(1, 1, 3)  # делаем параллелепипед путем масштабирования куба

    glEnable(GL_BLEND)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 0, 0, 0.7))
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutSolidCube(1)
    glutWireCube(1)

    glPopMatrix()
    glDisable(GL_BLEND)


def draw_figures():
    draw_plane()
    draw_parallelepiped_without_texture()  # вариант с полупрозрачным параллелепипедом


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    glLoadIdentity()
    gluLookAt(15, 3, 15, 0, 0, 0, 0, 0, 1)
    glRotatef(538, 1, 0, 0)
    glRotatef(560, 0, 1, 0)
    glRotatef(300, 0, 0, 1)
    draw_figures()
    glutSwapBuffers()
    glFlush()


def camera():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(30, 1, 1, 30)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()


def light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 5, 0, 0.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 1, 1, 0.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 0.0))


glutInit()

glutInitWindowPosition(0, 0)
glutInitWindowSize(750, 750)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow("CurseWork")

glClearColor(0, 0, 0, 0)
light()
camera()

glutDisplayFunc(display)
glutIdleFunc(display)

glutMainLoop()
