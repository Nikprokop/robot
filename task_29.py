#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    n = 0
    while ((n < 3) and (wall_is_on_the_right() == False)):
        move_right()
        if cell_is_filled() == True:
            n = n + 1
        else:
            n=0
    if n == 0:
        while wall_is_on_the_right() == False:
            move_right()


if __name__ == '__main__':
    run_tasks()
