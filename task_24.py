#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_right(2)
    move_down()
    for i in range (3):
        fill_cell()
        move_down()
    move_up(2)
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up()


if __name__ == '__main__':
    run_tasks()
