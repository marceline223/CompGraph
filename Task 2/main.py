from tkinter import Image

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


def draw_cube():
    glPushMatrix()
    glTranslatef(-5, 0, 0)
    glEnable(GL_BLEND)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 0, 0, 0.4))
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutSolidCube(2.5)
    glutWireCube(2.5)
    glPopMatrix()
    glDisable(GL_BLEND)


def draw_torus():
    glPushMatrix()
    glTranslatef(5, 5, 0)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 100)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 1, 1))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1, 1, 1, 1))
    glutSolidTorus(0.6, 1.2, 64, 64)
    glPopMatrix()


def draw_octahedron():
    glPushMatrix()
    glTranslatef(-5, 0, 0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 1, 0, 1))
    glutSolidOctahedron()
    glPopMatrix()


def draw_sphere():
    glPushMatrix()
    glTranslatef(0, -5, 0)

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    image = Image.open("1.png")
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = image.convert("RGBA").tobytes()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glEnable(GL_TEXTURE_2D)

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 1, 1, 1))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 0)
    gluSphere(quadric, 2.5, 64, 64)
    gluDeleteQuadric(quadric)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()


def draw_figures():
    draw_octahedron()
    draw_cube()
    draw_torus()
    draw_sphere()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(15, 3, 15, 0, 0, 0, 0, 0, 1)
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)
    glRotatef(180, 0, 0, 1)
    draw_figures()
    glutSwapBuffers()


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
    if key == GLUT_KEY_UP:
        light_moving('up')
    elif key == GLUT_KEY_DOWN:
        light_moving('down')
    elif key == GLUT_KEY_RIGHT:
        light_moving('right')
    elif key == GLUT_KEY_LEFT:
        light_moving('left')


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
glutCreateWindow("Task 2")

glClearColor(0, 0, 0, 0)
light()
camera()

glutDisplayFunc(display)
glutIdleFunc(glutPostRedisplay)
glutKeyboardFunc(keyboard_callback)
glutMotionFunc(mouse_motion_callback)
glutMouseWheelFunc(mouse_wheel_callback)
glutSpecialFunc(special_keys_callback)

glutMainLoop()
