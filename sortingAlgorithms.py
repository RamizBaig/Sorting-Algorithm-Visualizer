def bubbleSort(array):
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - i - 1):
            yield array
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    yield array
                
def selectionSort(array):
    for i in range(len(array) - 1):
        minIndex = i
        for j in range(i + 1, len(array)):
            yield array  
            if array[j] < array[minIndex]:
                minIndex = j
        if minIndex != i:
            array[i], array[minIndex] = array[minIndex], array[i]
    yield array
                
def insertionSort(array):
    for i in range(1, len(array)):
        insertElement = array[i]
        j = i - 1
        while j >= 0:
            yield array
            if array[j] > insertElement:
                array[j + 1] = array[j]
                j -= 1
            else:
                break
        array[j + 1] = insertElement
    yield array
    
def quickSort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivotIndex = high
        pivot = array[pivotIndex]
        ppvt = low

        for i in range(low, high):
            yield array  
            if array[i] < pivot:
                array[i], array[ppvt] = array[ppvt], array[i]  
                ppvt += 1

        array[ppvt], array[pivotIndex] = array[pivotIndex], array[ppvt] 

        yield from quickSort(array, low, ppvt - 1)
        yield from quickSort(array, ppvt + 1, high)
    yield array