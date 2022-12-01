################
# Background.py    #
# CLEMENT KM  #
# 07/04/2022  #
# Jeu de Pong #
###############

import sys
import random


def create(mytable):
    table = {'width': None, 'height': None, 'grid': []}
    myfile = open(mytable, "r")
    s = myfile.read()
    myfile.close()
    lines = s.splitlines()
    for line in lines:
        table['grid'].append(list(line))
    table['height']=len(lines)
    table['width'] =len(lines[0])
    return table


def get_width(table): return table['width']
def set_width(table, width) : table['width'] =width
def get_height(table): return table['height']
def set_height(table, height) : table['width'] = height
def get_grid(table): return table['grid']


def set_grid(table, grid):
    table['grid'] = grid
    table['height'] = len(grid)
    table['width'] = len(grid[0])


def show(table):
    for j in range(table['height']):
        for i in range(table['width']):
            sys.stdout.write("\033["
                         +str(j+1)
                         +";"
                         +str(i+1)
                         +"H")
            sys.stdout.write(get_char(table, j, i))
    sys.stdout.write("\n")


def get_char(table,line_index, column_index):
    return table['grid'][line_index][column_index]


def set_char(table,line_index, column_index, c):
    table['grid'][line_index][column_index] = c


def give_random_location(i):
    x = random.randint(0, i['width'])
    y = random.randint(0, i['height'])
    while not get_char(i, y, x) == " ":
        x = random.randint(0, i['width'])
        y = random.randint(0, i['height'])
    return x, y


if __name__ == '__main__':
    ci = create('image.txt')

    show(ci)
