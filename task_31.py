#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    k = 1
    while wall_is_beneath() == False:
        move_down()
    while wall_is_on_the_left() == False:
        move_left()
        k = k +1
        i = 0
    while i < k - 1:
        if wall_is_on_the_right() == False and wall_is_beneath() == True:
            move_right()
            i = i + 1
        if wall_is_beneath() == False:
            i = 0
            move_down()
            while wall_is_on_the_left() == False:
                move_left()
    while wall_is_on_the_left() == False:
        move_left()
if __name__ == '__main__':
    run_tasks()
