#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    n = 1
    while wall_is_on_the_right() == False:
        for i in range(n):
            if wall_is_on_the_right() == False:
                move_right()
        if wall_is_on_the_right() == False:
            fill_cell()
        n = n + 1

if __name__ == '__main__':
    run_tasks()
