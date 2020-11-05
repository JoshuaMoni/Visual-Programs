import pygame 
import math 
import random
import time 
import tkinter as tk

class Quick_sort():
    def __init__(self): 
        self.start = time.time()
        self.width = 1000
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Visual Binary Selection sort")

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)

    def draw(self, lines): 
        self.win.fill(self.white)

        for i in range(self.width): 
            #Here draw a line for each pixel on the width
            pygame.draw.line(self.win, self.black, (i, 0), (i, lines[i]))
        pygame.display.update()
        
    def partition(self, lines, low, high):
        pygame.event.pump()
        i = (low-1)         # index of smaller element
        pivot = lines[high]     # pivot
    
        for j in range(low, high):
            self.draw(lines)
            if lines[j] <= pivot:
    
                i = i+1
                lines[i], lines[j] = lines[j], lines[i]
    
        lines[i+1], lines[high] = lines[high], lines[i+1]
        return (i+1)
 
 
    def quickSort(self, lines, low, high):
        pygame.event.pump() #Windows crashs pygame when this isn't called
        if len(lines) == 1:
            return False #Breaks when it isnt run anymore

        if low < high:
    
            pi = self.partition(lines, low, high)
    
            self.quickSort(lines, low, pi-1)
            self.quickSort(lines, pi+1, high)

    def main(self): 
        run = True
        lines = []
        algorithm = True
        for i in range(self.width): 
            lines.append(random.randrange(1, self.height + 1))
        while run: 
            event = pygame.event.poll() #ATM its acutally impossible to close the program whilst its running as the interp is in the body
            if event.type == pygame.QUIT:
                pygame.display.quit()
                run = False
            if algorithm:    
                self.draw(lines)
                algorithm = self.quickSort(lines, 0, len(lines) - 1)