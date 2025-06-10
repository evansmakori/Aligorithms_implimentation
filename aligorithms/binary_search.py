def binary_search(list, target):
    first=0
    last=len(list)-1
    
    while first<=last:
        midpoint=(first+last)//2 
        if list [midpoint]==target:
            return midpoint
        elif list [midpoint]<target:
            first=midpoint+1
        else:
            last=midpoint-1
            

    return None        
def verify(index):
    if index is not None:
        print("Target Found at index: ", index)
    else:
        print("Target not found in list")
        
numbers=[2,4,5,1, 3,6,7,8,9,10,11]
result=binary_search(numbers, 8)
verify(result)

result=binary_search(numbers, 2)
verify(result)