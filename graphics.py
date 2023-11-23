# class for drawing numbers as lines, used to visualize the values stored in the Sorter class defined in sorter.py
# By Seth Robinson https://github.com/sethrobinson29 
from tkinter import *
from random import randrange, uniform, shuffle
colors = [ "#A18DCE", "#AA8ED2", "#B38ED6", "#BD8FD9", "#C68FDD", "#CF90E1", "#D890E5", "#E291E8", "#EB91EC", "#F492F0" ]
# colors = ["#dba8ac", "#f7fff7", "#00cc99", "#ffee88" ]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bar:
    def __init__(self, val, h, w):
        self.val = val
        self.height = h
        self.width = w
    
    # draws bar as gradient, sets color to tens place, meaning for arrays < 100 vals, only part of the gradient will be displayed
    def drawBar(self, canvas, point):
        color = (self.val % 100) // 10 if self.val > 9 else 0
        canvas.create_line(point.x, point.y, point.x, point.y+(self.height), fill=colors[color], width=self.width)
