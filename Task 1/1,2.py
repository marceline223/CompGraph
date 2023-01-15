from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

global current_angle, dx


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


def display_1():
    glClear(GL_COLOR_BUFFER_BIT)  # очистка экрана
    glLoadIdentity()

    glRotatef(45, 1.0, 0.0, 0.0)
    glRotatef(-25, 0.0, 1.0, 0.0)
    glScale(0.25, 0.25, 0.25)

    draw_axes()

    # КУБ
    glPushMatrix()
    glColor3f(1, 0, 0)  # красный
    glutWireCube(1)
    glPopMatrix()

    # ОКТАЭДР
    glPushMatrix()
    glTranslatef(-0.5, -0.5, -0.5)  # переносим октаэдр для совпадения некоторых вершин
    glColor3f(0, 0, 1)  # синий
    glutWireOctahedron()
    glPopMatrix()

    time.sleep(0.025)
    glFlush()
    glutSwapBuffers()


def display_2():
    global current_angle
    global dx
    glClear(GL_COLOR_BUFFER_BIT)  # очистка экрана
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glRotatef(45, 1.0, 0.0, 0.0)
    glRotatef(-25, 0.0, 1.0, 0.0)
    glScale(0.25, 0.25, 0.25)

    draw_axes()

    # КУБ
    glPushMatrix()
    glRotatef(current_angle, 1.0, 0.0, 0.0)
    if current_angle > -45:
        current_angle -= 1
    glColor3f(1, 0, 0)  # красный
    glutWireCube(1)
    glPopMatrix()

    # ОКТАЭДР
    glPushMatrix()
    glTranslatef(-0.5, -0.5, -0.5)  # перенос для совпадения вершин
    glColor3f(0, 0, 1)  # синий
    if (dx < 5) & (current_angle == -45):
        dx += 0.025
    glTranslatef(dx, 0, 0)  # перенос по заданию
    glutWireOctahedron()
    glPopMatrix()

    time.sleep(0.025)
    glFlush()
    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow("Task 1")

glutDisplayFunc(display_1)
glutIdleFunc(display_1)

glutInitWindowSize(800, 800)
glutInitWindowPosition(700, 0)
glutCreateWindow("Task 2")

current_angle = 0
dx = 0
glutDisplayFunc(display_2)
glutIdleFunc(display_2)

glutMainLoop()
