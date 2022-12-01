################
# Racket.py    #
# CLEMENT KM  #
# 07/04/2022  #
# Jeu de Pong #
###############
# constructor
import sys
import Background

def create(x=10.,y=10.,vx=0.,vy=0., color=0):
    racket = {'x': x,'y':y, 'vx':vx, 'vy':vy ,'color':color}
    return racket
# Accessors \mutators
def get_x(racket): return racket['x']
def set_x(racket, x): racket['x']=x
def get_y(racket): return racket['y']
def set_y(racket, y): racket['y']=y
def get_vx(racket): return racket['vx']
def set_vx(racket, vx): racket['vx']=vx
def get_vy(racket): return racket['vy']
def set_vy(racket, vy): racket['vy']=vy

# Operations  .
def live(racket,dt,img):
    i0=int(racket['x'])
    j0=int(racket['y'])
    racket['x']+=dt *racket['vx']
    racket['y']+=dt *racket['vy']
    x=racket['x']
    y=racket['y']
    i=int(x)
    j=int(y)
    c=Background.get_char(img,j,i)
    if not c==" ":
        if not i==i0:
            racket['vx']=-racket['vx']
        if not j==j0:
            racket['vy']=-racket['vy']
def show(racket):
    i=int(racket['x'])+1
    j=int(racket['y'])+1
    msg="\033["+str(j)+";"+str(i)+"H"
    sys.stdout.write(msg)
    sys.stdout.write("\033[4"+str(racket['color']+3)+"m")
    sys.stdout.write("|\n")
    sys.stdout.write("\033[40m")


def test_collision(t1, t2):
    if int(t1["x"]) == int(t2['x']) and int(t1["y"]) == int(t2['y']):
        return True
    return False

# test

if __name__ == "__main__":
    ra = create(2, 3, 5, 5, 6)
    show(ra)

