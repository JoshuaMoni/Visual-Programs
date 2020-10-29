import pygame 
import math 
import random
import time

class Selection():
    def __init__(self): 
        self.start = time.time()
        self.width = 1000
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Visual Selection sort")

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)

    def draw(self, win, width, lines): 
        win.fill(self.white)

        for i in range(width): 
            #Here draw a line for each pixel on the width
            pygame.draw.line(win, self.black, (i, 0), (i, lines[i]))
        pygame.display.update()
    
    def selection_sort(self, win, width, lines): 
        for i in range(width): 
            min_index = i 
            for j in range(i + 1, width): 
                if lines[j] < lines[min_index]: 
                    min_index = j 

            temp = lines[i]
            lines[i] = lines[min_index]
            lines[min_index] = temp
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
                algorithm = self.selection_sort(self.win, self.width, lines)
            if not algorithm and not show: 
                show = True
                print("Took: {}". format(time.time() - self.start))
