#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    while wall_is_on_the_right() == False:
        move_right()
        if wall_is_above() == False:
            while wall_is_above() == False:
                move_up()
                fill_cell()
            fill_cell()
            while wall_is_beneath() == False:
                move_down()
    while wall_is_beneath() == True:
        move_left()


if __name__ == '__main__':
    run_tasks()
