#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    move_down(2)
    while wall_is_beneath() == False:
        move_right()
        move_up(2)
        for i in range(3):
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
        while wall_is_on_the_left() == False:
            move_left()
        for i in range(5):
            move_down()
    move_right(2)
    move_up()
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
    while wall_is_on_the_left() == False:
        move_left()
    move_up()

if __name__ == '__main__':
    run_tasks()
