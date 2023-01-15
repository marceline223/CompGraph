import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ver = [[0 for j in range(3)] for i in range(64)]  # список вершин цилиндра

new_ver = []  # список морфированных вершин цилиндра

step = 0  # шаг морфирования
MAX_STEP = 15
MIN_STEP = 0


def getVertexOfCilynder():
    global ver, ver_circles
    x0 = 0
    y0 = 0
    R = 1.0
    n_ver = 0
    while n_ver < 64:
        alpha = (360 / 32) * (n_ver // 2) * math.pi / 180
        if n_ver % 2 == 0:
            ver[n_ver] = [x0 + R * math.sin(alpha), y0 + R * math.cos(alpha), -1]
        else:
            ver[n_ver] = [x0 + R * math.sin(alpha), y0 + R * math.cos(alpha), 1]
        n_ver += 1


def getNewVertex():
    global new_ver
    f = open("vertex.txt", "r")
    for line in f:
        new_ver.append([float(x) for x in line.split()])


def draw_cylinder():
    n_ver = 0
    glColor3f(1, 0, 0)
    dx, dy, dz = (0, 0, 0)
    while n_ver < 64:
        glBegin(GL_POLYGON)
        dx = (new_ver[n_ver % 64][0] - ver[n_ver % 64][0]) / MAX_STEP  # единичный сдвиг по х
        dy = (new_ver[n_ver % 64][1] - ver[n_ver % 64][1]) / MAX_STEP  # единичный сдвиг по y
        dz = (new_ver[n_ver % 64][2] - ver[n_ver % 64][2]) / MAX_STEP  # единичный сдвиг по z
        glVertex3f(ver[n_ver % 64][0] + dx * step, ver[n_ver % 64][1] + dy * step, ver[n_ver % 64][2] + dz * step)

        dx = (new_ver[(n_ver + 1) % 64][0] - ver[(n_ver + 1) % 64][0]) / MAX_STEP  # единичный сдвиг по х
        dy = (new_ver[(n_ver + 1) % 64][1] - ver[(n_ver + 1) % 64][1]) / MAX_STEP  # единичный сдвиг по y
        dz = (new_ver[(n_ver + 1) % 64][2] - ver[(n_ver + 1) % 64][2]) / MAX_STEP  # единичный сдвиг по z
        glVertex3f(ver[(n_ver + 1) % 64][0] + dx * step, ver[(n_ver + 1) % 64][1] + dy * step,
                   ver[(n_ver + 1) % 64][2] + dz * step)

        dx = (new_ver[(n_ver + 3) % 64][0] - ver[(n_ver + 3) % 64][0]) / MAX_STEP  # единичный сдвиг по х
        dy = (new_ver[(n_ver + 3) % 64][1] - ver[(n_ver + 3) % 64][1]) / MAX_STEP  # единичный сдвиг по y
        dz = (new_ver[(n_ver + 3) % 64][2] - ver[(n_ver + 3) % 64][2]) / MAX_STEP  # единичный сдвиг по z
        glVertex3f(ver[(n_ver + 3) % 64][0] + dx * step, ver[(n_ver + 3) % 64][1] + dy * step,
                   ver[(n_ver + 3) % 64][2] + dz * step)

        dx = (new_ver[(n_ver + 2) % 64][0] - ver[(n_ver + 2) % 64][0]) / MAX_STEP  # единичный сдвиг по х
        dy = (new_ver[(n_ver + 2) % 64][1] - ver[(n_ver + 2) % 64][1]) / MAX_STEP  # единичный сдвиг по y
        dz = (new_ver[(n_ver + 2) % 64][2] - ver[(n_ver + 2) % 64][2]) / MAX_STEP  # единичный сдвиг по z
        glVertex3f(ver[(n_ver + 2) % 64][0] + dx * step, ver[(n_ver + 2) % 64][1] + dy * step,
                   ver[(n_ver + 2) % 64][2] + dz * step)

        glEnd()
        n_ver += 2


def draw_circles():
    global ver
    n_ver = 0
    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)
    while n_ver < 64:
        dx = (new_ver[n_ver % 64][0] - ver[n_ver % 64][0]) / MAX_STEP  # единичный сдвиг по х
        dy = (new_ver[n_ver % 64][1] - ver[n_ver % 64][1]) / MAX_STEP  # единичный сдвиг по y
        dz = (new_ver[n_ver % 64][2] - ver[n_ver % 64][2]) / MAX_STEP  # единичный сдвиг по z
        glVertex3f(ver[n_ver][0] + dx * step, ver[n_ver][1] + dy * step, ver[n_ver][2] + dz * step)
        n_ver += 2
    glEnd()

    n_ver = 1
    glBegin(GL_POLYGON)
    while n_ver < 64:
        dx = (new_ver[n_ver % 64][0] - ver[n_ver % 64][0]) / MAX_STEP  # единичный сдвиг по х
        dy = (new_ver[n_ver % 64][1] - ver[n_ver % 64][1]) / MAX_STEP  # единичный сдвиг по y
        dz = (new_ver[n_ver % 64][2] - ver[n_ver % 64][2]) / MAX_STEP  # единичный сдвиг по z
        glVertex3f(ver[n_ver][0] + dx * step, ver[n_ver][1] + dy * step, ver[n_ver][2] + dz * step)
        n_ver += 2
    glEnd()


