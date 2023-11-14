from tkinter import *
from random import randrange, uniform, shuffle
# colors = [ "#0b5351", "#4e8098", "#ffc857", "#90c2e7", "#ffb997", "#f67e7d", "#00a9a5", "#843b62", "#74546a", "#9ce37d", "#77867f", "#ff37a6" ]
colors = ["#dba8ac", "#f7fff7", "#00cc99", "#ffee88" ]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bar:
    def __init__(self, val, h, w):
        self.val = val
        self.height = h
        self.width = w

    def drawBar(self, canvas, point):
        canvas.create_line(point.x, point.y, point.x, point.y+(self.height), fill=colors[int(self.val)%4], width=self.width)
        # canvas.create_rectangle(point.x, point.y, point.x+self.width, point.y+(self.height), fill=colors[self.val-1])
