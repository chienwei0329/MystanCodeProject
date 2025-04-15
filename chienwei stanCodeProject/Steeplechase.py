"""
File: Steeplechase.py
Name: chienwei:
---------------------------------
chienwei:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
       if front_is_clear():
           move()
       else:
           jump()
           turn_left()


def jump():
    """
    pre-condition:Karel is on the left side of the wall,facing East
    Post-condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()
def up():
    """
    pre-condition:Karel is on the left side of the wall,facing East
    Post-condition:Karel is at the upper left  of the wall,facing North
    """
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()
    turn_left()
    while not right_is_clear():
       move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def cross():
    """
    pre-condition:Karel is at the upper left of the wall,facing North
    Post-condition:Karel is at the upper right,facing South
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition:Karel is at the upper right,facing South
    Post-condition:Karel is at the upper right,facing South
    """
    while front_is_clear():
        move()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
