def merge_sort(list_to_sort): # Renamed 'list' to 'list_to_sort' to avoid shadowing built-in 'list'
    # Sorts a list in ascending order and returns a new sorted list.
    # Divide: find the midpoint of the list and divide into sublists.
    # Conquer: Recursively sort the sublist created in previous step.
    # Combine: Merge the sorted sublists created in previous step.
    
    if len(list_to_sort) <= 1:
        return list_to_sort
    
    left_half, right_half = split(list_to_sort)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)


def split(list_to_split): # Renamed 'list' to 'list_to_split'
    # Divide unsorted list into sublists at midpoint. Returns two sublists-left and right.
    
    mid = len(list_to_split) // 2
    left = list_to_split[:mid]
    right = list_to_split[mid:]
    
    return left, right

def merge(left, right):
    # Merges two lists (arrays), sorting them in the process
    
    L = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L.append(left[i])
            i += 1
        else:
            L.append(right[j])
            j += 1
            
    while i < len(left):
        L.append(left[i])
        i += 1
        
    while j < len(right): 
        L.append(right[j])
        j += 1
        
    return L

def verify(sorted):
    n=len(list)
    
    
    if n==0 or n==1:
        return True
    return list[0]< list[1] and verify.sorted(list[1:])


alist = [54, 32, 46, 78, 12, 34, 67, 89, 234, 21, 256]
l = merge_sort(alist)
print(l)