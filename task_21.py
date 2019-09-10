#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    n=0
    fill_cell()
    for i in range(13):
        n=n+1
        for g in range(n):
            fill_cell()
            move_right()
        for g in range(n):
            move_left()
        move_down()









if __name__ == '__main__':
    run_tasks()