def draw_figures():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 1))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 0)
    draw_circles()

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (255 / 255, 165 / 255, 0, 1))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 0)
    draw_cylinder()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(15, 3, 15, 0, 0, 0, 0, 0, 1)
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)
    glRotatef(180, 0, 0, 1)
    glScale(2, 2, 2)
    draw_figures()
    glutSwapBuffers()
    glFlush()


def keyboard_callback(key, x, y):
    global light0_y
    if key == b'r':
        light_change_color('r')
    elif key == b'g':
        light_change_color('g')
    elif key == b'b':
        light_change_color('b')
    elif key == b'y':
        light_change_color('y')
    elif key == b'p':
        light_change_color('p')
    elif key == b'w':
        light_change_color('w')


def mouse_motion_callback(x, y):
    global begin_x, begin_y, rotation_x, rotation_y
    rotation_x = rotation_x + (y - begin_y)
    rotation_y = rotation_y + (x - begin_x)
    begin_x = x
    begin_y = y


def special_keys_callback(key, *args):
    global step
    if key == GLUT_KEY_RIGHT:
        if step < MAX_STEP:
            step += 1
    elif key == GLUT_KEY_LEFT:
        if step > MIN_STEP:
            step -= 1


def mouse_wheel_callback(wheel, state, x, y):
    if state == 1:
        light_intensity('+')
    elif state == -1:
        light_intensity('-')


def camera():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50, 1, 1, 50)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()


def light():
    global light0_x, light0_y, light0_z, light0_color_x, light0_color_y, light0_color_z
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glLightfv(GL_LIGHT0, GL_POSITION, (light0_x, light0_y, light0_z, 0.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (light0_color_x, light0_color_y, light0_color_z, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (light0_color_x, light0_color_y, light0_color_z, 0.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (light0_color_x, light0_color_y, light0_color_z, 0.0))


def light_moving(direction):
    global light0_x, light0_z
    if direction == 'left':
        light0_x -= 1.0
        glLightfv(GL_LIGHT0, GL_POSITION, (light0_x, light0_y, light0_z, 0.0))
    elif direction == 'right':
        light0_x += 1.0
        glLightfv(GL_LIGHT0, GL_POSITION, (light0_x, light0_y, light0_z, 0.0))
    elif direction == 'up':
        light0_z += 1.0
        glLightfv(GL_LIGHT0, GL_POSITION, (light0_x, light0_y, light0_z, 0.0))
    elif direction == 'down':
        light0_z -= 1.0
        glLightfv(GL_LIGHT0, GL_POSITION, (light0_x, light0_y, light0_z, 0.0))


def light_intensity(direction):
    global light0_color_x, light0_color_y, light0_color_z
    if direction == '+':
        if 0.0 < light0_color_x < 1.0:
            light0_color_x += 0.05
        if 0.0 < light0_color_y < 1.0:
            light0_color_y += 0.05
        if 0.0 < light0_color_z < 1.0:
            light0_color_z += 0.05
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (light0_color_x, light0_color_y, light0_color_z, 1.0))
    elif direction == '-':
        if 0.05 < light0_color_x:
            light0_color_x -= 0.05
        if 0.05 < light0_color_y:
            light0_color_y -= 0.05
        if 0.05 < light0_color_z:
            light0_color_z -= 0.05
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (light0_color_x, light0_color_y, light0_color_z, 1.0))


def light_change_color(color):
    global light0_color_x, light0_color_y, light0_color_z
    if color == 'r':
        light0_color_x = 1.0
        light0_color_y = 0.0
        light0_color_z = 0.0
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (light0_color_x, light0_color_y, light0_color_z, 1.0))
    elif color == 'g':
        light0_color_x = 0.0
        light0_color_y = 1.0
        light0_color_z = 0.0
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (light0_color_x, light0_color_y, light0_color_z, 1.0))
    elif color == 'b':
        light0_color_x = 0.0
        light0_color_y = 0.0
        light0_color_z = 1.0
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (light0_color_x, light0_color_y, light0_color_z, 1.0))
    elif color == 'w':
        light0_color_x = 1.0
        light0_color_y = 1.0
        light0_color_z = 1.0
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (light0_color_x, light0_color_y, light0_color_z, 1.0))


light0_x = 0.0
light0_y = 5.0
light0_z = 0.0
light0_color_x = 1.0
light0_color_y = 1.0
light0_color_z = 1.0

begin_x = 0
begin_y = 0
rotation_x = 538
rotation_y = 543

glutInit()

glutInitWindowPosition(0, 0)
glutInitWindowSize(750, 750)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow("Task 3")

glClearColor(0, 0, 0, 0)
light()
camera()

glutDisplayFunc(display)
glutIdleFunc(glutPostRedisplay)
glutKeyboardFunc(keyboard_callback)
glutMotionFunc(mouse_motion_callback)
glutMouseWheelFunc(mouse_wheel_callback)
glutSpecialFunc(special_keys_callback)

getVertexOfCilynder()
getNewVertex()

glutMainLoop()
