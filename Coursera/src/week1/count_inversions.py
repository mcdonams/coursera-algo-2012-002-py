'''
Created on Jun 29, 2012

@author: mmcdonald
'''
def count_inversions(source):
    if len(source) <= 1:
        return 0, source
    
    mid = len(source) // 2
    left = source[:mid]
    right = source[mid:]
    
    countLeft, left = count_inversions(left)
    countRight, right = count_inversions(right)
    
    countMerged, merged = merge_and_count(left, right)
    
    return countLeft + countRight + countMerged, merged

def merge_and_count(left, right):
    merged = []
    i, j = 0, 0
    count = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    
    while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
               
    return count, merged

def main():
    integers = []    
    f = open("files//IntegerArray_100k.txt", "r")
    
    for line in f.readlines():
        integers.append(int(line.rstrip("\n")))
    
    f.close
    
    inversions = count_inversions(integers)[0]
    print(inversions) #2407905288

if __name__ == '__main__':
    main()