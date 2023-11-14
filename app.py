from graphics import *
from math import *
import time
# import pygame
import sys
sys.setrecursionlimit(1100)     # for  unknownSort's recursion depth

vals, sortedVals = [], []
end =  numBars = comps = -1
root = Tk()
root.config(background="#297373")
root.geometry("1100x750")
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
can = Canvas(canFrame, height=550, width=1015,highlightbackground="#2e294e", highlightthickness=2, background="#000034")
can.pack()

# pygame.init()
# sound = pygame.mixer.Sound("sound1.mp3")

# def playSound():
#     pygame.mixer.Sound.play(sound)
#     pygame.mixer.music.stop()

# fills array, sorts array for comparison, sets global variables, draws array on canvas prints array to console 
def makeNewVals(length):
    global vals, sortedVals, end, numBars, comps
    numBars = length
    # vals = [randrange(1, 23) for i in range(length)]  
    vals = [i for i in range(length)]
    shuffle(vals)
    # vals = [round(uniform(1.0, 10.9), 2)for i in range(length)]
    sortedVals = sorted(vals)
    end = length - 1
    comps = 0
    drawNums()
    # print(vals)

# draws bars representing array on screen; ONLY CALL AFTER/DURING makeNewVals
def drawNums():
    can.delete('all')
    x, y, = 10, 500
    
    for i in range(end + 1):
        y -= (vals[i]*4)
        # y -= vals[i]
        tmp = Bar(vals[i], 550-y, (numBars // 1000) + 1)
        tmp.drawBar(can, Point(x, y))
        # playSound()
        x += (1000 // numBars)
        y = 500

    root.update_idletasks()

# initialize number of bars and array
numBars = 100
makeNewVals(numBars)

def swapVals(arr, i, j):
    tmp = vals[j]
    arr[j] = arr[i]
    arr[i] = tmp

# reverses array
def reverse(i, j):
    if i >= j:
        print("Reverse Done")
        return 
    else:
        swapVals(vals, i, j)
        drawNums()
        i += 1
        j -= 1
        reverse(i, j)

# recursively bubble sort array; stop used to not iterated over previously sorted array. 
def bubbleSort(arr):
    global comps
    stop = len(arr)
    for i in range(stop-1):
        for j in range(stop-i-1):
            comps += 1                                                              # comparisons
            if arr[j] > arr[j+1]:
                drawNums()
                swapVals(vals, j, j+1)
    print("bubbleSort complete")
    print("Comparisons: ", comps)
    drawNums()


# recursively select the largest element of the remaining unsorted array and move it to the correct position
def selectionSort(stop):
    global comps
    for i in range(stop):
        for j in range(i+1, stop+1):
            comps += 1                                                              # comparisons
            if vals[i] > vals[j]:
                swapVals(vals, i, j)
                drawNums()
    drawNums()
    print("selectionSort complete")
    print("Comparisons: ", comps)

#TODO: figure out what this algorithm is
def unknownSort(stop):
    global comps
    curMax = -999
    swapIndex = -1
    for i in range(stop+1):
        comps += 1                                                              # comparisons
        if vals[i] > curMax:
            curMax = vals[i]
            swapIndex = i
            # swapVals(vals, i, stop)
            # drawNums()
    swapVals(vals, swapIndex, stop)
    drawNums()
    if stop > 0:
        # print("Next Pass", stop, curMax)
        # can.after(100, lambda:(uknownSort(stop-1)))
        unknownSort(stop-1)
    else:
        print("unknownSort complete")
        print("Comparisons: ", comps)

def merge(arr, begin, mid, end):
    global comps
    x, y = begin, mid + 1
    tmp = []

    for i in range(begin, end+1):
        comps += 1                                                              # comparisons
        if x > mid:
            tmp.append(arr[y])
            y += 1
        elif y > end:
            tmp.append(arr[x])
            x += 1
        elif arr[x] < arr[y]:
            tmp.append(arr[x])
            x += 1
        else:
            tmp.append(arr[y])
            y += 1
    
    for i in range(len(tmp)):
        arr[begin] = tmp[i]
        begin += 1

def mergeSort(arr, begin, end):
    global comps
    if begin < end:
        # comps += 1                                                              # comparisons
        mid = (begin + end) // 2
        mergeSort(arr, begin, mid)
        mergeSort(arr, mid + 1, end)

        merge(arr, begin, mid, end)
        drawNums()
    drawNums() 

# wrapper function to print to console when mergeSort is finished
def mergeSortWrap(arr, begin, end):
    global comps
    mergeSort(arr, begin, end)
    if arr == sortedVals:
        print("mergeSort complete")
        print("Comparisons: ", comps)

def changesize():
    global numBars
    popUp = Toplevel(root)
    

topnav = Menu(root)
options = Menu(topnav)
options.add_command(label="change array size", command=changesize)

# frame for buttons
bFrame = Frame(root, background="#000034", highlightbackground="#2e294e", highlightthickness=4, relief="ridge", pady=5, padx=20)
bFrame.grid(row=2)

# sorting buttons
sortFrame = Frame(bFrame, pady=5, background="#000034")
sortFrame.grid(row=0)
bubble = Button(sortFrame, bg="#be97c6", text="Bubble", command=lambda: (bubbleSort(vals)))
bubble.grid(row=0, column=0, padx=5)
selection = Button(sortFrame, bg="#be97c6", text="Selection", command=lambda: (selectionSort(end)))
selection.grid(row=0, column=1, padx=5)
mergeButton = Button(sortFrame, bg="#be97c6", text="Merge", command=lambda: (mergeSortWrap(vals, 0, len(vals)-1)))
mergeButton.grid(row=0, column=2, padx=5)
mystery = Button(sortFrame,bg="#be97c6", text="Mystery", command=lambda: (unknownSort(end)))
mystery.grid(row=0, column=3, padx=5)

# utility buttons
midFrame = Frame(bFrame, pady=5, background="#000034")
midFrame.grid(row=1)
backwards = Button(midFrame, bg="#be97c6", text="reverse", command=lambda: (reverse(0, end)))
backwards.grid(row=0, column=0, padx=5)
p = Button(midFrame, bg="#be97c6", text="print", command=lambda: (print(vals)))
p.grid(row=0, column=1, padx=5)
genNums = Button(midFrame, bg="#be97c6", text="Create New Array", command=lambda:(makeNewVals(numBars)))
genNums.grid(row=0, column=2, padx=5)


if __name__ == "__main__":
    root.mainloop()