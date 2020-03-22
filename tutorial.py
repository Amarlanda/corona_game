import math
import random
import Pygame
import tkinter as tk
from tkinter import messagebox

class cube (object) 
    rows = 0
    w = 0
    def __init__self(,start,dirnx=dirny=0,color=(255,0,0)
    pass

    def move(self, dirnx, dirny)
        pass

    def draw(self, surface, eyes=False):

class snake(object):
    def __init__(self, color, pos):
    
    def move (self):
        pass

    def reset(self):        

    def addcube(self):
        pass

    draw(self, surface):
        pass

def drawGrid(w, rows, surface):
sizeBtwn = w // rows

x = 0 
y = 0 
   

def redrawWindow(Surface):
    global rows, width
    win.fill((0,0,0))
    drawGrid(width,rows, surface)
    pygame.display.update()

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0) , (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag          
        pygame.time.delay(50)
        clock.tick(10)

        reddrawWindow(win)
    pass

main()

while flag:
    Pygame.time.delay(50)
    clock.tick(10)    
pass
