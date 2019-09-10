#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while (wall_is_beneath() == False):
        if wall_is_on_the_right() == False:
            while wall_is_on_the_right() == False:
                fill_cell()
                move_right()
            fill_cell()
            move_down()
        if wall_is_on_the_right() == True:
            while wall_is_on_the_left() == False:
                fill_cell()
                move_left()
            fill_cell()
    if ((wall_is_above() == True) and (wall_is_beneath() == True)):
        if wall_is_on_the_right() == False:
            while wall_is_on_the_right() == False:
                fill_cell()
                move_right()
            fill_cell()
            while wall_is_on_the_left() == False:
                move_left()
        else:
            fill_cell()

if __name__ == '__main__':
    run_tasks()
