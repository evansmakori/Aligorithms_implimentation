from unittest import result


def linear_search(list, target):
    #returns the index position of the target if found, else returns None
    for i in range(0, len(list)):
                if list[i] ==target:
                    return i

def verify(index):
    if index is not None:
        print("Target Found at index: ", index)
    else:
        print("Target not found in list")
        
numbers=[2,4,5,1, 3,6,7,8,9,10,11]
result=linear_search(numbers, 8)
verify(result)

result=linear_search(numbers, 2)
verify(result)