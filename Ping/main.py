################
# main.py    #
# CLEMENT KM  #
# 07/04/2022  #
# Jeu de Pong #
###############
import sys
import time
import select
import tty
import termios

# Mes modules
import Ball
import Racket
import Background


def init(data):
    # initialisation de la partie
    data['score'] = 0
    data['timeStep'] = 0.2
    data['table'] = Background.create('image.txt')
    data['racket1'] = Racket.create(6, 2, 0, 4, 3)
    data['racket2'] = Racket.create(32, 5, 0, 0, 2)
    data['ball'] = Ball.create(10.1, 5.01, 2.4, 2., 4)

    # creation des elements du je
    # interaction clavier
    data['old_settings'] = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    return data


def live(data):
    Racket.live(data['racket1'], data['timeStep'], data['table'])
    Racket.live(data['racket2'], data['timeStep'], data['table'])
    Ball.live(data['ball'], data['timeStep'], data['table'])

    if (Racket.test_collision(data['racket2'], data['ball'])) and (Racket.test_collision(data['racket1'], data['ball'])):
        Ball.change_position(data['ball'],  data['table'])
        data['score'] += 1
        x, y = Background.give_random_location(data['table'])
        Ball.set_x(data['racket'], x)
        Ball.set_y(data['racket'], y)
    #if not (Racket.test_collision(data['racket1'], data['racket2'])):


def interact(data):
    # gestion des evenement clavier
    # si une touche est appuyee
    if isData():
        c = sys.stdin.read(True)
        if c == '\x1b':  # x1b is ESC
            quitGame(data)
        #elif c == 'q':
            ##Racket.set_vy(data['racket2'], 0)
        elif c == 'z':
            Racket.set_vx(data['racket2'], 0)
            Racket.set_vy(data['racket2'], -5)
        elif c == 's':
            Racket.set_vx(data['racket2'], 0)
            Racket.set_vy(data['racket2'], 5)


def isData():
    # recuperation evenement clavier
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def show(data):
    # rafraichissement de l'affichage
    # effacer la console
    sys.stdout.write("\033[10;10H")
    #sys.stdout.write("\033[2J")
    # restoration couleur
    # sys.stdout.write("\033[37m")
    # sys.stdout.write("\033[40m")
    # deplacement curseur

    sys.stdout.write("\033[0;0H\n")
    Background.show(data['table'])
    Racket.show(data['racket1'])
    Racket.show(data['racket2'])
    Ball.show(data['ball'])
    sys.stdout.write("\n")


def run(data):
    # Boucle de simulation
    while True:
        interact(data)
        live(data)
        show(data)
        time.sleep(data['timeStep'])


def quitGame(data):
    # couleur white
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, data['old_settings'])
    sys.exit()


def main():
    data = {}
    init(data)
    run(data)

# tests


if __name__ == "__main__":
    msg = "Appuyer "
    main()
    sys.stdout.write(msg)
