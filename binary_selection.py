import pygame 
import math 
import random
import time 

class Binary_selection():
    def __init__(self): 
        self.start = time.time()
        self.width = 1000
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Visual Binary Selection sort")

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)

    def draw(self, win, width, lines): 
        win.fill(self.white)

        for i in range(width): 
            #Here draw a line for each pixel on the width
            pygame.draw.line(win, self.black, (i, 0), (i, lines[i]))
        pygame.display.update()
        
    def binary_search(self, arr, val, l, r): 
        if l == r: 
            if arr[l] > val: 
                return l
            else: 
                return l + 1 
        if l > r: 
            return l 
        
        mid = (l+r)//2 
        if arr[mid] < val: 
            return self.binary_search(arr, val, mid+1, r)
        elif arr[mid] > val: 
            return self.binary_search(arr, val, l, mid-1)
        else: 
            return mid

    def insertion_sort(self, win, width, lines): 
        for i in range(1, width): 
            key = lines[i]
            j = self.binary_search(lines, key, 0, i-1)
            lines = lines[:j] + [key] + lines[j:i] + lines[i+1:]
            
            self.draw(win, width, lines)
        return False

    def main(self): 
        run = True
        lines = []
        algorithm = True
        show = False
        for i in range(self.width): 
            lines.append(random.randrange(1, self.height + 1))
        while run: 
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                run = False
            if algorithm:    
                self.draw(self.win, self.width, lines)
                algorithm = self.insertion_sort(self.win, self.width, lines)
            if not algorithm and not show: 
                show = True
                print("Took: {}". format(time.time() - self.start))

