from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

global dz


def draw_axes():
    # ось x - зеленоватая
    glColor3f(0.5, 1, 0.5)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(5, 0, 0)
    glEnd()

    # ось y - голубоватая
    glLineWidth(1)
    glColor3f(0.5, 1, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 5, 0)
    glEnd()

    # ось z - белая
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 5)
    glEnd()


def display_3():
    glClear(GL_COLOR_BUFFER_BIT)  # очистка экрана
    glLoadIdentity()

    glRotatef(45, 1.0, 0.0, 0.0)
    glRotatef(-25, 0.0, 1.0, 0.0)
    glScale(0.25, 0.25, 0.25)

    draw_axes()

    # СФЕРА
    glPushMatrix()
    glColor3f(1, 0, 1)  # фиолетовый
    glTranslatef(1, 2, 3)
    glutWireSphere(0.7, 32, 32)
    glPopMatrix()

    # ТОР
    glPushMatrix()
    glColor3f(1, 1, 0)  # желтый
    glTranslatef(2, -1, -1)
    glutWireTorus(0.2, 0.5, 32, 32)
    glPopMatrix()

    time.sleep(0.025)
    glFlush()
    glutSwapBuffers()


def display_4():
    global dz
    glClear(GL_COLOR_BUFFER_BIT)  # очистка экрана
    glLoadIdentity()

    glRotatef(45, 1.0, 0.0, 0.0)
    glRotatef(-25, 0.0, 1.0, 0.0)
    glScale(0.25, 0.25, 0.25)

    draw_axes()

    # СФЕРА
    glPushMatrix()
    glColor3f(1, 0, 1)  # фиолетовый
    glTranslatef(1, 2, 3)
    glutWireSphere(0.7, 32, 32)
    glPopMatrix()

    # ТОР
    glPushMatrix()
    glColor3f(1, 1, 0)  # желтый
    glTranslatef(2, -1, -1)

    if dz < 3:
        dz += 0.2
    glTranslatef(0, 0, dz)
    glutWireTorus(0.2, 0.5, 32, 32)
    glPopMatrix()

    time.sleep(0.025)
    glFlush()
    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Task 3")

glutDisplayFunc(display_3)
glutIdleFunc(display_3)

glutInitWindowSize(800, 800)
glutInitWindowPosition(700, 0)
glutCreateWindow(b"Task 4")

dz = 0.0
glutDisplayFunc(display_4)
glutIdleFunc(display_4)


glutMainLoop()
