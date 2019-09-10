#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while wall_is_on_the_right() == False:
        if ((wall_is_above() == True) and (wall_is_beneath() == True)) :
            move_right()
        elif (wall_is_above() == False):
                move_up()
                fill_cell()
                move_down()
                if (wall_is_beneath() == False):
                    move_down()
                    fill_cell()
                    move_up()
                    move_right()
                else:
                    move_right()
        elif (wall_is_beneath() == False):
            move_down()
            fill_cell()
            move_up()
            if wall_is_above() == False:
                move_up()
                fill_cell()
                move_down()
                move_right()
            else:
                move_right()
    if (wall_is_above() == False):
            move_up()
            fill_cell()
            move_down()
            if wall_is_beneath() == False:
                move_down()
                fill_cell()
                move_up()
    if wall_is_beneath() == False:
        move_down()
        fill_cell()
        move_up()
        if wall_is_above() == False:
            move_up()
            fill_cell()
            move_down()
    if ((wall_is_above() == True) and (wall_is_beneath() == True) and (wall_is_on_the_right() == False)):
        move_right()
    

if __name__ == '__main__':
    run_tasks()
