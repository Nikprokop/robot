#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    a = 1
    while wall_is_on_the_right() == False:
        move_right()
        a = a + 1
    for i in range (1,a):
        for g in range(1,a):
            if (g == i) or ((a+1-g) == i):
                move_left()
            else:
                fill_cell()
                move_left()
            if wall_is_on_the_left() == True and wall_is_beneath() == False:
                move_down()
                if (g != i):
                    fill_cell()
                while wall_is_on_the_right() == False:
                    move_right()
    move_left()
    while wall_is_on_the_left() == False:
        fill_cell()
        move_left()











if __name__ == '__main__':
    run_tasks()
