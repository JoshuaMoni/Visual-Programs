import tkinter as tk #Used for interface 
import binary_selection as bs #Importing the different algorithms
import selection as selection
import insertion as insertion
import quicksort as quick
#import merge as merge
import time #Used to record the running time of the algorithms
#import astar as astar

root = tk.Tk()
root.resizable(0, 0)
root.title("Selection Window")
width = 400
height = 200
root.geometry(str(width)+ "x" + str(height))

disc = tk.Label(root, text = "The following is a visual sorting algorithm tool", font = ("Times", 14))
disc.place(x = width//20, y = height // 10)
disc2 = tk.Label(root, text = "Select an algorithm to see how it sorts", font = ("Times", 12))
disc2.place(x = width//5, y = height // 4)
run_time = tk.Label(root, text = "The selected algoirthm took this long to run", font = ("Times", 10))
run_time.place(x = (width // 2) - 125, y = (height // 2) + 40)
result_window = tk.Entry()
result_window.place(x = (width // 2) - 80, y = (height // 2) + 60)

"""Runner code of the buttons"""
#Clears the run time window incase there was something already being displayed 
#Starts new time 
#Runs algorithm 
#Displays time 
#NOTE: Need to change it so that the time does not depend on when you close the window
def run_binary(): 
    result_window.delete(0, "end")
    start_time = time.time()
    a = bs.Binary_selection()
    a.main()
    result = str(round(time.time() - start_time, 2)) + " Seconds"
    result_window.insert(0, result)

def run_selection(): 
    result_window.delete(0, "end")
    start_time = time.time()
    b = selection.Selection()
    b.main()
    result = str(round(time.time() - start_time, 2)) + " Seconds"
    result_window.insert(0, result)

def run_insertion(): 
    result_window.delete(0, "end")
    start_time = time.time()
    c = insertion.Insertion()
    c.main()
    result = str(round(time.time() - start_time, 2)) + " Seconds"
    result_window.insert(0, result)

def run_quick(): 
    result_window.delete(0, "end")
    start_time = time.time()
    a = quick.Quick_sort()
    a.main()
    result = str(round(time.time() - start_time, 2)) + " Seconds"
    result_window.insert(0, result)
"""
#This needs to be fixed
def run_merge(): 
    result_window.delete(0, "end")
    start_time = time.time()
    a = merge.Main()
    a.main()
    result = str(round(time.time() - start_time, 2)) + " Seconds"
    result_window.insert(0, result)
"""
"""
#Implement this when there is time
def run_astar(): 
    d = astar.Main()
    d.main()
"""

binary = tk.Button(root, text="Binary Selection Sort", command = run_binary)
select = tk.Button(root, text="Selection Sort", command = run_selection)
insert = tk.Button(root, text="Insertion Sort", command = run_insertion)
quickB = tk.Button(root, text="Quick Sort", command = run_quick)
#mergeB = tk.Button(root, text="Merge Sort", command = run_merge)
#astar = tk.Button(root, text="Astar Path", command = run_astar)
binary.pack(side = "left")
select.pack(side = "right")
insert.pack(side = "right")
quickB.pack(side = "left")
#mergeB.pack(side = "left")
#astar.pack(side = "top")
root.mainloop()