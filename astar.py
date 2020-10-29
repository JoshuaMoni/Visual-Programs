#This algorithm only condisers paths that are optimal 
#Informed search algorithm 
#Heuristic function to help guide us
#Only consider paths that are optimal  

"""Process"""
#Use an open set. The open set is a priority queque in this case 
#The open set keeps track of the nodes we want to look at next 
#Algorithm runs in F(n) = G(n) + H(n)
#H(n): Gives an estimate from node n to the ending node, uses the current node and the end node and creates an estimate of the absolute distance 
#The H score depends on the approach that you use to calculate it. There is more than one way 
#G(n): Current shortest distance from the start node to the current node
#F(n): The addition of H(n) and G(n)
#F(n): Gives us an estimate of how long it will take to get to the end node 
#This is used in the algorithm by prioritizing nodes with a lower f(n) value  

#When we start the algorithm the starting node has all values set to 0 
#All other nodes are set to infinity 
#Pop starting node from the open set 
#Look at where it points, is there a lower weight or time to get to the next node that it points to than what it currently has
#As the node will have scores of infinity than this is true 
#Then we take a guess at the H score 
#Update the F score with the total 
#Last variable tells you where you came from 

#Now we add the new node to the open set with the f score and the node itself
#Take the node in the open set with the lowest f score  
#The above steps are repeated 

#When you remove the end node out of the open set the algorithm end and returns the f score
#We find the path by backtracking from the last of each element 
import pygame 
import math
from queue import PriorityQueue

width = 800 
win = pygame.display.set_mode((width, width))
pygame.display.set_caption("A* Path Finding Algorithm")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
grey = (128, 128, 128)
turquoise = (64, 224, 208)

class Node:
    #Time 24min 
    def __init__(self, row, col, width, total_rows): 
        self.row = row
        self.col = col 
        self.width = width 
        self.x = row * width 
        self.y = col * width 
        self.colour = white
        self.neighbours = []
        self.total_rows = total_rows

    def get_pos(self): 
        return self.row, self.col
    
    def is_closed(self):
        #This is for checking if the node has already been looked at or not 
        #If it has been looked at then it will return red and false if it hasn't
        return self.colour == red

    def is_open(self): 
        return self.colour == green 
    
    def is_barrier(self): 
        return self.colour == black 

    def is_start(self): 
        return self.colour == orange 
    
    def is_end(self):
        return self.colour == turquoise 
    
    def reset(self): 
        self.colour = white 
    
    """Changing the colours""" 
    def make_start(self): 
        self.colour = orange

    def make_closed(self): 
        self.colour = red
    
    def make_open(self): 
        self.colour = green

    def make_barrier(self): 
        self.colour = black

    def make_end(self): 
        self.colour = turquoise

    def make_path(self): 
        self.colour = purple
    
    def draw(self, win): 
        #This draws the actual square 
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))
    
    def update_neighbours(self, grid): 
        #This checks if the nodes on either side are movable to or not i.e barriers or open
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #Move down
            self.neighbours.append(grid[self.row + 1][self.col]) 

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #Move up
            self.neighbours.append(grid[self.row - 1][self.col]) 

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): #Move left
            self.neighbours.append(grid[self.row][self.col - 1]) 

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): #Move right
            self.neighbours.append(grid[self.row][self.col + 1]) 
    
    def __lt__(self, other):
        #This is when we compare 2 nodes
        #This is set to return that the other spot is always greather than the current node or other way around 
        return False 

def h(p1, p2): 
    #Think of the p1 as row and p2 as column 
    #Using the manhattan formula 
    #Moving in an L shape, as it is the same as moving in a diagonal 
    #NOTE: p1 and p2 are tupples 
    x1, y1 = p1
    x2, y2 = p2 
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw): 
    #This back tracks from the end node to the start node along the came_from list and draws the path of nodes that was taken to find the shortest path
    while current in came_from: 
        current = came_from[current]
        current.make_path()
        draw()

def a_star(draw, grid, start, end): 
    count = 0 
    open_set = PriorityQueue()
    #Count is used in the occurance of a tie breaker
    #If two nodes have the same f score then the one that has the lower count will be used first
    open_set.put((0, count, start)) #0 is the f score, count is where it occured and start is the node 
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row} #Sets the G score of every node to infinity using dictionary comprehension
    g_score[start] = 0 
    f_score = {node: float("inf") for row in grid for node in row} #Sets the G score of every node to infinity using dictionary comprehension
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start} #This stores all the nodes that are currently in the open set  

    while not open_set.empty(): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()

        current = open_set.get()[2] #This looks at the current node, as the node is stored as the 3rd index in the priority queue
        open_set_hash.remove(current)

        if current == end: #This is when we have found the shortest path
            reconstruct_path(came_from, end, draw)
            end.make_end() #This draws the end node as itself
            return True 
        
        for neighbour in current.neighbours: 
            temp_g_score = g_score[current] + 1 #This is that we say it takes one more step to get to the next node as all edges have weight 1 

            if temp_g_score < g_score[neighbour]: 
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score 
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash: 
                    count += 1 
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()

        draw()
        if current != start: 
            #If this node is not the start node then close it off as we have already considered it and do not want to reconsider it 
            current.make_closed()

    return False #This is triggered when there in no such path 
def make_grid(rows, width): 
    grid = []
    gap = width // rows #This gives the width of what each square should be 
    for i in range(rows): 
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
        
    return grid 

def draw_grid(win, rows, width): 
    gap = width // rows 
    for i in range(rows): 
        pygame.draw.line(win, grey, (0, i * gap), (width, i * gap)) #Pass it the grid, colour, starting x y and ending x, y  
        for j in range(rows): 
            pygame.draw.line(win, grey, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width): 
    win.fill(white)

    for row in grid: 
        for spot in row: 
            spot.draw(win)
        
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width): 
    gap = width // rows 
    y, x = pos 

    row = y // gap 
    col = x // gap 

    return row, col 

def main(win, width): 
    #This can be changed so that the amount of rows changes
    #When done add the ability for the user to choose this 
    rows = 50 
    grid = make_grid(rows, width)

    start = None 
    end = None 
    run = True

    while run: 
        draw(win, grid, rows, width)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 

            if pygame.mouse.get_pressed()[0]: #Left
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node 
                    start.make_start()
                
                elif not end and node != start: 
                    end = node
                    end.make_end()

                elif node != start and node != end: 
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #Right
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                node = grid[row][col]

                node.reset()
                if node == start: 
                    start = None
                elif node == end: 
                    end = None
            

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and start and end: 
                    for row in grid: 
                         for node in row: 
                              node.update_neighbours(grid)
                    
                    result = a_star(lambda: draw(win, grid, rows, width), grid, start, end)
                    if result: 
                        print("There exists a path")
                    else: 
                        print("The end node is not reachable")
                    #lambda is an annoymous function that you don't have to define 
                
                if event.key == pygame.K_c: 
                    start = None 
                    end = None 
                    grid = make_grid(rows, width)
    pygame.quit()

main(win, width)