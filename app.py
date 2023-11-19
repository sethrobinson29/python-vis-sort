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
    compsDisplay.config(text=comps)
    drawNums()
    # print(vals)

# draws bars representing array on screen; ONLY CALL AFTER/DURING makeNewVals
def drawNums():
    can.delete('all')
    x, y, = 10, 500
    
    for i in range(end + 1):
        # y -= (vals[i]*2)
        y -= vals[i]
        tmp = Bar(vals[i], 550-y, (numBars // 1000) + 1)
        tmp.drawBar(can, Point(x, y))
        # playSound()
        x += (1000 // numBars)
        y = 500

    root.update_idletasks()

def swapVals(arr, i, j):
    tmp = vals[j]
    arr[j] = arr[i]
    arr[i] = tmp

# reverses array
def reverse(i, j):
    if i < j:
        swapVals(vals, i, j)
        drawNums()
        i += 1
        j -= 1
        reverse(i, j)

# recursively bubble sort array; stop used to not iterated over previously sorted array. 
def bubbleSort(arr):
    global comps
    comps = 0                                                                       # comparisons
    stop = len(arr)
    for i in range(stop-1):
        for j in range(stop-i-1):
            comps += 1                                                              # comparisons
            if arr[j] > arr[j+1]:
                drawNums()
                swapVals(vals, j, j+1)
    # print("bubbleSort complete")
    compsDisplay.config(text=comps)
    drawNums()


# recursively select the largest element of the remaining unsorted array and move it to the correct position
def selectionSort(stop):
    global comps
    comps = 0
    for i in range(stop):
        for j in range(i+1, stop+1):
            comps += 1                                                              # comparisons
            if vals[i] > vals[j]:
                swapVals(vals, i, j)
                drawNums()
    drawNums()
    # print("selectionSort complete")
    # print("Comparisons: ", comps)
    compsDisplay.config(text=comps)

# recursive selection sort
# def unknownSort(stop):
#     global comps
#     comps = 0
#     curMax = -999
#     swapIndex = -1
#     for i in range(stop+1):
#         comps += 1                                                              # comparisons
#         if vals[i] > curMax:
#             curMax = vals[i]
#             swapIndex = i
#             # swapVals(vals, i, stop)
#             # drawNums()
#     swapVals(vals, swapIndex, stop)
#     drawNums()
#     if stop > 0:
#         unknownSort(stop-1)
#     else:
#         print("unknownSort complete")
#         print("Comparisons: ", comps)


# radix and counting sort code from https://www.geeksforgeeks.org/radix-sort/
def countingSort(arr, exp1):
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        drawNums()
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
    drawNums()

# merge sorted sections from merge sort
def merge(arr, begin, mid, end):
    global comps
    x, y = begin, mid + 1
    tmp = []

    for i in range(begin, end+1):
        
        if x > mid:
            tmp.append(arr[y])
            y += 1
        elif y > end:
            tmp.append(arr[x])
            x += 1
        elif arr[x] < arr[y]:
            comps += 1                                                              # comparisons
            tmp.append(arr[x])
            x += 1
        else:
            comps += 1                                                              # comparisons
            tmp.append(arr[y])
            y += 1
    
    for i in range(len(tmp)):
        arr[begin] = tmp[i]
        begin += 1

def mergeSort(arr, begin, end):
    if begin < end:
        mid = (begin + end) // 2
        mergeSort(arr, begin, mid)
        mergeSort(arr, mid + 1, end)

        merge(arr, begin, mid, end)
        drawNums()
    drawNums() 

# wrapper function to print to console when mergeSort is finished
def mergeSortWrap(arr, begin, end):
    global comps
    comps = 0
    mergeSort(arr, begin, end)
    if arr == sortedVals:
        # print("mergeSort complete")
        # print("Comparisons: ", comps)
        compsDisplay.config(text=comps)

def changesize():
    global numBars
    popUp = Toplevel(root)
    

topnav = Menu(root)
options = Menu(topnav, tearoff=0)
topnav.add_cascade(label="options", menu=options)
options.add_command(label="change array size", command=changesize)
root.config(menu=topnav)

# lowFrame = Frame(root, background="#000034", highlightbackground="#2e294e", highlightthickness=4, relief="ridge", pady=5, padx=20) #297373
lowFrame = Frame(root, background="#297373", pady=5, padx=20)
lowFrame.grid(row=2)

compFrame = Frame(lowFrame, background="#000034", highlightbackground="#2e294e", highlightthickness=4, relief="ridge", pady=5, padx=20)
compFrame.grid(row=0, column=0)
compsLabel = Label(compFrame, text="Comparisons: ", background="#be97c6")
compsLabel.grid(row=0, column=0)
compsDisplay = Label(compFrame, text="0", background="#be97c6")
compsDisplay.grid(row=0, column=1)

lowFrameSpace1 = Label(lowFrame, background="#297373", padx=10, text=" ")
lowFrameSpace1.grid(row=0, column=1)

# frame for buttons
bFrame = Frame(lowFrame, background="#000034", highlightbackground="#2e294e", highlightthickness=4, relief="ridge", pady=5, padx=20)
bFrame.grid(row=0, column=2)

# sorting buttons
sortFrame = Frame(bFrame, pady=5, background="#000034")
sortFrame.grid(row=0)
bubble = Button(sortFrame, bg="#be97c6", text="Bubble", command=lambda: (bubbleSort(vals)))
bubble.grid(row=0, column=0, padx=5)
selection = Button(sortFrame, bg="#be97c6", text="Selection", command=lambda: (selectionSort(end)))
selection.grid(row=0, column=1, padx=5)
mergeButton = Button(sortFrame, bg="#be97c6", text="Merge", command=lambda: (mergeSortWrap(vals, 0, len(vals)-1)))
mergeButton.grid(row=0, column=2, padx=5)
radix = Button(sortFrame,bg="#be97c6", text="Radix", command=lambda: (radixSort(vals)))
radix.grid(row=0, column=3, padx=5)

# utility buttons
midFrame = Frame(bFrame, pady=5, background="#000034")
midFrame.grid(row=1)
backwards = Button(midFrame, bg="#be97c6", text="reverse", command=lambda: (reverse(0, end)))
backwards.grid(row=0, column=1, padx=5)
# p = Button(midFrame, bg="#be97c6", text="print", command=lambda: (print(vals)))
# p.grid(row=0, column=1, padx=5)
genNums = Button(midFrame, bg="#be97c6", text="Create New Array", command=lambda:(makeNewVals(numBars)))
genNums.grid(row=0, column=0, padx=5)
closeProgram = Button(midFrame, bg="#be97c6", fg="#f31227", text="Quit", command=root.destroy)
closeProgram.grid(row=0,  column=2, padx=5)


# initialize number of bars and array
numBars = 200
makeNewVals(numBars)

if __name__ == "__main__":
    root.mainloop()
