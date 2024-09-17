import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):

    win = curses.newwin(3, 18, 2, 2, )
    box = Textbox(win)
    rectangle(stdscr, 2, 2, 5, 20)

    stdscr.refresh()

    box.edit()

    stdscr.getch()


wrapper (main)