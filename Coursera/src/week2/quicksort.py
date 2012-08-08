'''
Created on Jul 18, 2012

@author: mmcdonald
'''
pivotMode = 1
totalComparisons = 0

def quicksort(toSort, left = 0, right = None):
    if len(toSort) <= 1:
        return toSort
    
    if (right is None):
        right = len(toSort) - 1
        
    if (left < right):
        pivotIndex = partition(toSort, left, right)
        quicksort(toSort, left, pivotIndex - 1)
        quicksort(toSort, pivotIndex + 1, right)

def partition(inputArray, left, right):
    pivotIndex = get_pivot_index(inputArray, left, right)
    pivotElement = inputArray[pivotIndex]
    
    i = left + 1
    j = left + 1
    
    while (j <= right):
        if (inputArray[j] < pivotElement):    
            temp = inputArray[i]
            inputArray[i] = inputArray[j]
            inputArray[j] = temp
            i += 1
        
        j += 1
    
    inputArray[left] = inputArray[i - 1]
    inputArray[i - 1] = pivotElement
    
    global totalComparisons
    totalComparisons += right - left
    
    return i - 1

def get_pivot_index(inputArray, left, right):
    """
    Helper method to compute the pivot index for each run of the partition method.
    
    The programming assignment calls for 3 distinct ways to determine the pivot:
    1) First element of the input array (left)
    2) The last element of the input array (right)
    3) Use the "median-of-three" rule.  That is, the median of the first, middle, and last elements.
    
    Note: the pivot element is always swapped to the first spot in the array, per
    instructions provided in the assignment.
    """
    
    if pivotMode == 2:
        # Swap first and last element, pivot should always be the first element
        temp = inputArray[left]
        inputArray[left] = inputArray[right]
        inputArray[right] = temp
    elif pivotMode == 3:
        # Compute index of median element
        mid = left + ((right - left + 1) // 2)
        if ((right - left + 1) % 2 == 0):
            mid -= 1 # Per assignment instructions
        
        options = {left: inputArray[left], right: inputArray[right], mid: inputArray[mid]}
        sortedOptions = sorted(options, key = lambda x: options[x])
        pivotIndex = sortedOptions[1]
        
        # Swap elements to get pivot in the first position
        if (pivotIndex != left):
            temp = inputArray[left]
            inputArray[left] = inputArray[pivotIndex]
            inputArray[pivotIndex] = temp

    # Pivot is always in the the leftmost position
    return left
    
def main():
    integers = []
    f = open("files//Quicksort_10k.txt", "r")
    
    for line in f.readlines():
        integers.append(int(line.rstrip("\n")))
    
    f.close
    
    quicksort(integers)
    print(totalComparisons)

if __name__ == '__main__':
    main()