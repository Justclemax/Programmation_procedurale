################
# Ball .py    #
# CLEMENT KM  #
# 07/04/2022  #
# Jeu de Pong #
###############
# constructor

import sys
import Background


def create(x=10.,y=10.,vx=0.,vy=0., color=0):
    racket = {'x': x, 'y': y, 'vx': vx, 'vy': vy, 'color': color}
    return racket
# Accessors \mutators
def get_x(ball): return ball['x']
def set_x(ball, x): ball['x'] = x
def get_y(ball): return ball['y']
def set_y(ball, y): ball['y'] = y
def get_vx(ball): return ball['vx']
def set_vx(ball, vx): ball['vx'] = vx
def get_vy(ball): return ball['vy']
def set_vy(ball, vy): ball['vy'] = vy

# Operations


def live(ball, dt, img):
    i0 = int(ball['x'])
    j0 = int(ball['y'])
    ball['x'] += dt*ball['vx']
    ball['y'] += dt*ball['vy']
    x = ball['x']
    y = ball['y']
    i = int(x)
    j = int(y)
    c = Background.get_char(img, j, i)
    if not c == " ":
        if not i == i0:
            ball['vx'] = -ball['vx']+1
        if not j == j0:
            ball['vy'] = -ball['vy'] + 1


def show(ball):
    # La position de la balle dans le terminal
    i = int(ball['x'])
    j = int(ball['y'])
    msg = "\033[" + str(j) + ";" + str(i) + "H"
    sys.stdout.write(msg)
    sys.stdout.write("\033[4" + str(ball['color']) + "m")
    b = "0"
    sys.stdout.write(b)
    sys.stdout.write("\033[40m")


def test_collision(b1, b2):

    if int(b1["x"]) == int(b2['x']) and int(b1["y"]) == int(b2['y']):
        return True
    return False


def change_position(b, img):
    i0 = int(b['x'])
    j0 = int(b['y'])
    b['x'] += b['vx']
    b['y'] += b['vy']
    i = int(b['x'])
    j = int(b['y'])

    c = Background.get_char(img, j, i)
    if not c == " ":
        if i != i0:
            b['vx'] = -b['vx'] % 4
        if j != j0:
            b['vy'] = -b['vy'] % 4



# test
#if __name__ =="__main__":
    ####show(ra)
