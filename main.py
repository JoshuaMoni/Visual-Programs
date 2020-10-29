import tkinter as tk
import binary_selection as bs
import selection as selection

root = tk.Tk()
def run_binary(): 
    a = bs.Binary_selection()
    a.main()

def run_selection(): 
    b = selection.Selection()
    b.main()

binary = tk.Button(root, text="Binary Selection Sort", command = run_binary)
select = tk.Button(root, text="Selection Sort", command = run_selection)
binary.pack(side = "left")
select.pack(side = "right")
root.mainloop()


