import tkinter as tk

root = tk.Tk()

can = tk.Canvas(root, width = 500, height = 550)
can.pack()
can.create_line(500, 550, 500, 50, fill="#000")

root.mainloop()