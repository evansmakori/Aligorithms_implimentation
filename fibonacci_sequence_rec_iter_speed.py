# To see the time taken for te iteration and recursion
import time

#recursion for Fibonacci sequence
def Fibonacci(idx):
    if idx<=1:
        return idx
    
    else:
        return Fibonacci(idx-1)+Fibonacci(idx-2)
    
#iterations for the same game to see which one is efficient

def fibonacci(idx):
    seq=[0,1]
    for i in range (idx):
        seq.append(seq[-1]+seq[-2])
    return [-2]



#Function calls for both Function
print("*****Recursion*****")
rec=time.time()
print (Fibonacci(8))
print ("speed: " + str(time.time()-rec))
print()
print("*****Iteration*****")
Itr=time.time()
print (Fibonacci(8))
print ("speed: " + str(time.time()-Itr))
print (fibonacci(8))