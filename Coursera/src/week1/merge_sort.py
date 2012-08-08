'''
Created on Jun 29, 2012

@author: mmcdonald
'''
def merge_sort(toSort):
    if len(toSort) <= 1:
        return toSort
    
    mid = len(toSort) // 2
    left = toSort[:mid]
    right = toSort[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1  
    
    while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
               
    return merged  

def main():
    pass

if __name__ == '__main__':
    main()