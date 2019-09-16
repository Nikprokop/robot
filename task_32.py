#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    a = 0

    while ((wall_is_beneath() == True) or ((wall_is_on_the_left() == True) and (wall_is_on_the_right() == True))) :
        while ((wall_is_above() == True) and (wall_is_beneath() == True)):
            fill_cell()
            move_right()
        if wall_is_on_the_right() == False:
            move_up()
        while ((wall_is_above() == False) and (wall_is_on_the_left() == True) and (wall_is_on_the_right() == True)):
            if cell_is_filled() == True:
                a = a + 1
            move_up()
        if wall_is_above() == True:
            if cell_is_filled() == True:
                a = a + 1
            while wall_is_beneath() == False:
                fill_cell()
                move_down()
        if wall_is_on_the_right() == False:
            move_right()

    mov('ax', a)




if __name__ == '__main__':
    run_tasks()
