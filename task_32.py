#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    while (wall_is_beneath() == True):
        if ((wall_is_above() == True) and (wall_is_beneath() == True)):
            fill_cell()
        move_right()
        if wall_is_above() == False:
            while wall_is_above() == False:
                if cell_is_filled() == True:
                    a = a + 1
                move_up()
            while wall_is_beneath() == False:
                move_down()




if __name__ == '__main__':
    run_tasks()
