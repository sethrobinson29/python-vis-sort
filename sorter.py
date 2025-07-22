# Class for animating sorting algorithms
# By Seth Robinson https://github.com/sethrobinson29 
# radix and counting sort code originally from https://www.geeksforgeeks.org/radix-sort/
from tkinter import *
from random import shuffle

# swap function
def swapVals(arr, i, j):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp

# colors for drawing values
# colors = [ "#A18DCE", "#AA8ED2", "#B38ED6", "#BD8FD9", "#C68FDD", "#CF90E1", "#D890E5", "#E291E8", "#EB91EC", "#F492F0" ]
colors = [ "#A8F368", "#B1D867", "#BABE66", "#C3A365", "#CC8864", "#D56E62", "#DE5361", "#E73860", "#F01E5F", "#F9035E" ]
colors.reverse()

# class for array, canvas, and sorting 
class Sorter():
    def __init__(self, root, arr=[]):
        self.root = root
        self.canvas = Canvas(root, height=550, width=1015,highlightbackground="#2e294e", highlightthickness=2, background="#000034")
        self.vals = arr
        self.sortedVals = self.vals
        self.numBars = len(arr)
        self.comps = 0

    # set up object for sorting, accepts int parameter 
    def makeNewVals(self, length):
        self.numBars = length 
        self.vals = [i for i in range(length)]
        self.sortedVals = self.vals
        shuffle(self.vals)
        self.canvascomps = 0
        self.drawNums()

    # draw self.vals
    def drawNums(self):
        self.canvas.delete('all')
        x, y, = 10, 0

        for i in range(self.numBars):
            color = (self.vals[i] % 100) // 10 if self.vals[i] > 9 else 0           # repeat gradient every 100 
            y = self.vals[i]
            self.canvas.create_line(x, 550, x, 550-y, fill=colors[color], width=1)

            x += (1000 / self.numBars)
            # y = 550
        self.root.update_idletasks()
    
    # reverses array
    def reverse(self):
        i, j = 0, self.numBars-1
        while i < j:
            swapVals(self.vals, i, j)
            self.drawNums()
            i += 1
            j -= 1

    # recursively bubble sort array; stop used to not iterated over previously sorted array. 
    def bubbleSort(self):
        self.comps = 0                                                                       
        stop = self.numBars
        for i in range(stop-1):
            for j in range(stop-i-1):
                self.comps += 1                                                              
                if self.vals[j] > self.vals[j+1]:
                    self.drawNums()
                    swapVals(self.vals, j, j+1)
        # print("bubbleSort complete")
        self.drawNums()

    # recursively select the largest element of the remaining unsorted array and move it to the correct position
    def selectionSort(self):
        stop = self.numBars
        self.comps = 0
        for i in range(stop-1):
            for j in range(i+1, stop):
                self.comps += 1                                                           
                if self.vals[i] > self.vals[j]:
                    swapVals(self.vals, i, j)
                    self.drawNums()
        self.drawNums()
        # print("selectionSort complete")

    # merge sorted sections from merge sort
    def merge(self, begin, mid, end):
        x, y = begin, mid + 1
        tmp = []

        for i in range(begin, end+1):
            
            if x > mid:
                tmp.append(self.vals[y])
                y += 1
            elif y > end:
                tmp.append(self.vals[x])
                x += 1
            elif self.vals[x] < self.vals[y]:
                self.comps += 1                                                           
                tmp.append(self.vals[x])
                x += 1
            else:
                self.comps += 1                                                        
                tmp.append(self.vals[y])
                y += 1
        
        for i in range(len(tmp)):
            self.vals[begin] = tmp[i]
            begin += 1

    # recursive mergesort 
    def mergeSort(self, begin, end):
        if begin < end:
            mid = (begin + end) // 2
            self.mergeSort(begin, mid)
            self.mergeSort(mid + 1, end)

            self.merge(begin, mid, end)
            self.drawNums()
        self.drawNums() 

    # wrapper function to handle mergesort
    def mergeSortWrap(self):
        self.comps = 0
        begin, end = 0, self.numBars-1
        self.mergeSort(begin, end)

    # partition array for quicksort
    def partition(self, left, right):
        pivot = self.vals[right]
        i = left-1

        for j in range(left, right):
            self.comps += 1
            if self.vals[j] <= pivot:
                i += 1
                swapVals(self.vals, i, j)
                self.drawNums()
        swapVals(self.vals, i+1, right)
        self.drawNums()
        
        return i+1

    # recursive quicksort
    def quicksort(self, begin, end):
        if begin < end:
            pivot = self.partition(begin, end)
            self.quicksort(begin, pivot-1)
            self.quicksort(pivot+1, end)

    # wrapper function to handle quicksort
    def quickSortWrap(self):
        self.comps = 0
        left, right = 0, self.numBars-1
        self.quicksort(left, right)
        self.drawNums()

    # based on example found at https://www.cs.uah.edu/~rcoleman/CS221/Sorting/ProxMapSort.html
    def proxMapSort(self, data1: dict, count: int) -> None:
        result = {}
        hits, proxMap, location = [], [], []
        hIndex, curTotal = 0, 0
        keyMin, keyMax = 0, 32767

        # initializing
        for i in range(count):
            hits[i] = 0
            proxMap[i] = -1
            result[i].key = -1

        # find mix and max
        for i in range(count):
            if data1[i].key > keyMax:
                keyMax = data1[i].key
            if data1[i].key < keyMin:
                keyMin = data1[i].key

        # compute hits; hits = number of collisions + 1
        for i in range(count):
            hIndex = self.calculateHash(data1[i].key, keyMin, keyMax, count)
            location[i] = hIndex
            hits[hIndex] += 1

        # create proximity map
        for i in range(count):
            if hits[i] > 0:
                proxMap[i] = curTotal
                curTotal += hits[i]


        for i in range(count):
            if result[proxMap[location[i]]].key == -1:
                result[proxMap[location[i]]] = data1[i]
            else:
                self.mapInsertionSort()

    def calculateHash(self, key: int, keyMin: int, keyMax: int, count: int) -> int:
        # todo: implement
        pass

    def mapInsertionSort(self):
        #todo: translate example into correct function signature
        pass

    # radix and counting sort code originally from https://www.geeksforgeeks.org/radix-sort/
    def countingSort(self, exp1):
        n = self.numBars
    
        # The output array elements that will have sorted arr
        output = [0] * (n)
    
        # initialize count array as 0
        count = [0] * (10)
    
        # Store count of occurrences in count[]
        for i in range(0, n):
            index = self.vals[i] // exp1
            count[index % 10] += 1
    
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            self.drawNums()
            count[i] += count[i - 1]
    
        # Build the output array
        i = n - 1
        while i >= 0:
            index = self.vals[i] // exp1
            output[count[index % 10] - 1] = self.vals[i]
            count[index % 10] -= 1
            i -= 1
    
        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, n):
            self.vals[i] = output[i]

    # radix and counting sort code originally from https://www.geeksforgeeks.org/radix-sort/
    def radixSort(self):
        self.comps = 0
        # Find the maximum number to know number of digits
        max1 = max(self.vals)
    
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp >= 1:
            self.countingSort(exp)
            exp *= 10
        self.drawNums()
