import pygame #Used to draw 
import math 
import random

class Insertion(): 
    def __init__(self): 
        self.width = 1000 #These dimensions should be changed otherwise it takes too long to run
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height)) #For the display
        pygame.display.set_caption("Visual Insetion sort")

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)

    def draw(self, win, width, lines): #Draws the lines
        win.fill(self.white)
        for i in range(width): 
            #Here draw a line for each pixel on the width
            pygame.draw.line(win, self.black, (i, 0), (i, lines[i]))
        pygame.display.update()
    
    def insertion_sort(self, win, width, lines): 
        for i in range(1, width): 
            pygame.event.pump()
            key = lines[i] #Key is the sorted part of the list, once it has been sorted it doesnt need to be drawn again
            j = i - 1 
            while j >= 0 and key < lines[j]: 
                lines[j + 1] = lines[j]
                j-= 1 
                lines[j + 1] = key
                
                self.draw(win, width, lines)
                
        return False

    def skip(self, win, width, lines): 
        """Find a way to implement this that pygame will accept"""
        for i in range(1, width): 
            key = lines[i] #Key is the sorted part of the list, once it has been sorted it doesnt need to be drawn again
            j = i - 1 
            while j >= 0 and key < lines[j]: 
                lines[j + 1] = lines[j]
                j-= 1 
                lines[j + 1] = key

        self.draw(win, width, lines)
        return False

    def main(self): 
        run = True
        lines = []
        algorithm = True
        for i in range(self.width): 
            lines.append(random.randrange(1, self.height))

        while run: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: 
                        self.skip(self.win, self.width, lines)

                elif self.insertion_sort(self.win, self.width, lines): 
                    self.draw(self.win, self.width, lines)

#a = Insertion()
#a.main()