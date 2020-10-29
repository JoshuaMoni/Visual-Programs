import pygame 
import math 
import random

width, height = 400, 250
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visual Insetion sort")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

def draw(win, width, lines): 
    win.fill(white)

    for i in range(width): 
        #Here draw a line for each pixel on the width
        pygame.draw.line(win, black, (i, 0), (i, lines[i]))
    pygame.display.update()
    
def insertion_sort(win, width, lines): 
    for i in range(1, width): 
        key = lines[i]
        j = i - 1 
        while j >= 0 and key < lines[j]: 
            lines[j + 1] = lines[j]
            j-= 1 
            lines[j + 1] = key
            
            draw(win, width, lines)
    return False

def main(): 
    run = True
    lines = []
    for i in range(width): 
        lines.append(random.randrange(1, height))
    while run: 
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
    
        draw(win, width, lines)
        run = insertion_sort(win, width, lines)


main()