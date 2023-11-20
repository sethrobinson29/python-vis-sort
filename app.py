from sorter import *
from math import *

vals, sortedVals = [], []
end =  numBars = comps = -1
root = Tk()
root.config(background="#297373")
root.geometry("1100x800")
root.title("vis-sort")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

title = Label(root, text="Sorting Algorithm Visualizer", fg="#be97c6", font=("Helvetica bold", 40), background="#2e294e", padx=20)
title.config(highlightbackground="#000034", highlightthickness=4, relief="raised")
title.grid(row=0)

canFrame = Frame(root,highlightbackground="#2e294e", highlightthickness=2, relief="raised")
canFrame.grid(row=1)
can = Sorter(canFrame)
can.canvas.pack()

# frame for bottom row of main window
lowFrame = Frame(root, background="#297373", pady=5, padx=20)
lowFrame.grid(row=2)

# comparisons output
compFrame = Frame(lowFrame, background="#000034", highlightbackground="#2e294e", highlightthickness=4, relief="ridge", pady=5, padx=20)
compFrame.grid(row=0, column=0)
compsLabel = Label(compFrame, text="Comparisons: ", background="#000034", fg="#be97c6", font="Helvetica 10")
compsLabel.grid(row=0, column=0)
compsDisplay = Label(compFrame, text="0", background="#000034", fg="#be97c6", font="Helvetica 10")
compsDisplay.grid(row=0, column=1)

# frame spacing
lowFrameSpace1 = Label(lowFrame, background="#297373", padx=10, text=" ")
lowFrameSpace1.grid(row=0, column=1)
lowFrameSpace2 = lowFrameSpace1 = Label(lowFrame, background="#297373", padx=10, text=" ")
lowFrameSpace1.grid(row=0, column=3)

# frame for buttons
bFrame = Frame(lowFrame, background="#000034", highlightbackground="#2e294e", highlightthickness=4, relief="ridge", pady=5, padx=20)
bFrame.grid(row=0, column=2)

# sorting buttons
sortFrame = Frame(bFrame, pady=5, background="#000034")
sortFrame.grid(row=0)
bubble = Button(sortFrame, bg="#be97c6", text="Bubble", command=lambda:(buttonClicked("bubble")), font="Helvetica 12")
bubble.grid(row=0, column=0, padx=5)
selection = Button(sortFrame, bg="#be97c6", text="Selection", command=lambda:(buttonClicked("selection")) , font="Helvetica 12")
selection.grid(row=0, column=1, padx=5)
mergeButton = Button(sortFrame, bg="#be97c6", text="Merge", command=lambda:(buttonClicked("merge")) , font="Helvetica 12")
mergeButton.grid(row=0, column=2, padx=5)
radix = Button(sortFrame,bg="#be97c6", text="Radix", command=lambda: (buttonClicked("radix")) , font="Helvetica 12")
radix.grid(row=0, column=3, padx=5)

# utility buttons
midFrame = Frame(bFrame, pady=5, background="#000034")
midFrame.grid(row=1)
backwards = Button(midFrame, bg="#be97c6", text="Reverse", command=can.reverse, font="Helvetica 12")
backwards.grid(row=0, column=1, padx=5)
# p = Button(midFrame, bg="#be97c6", text="print", command=lambda: (print(vals)))
# p.grid(row=0, column=1, padx=5)
genNums = Button(midFrame, bg="#be97c6", text="Create New Array", command=lambda:(can.makeNewVals(barScale.get())), font="Helvetica 12")
genNums.grid(row=0, column=0, padx=5)
closeProgram = Button(midFrame, bg="#be97c6", fg="#f31227", text="Quit", command=root.destroy, font="Helvetica 12 bold")
closeProgram.grid(row=0,  column=2, padx=5)

# change length of array based on slider
def scaleChange(event):
    if numBars != barScale.get():
        tmp = barScale.get()
        barScaleDisplay.config(text=tmp)
        can.makeNewVals(tmp)

# scale frame
scaleFrame = Frame(lowFrame, background="#000034", highlightbackground="#2e294e", highlightthickness=4, relief="ridge", pady=5, padx=20)
scaleFrame.grid(row=0, column=4)

# scale
barScale = Scale(scaleFrame,from_=50, to=500, orient=HORIZONTAL, resolution=5, bg="#000034", fg="#be97c6", highlightbackground="#2e294e", highlightthickness=4, troughcolor="#be97c6", activebackground="#2e294e", font="Helvetica 10")
barScale.bind("<ButtonRelease-1>", scaleChange)
barScale.grid(row=2, columnspan=2)

# scale label and display 
barLabelFrame = Frame(scaleFrame, background="#000034", highlightbackground="#2e294e", highlightthickness=4, relief="ridge", pady=5, padx=20) 
barLabelFrame.grid(row=0, columnspan=2)
barScaleLabel = Label(barLabelFrame, text="Size of Array ", background="#000034", fg="#be97c6", font="Helvetica 10")
barScaleLabel.grid(row=0, column=0)
barScaleDisplay = Label(barLabelFrame, text=barScale.get(), background="#000034", fg="#be97c6", font="Helvetica 10")
barScaleDisplay.grid(row=0, column=1)
scaleFrameSpace1 = Label(scaleFrame, background="#000034",  text=" ")
scaleFrameSpace1.grid(row=1, columnspan=2)

# initialize number of bars and array
can.makeNewVals(barScale.get())

# wrapper for sorting functions
def buttonClicked(buttonName):
    # sort 
    if buttonName == "bubble":
        can.bubbleSort()
    elif buttonName == "selection":
        can.selectionSort()
    elif buttonName == "merge":
        can.mergeSortWrap()
    elif buttonName == "quick":
        pass
    elif buttonName == "radix":
        can.radixSort()
    
    # update comparison display
    compsDisplay.config(text=can.comps)

if __name__ == "__main__":
    root.mainloop()
