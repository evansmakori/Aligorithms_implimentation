# Data Structures and Algorithms
This repository contains implementations of various algorithms, data structures, and utility scripts. Explore the folders for more details.

### A Recursive Algorithm 
**Algorithmically:** A way to design solutions to problems by **devide-and-conquer**  or **decrease-and-conquer**
**Semantically:** A recursive function breaks the problem down into smaller problems, and calls itself for each of the smaller problems. 
It usually includes 1 or more base case or terminal case and a recursive case.

*For more about recursion and dictionaries, check out MIT: https://www.youtube.com/watch?v=WPSeyjX1-4s* 

*Lets try print the ^2 of a number that exists between 1-1000, if the number does not exists, it should print "pick another num," otherwise it should print out the results.*

<pre> <code> '''python
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
print(results)'''</code> </pre>
     
Pro: 
- In some cases, its extremely fast and easy to code. 
- Practical for tree traversals and binary search aligorithm
Link: https://github.com/evansmakori/Aligorithms_implimentation/blob/main/aligorithms/recursive_binary_search.py

Con: 
- Require more memory, and does not scale up like iterations. 
Link:https://github.com/evansmakori/Aligorithms_implimentation/blob/main/fibonacci_sequence_rec_iter_speed.py

- Sometimes more abstract or harder to understand than iterative solutions.
