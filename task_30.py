#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    while wall_is_on_the_right() == False:
        move_right()
        a = a + 1








if __name__ == '__main__':
    run_tasks()
