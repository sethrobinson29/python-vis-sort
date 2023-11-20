from graphics import *

# swap function
def swapVals(arr, i, j):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp

class Sorter():
    def __init__(self, root, arr=[]):
        self.root = root
        self.canvas = Canvas(root, height=550, width=1015,highlightbackground="#2e294e", highlightthickness=2, background="#000034")
        self.vals = arr
        self.sortedVals = sorted(arr)
        self.numBars = len(arr)
        self.comps = 0

    # set up object for sorting
    def makeNewVals(self, length):
        self.numBars = length 
        self.vals = [i for i in range(length)]
        shuffle(self.vals)
        self.sortedVals = sorted(self.vals)
        self.canvascomps = 0
        self.drawNums()

    # draw 
    def drawNums(self):
        self.canvas.delete('all')
        x, y, = 10, 500
        
        for i in range(self.numBars):
            y -= self.vals[i]
            tmp = Bar(self.vals[i], 575-y, 1)
            tmp.drawBar(self.canvas, Point(x, y))
            x += (1000 / self.numBars)
            y = 500
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
        self.comps = 0                                                                       # comparisons
        stop = self.numBars
        for i in range(stop-1):
            for j in range(stop-i-1):
                self.comps += 1                                                              # comparisons
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
                self.comps += 1                                                              # comparisons
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
                self.comps += 1                                                              # comparisons
                tmp.append(self.vals[x])
                x += 1
            else:
                self.comps += 1                                                              # comparisons
                tmp.append(self.vals[y])
                y += 1
        
        for i in range(len(tmp)):
            self.vals[begin] = tmp[i]
            begin += 1

    def mergeSort(self, begin, end):
        if begin < end:
            mid = (begin + end) // 2
            self.mergeSort(begin, mid)
            self.mergeSort(mid + 1, end)

            self.merge(begin, mid, end)
            self.drawNums()
        self.drawNums() 

    # wrapper function to print to console when mergeSort is finished
    def mergeSortWrap(self):
        self.comps = 0
        begin, end = 0, self.numBars-1
        self.mergeSort(begin, end)

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


    def radixSort(self):
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
