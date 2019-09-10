#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if ((wall_is_on_the_left() == True) and (wall_is_above() == True)):
        while ((wall_is_on_the_right() == False) and (wall_is_beneath() == False)):
            move_right()
            move_down()
    elif ((wall_is_on_the_right() == True) and (wall_is_above() == True)):
        while ((wall_is_on_the_left() == False) and (wall_is_beneath() == False)):
            move_left()
            move_down()
    elif ((wall_is_on_the_left() == True) and (wall_is_beneath() == True)):
        while ((wall_is_on_the_right() == False) and (wall_is_above() == False)):
            move_right()
            move_up()
    elif ((wall_is_on_the_right() == True) and (wall_is_beneath() == True)):
        while ((wall_is_on_the_left() == False) and (wall_is_above() == False)):
            move_left()
            move_up()
if __name__ == '__main__':
    run_tasks()
