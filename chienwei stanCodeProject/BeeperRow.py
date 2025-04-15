"""
File: BeeperRow.py
Name:
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    while front_is_clear():
        if on_beeper():
           move()
        else:
           put_beeper()
           move()
    pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
