# Aligorithms_implementation

This repository contains implementations of various algorithms, data structures, and utility scripts (such as files_to_folder_organizer.py). Explore the folders for more details.
### A Recursive Aligorithm 
A recursive function breaks the problem down into smaller problems, and calls itself for each of the smaller problems. 
It usually includes a base case or terminal case and a recursive case. 
****Lets try print the ^2 of a number that exists between 1-1000, if the number does not exists, it should print "pick another num"
otherwise it should print out the results.



Pro: 
- In some cases, its extremely fast and easy to code. 
- Practical for tree traversals and binary search aligorithm
Link: https://github.com/evansmakori/Aligorithms_implimentation/blob/main/aligorithms/recursive_binary_search.py

def fact_three(nums):
    results=[]
    for num in nums:
        if num in range(1,1000):
            print(num)
            results.append(num**2)
            
        else:
            print("Pick another num")
    return results
        
        
results=fact_three([5,2222, 44])
print(results)


CON1: Require more memory, and does not scale up like iterations. 
Link:https://github.com/evansmakori/Aligorithms_implimentation/blob/main/fibonacci_sequence_rec_iter_speed.py

CON2: Sometimes more abstract or harder to understand than iterative solutions.
