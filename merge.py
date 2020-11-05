import pygame 
import math 
import random
import time 
import tkinter as tk

class Main():
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
        
    def mergeSort(self, win, width, lines): 
        pygame.event.pump()
        if len(lines) >1: 
            self.draw(lines)
            mid = len(lines)//2 # Finding the mid of the array 
            L = lines[:mid] # Dividing the array elements  
            R = lines[mid:] # into 2 halves 
    
            self.mergeSort(win, width, L) # Sorting the first half 
            self.mergeSort(win, width, R) # Sorting the second half 
            
            i = j = k = 0
            
            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                
                if L[i] < R[j]: 
                    lines[k] = L[i] 
                    i+= 1
                else: 
                    lines[k] = R[j] 
                    j+= 1
                k+= 1
                
            # Checking if any element was left 
            while i < len(L): 
                lines[k] = L[i] 
                i+= 1
                k+= 1
            
            while j < len(R): 
                lines[k] = R[j] 
                j+= 1
                k+= 1

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
                algorithm = self.mergeSort(lines, 0, len(lines) - 1)