#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_right()
    move_down()
    for i in range (3):
        fill_cell()
        move_down()
    move_up(2)
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_right(2)
    while (wall_is_on_the_right() == False):
        move_right(4)
        for k in range(2):
            fill_cell()
            move_left()
        fill_cell()
        move_right()
        move_up()
        fill_cell()
        move_down(2)
        fill_cell()
        move_up()
        move_right()
    move_left(2)
    move_up()




if __name__ == '__main__':
    run_tasks()
