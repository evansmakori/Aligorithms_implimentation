import time

def recursive_fact(n):
    if n<0:
        return -1
    elif n<2:
        return 1
    else:
        return n* recursive_fact(n-1)
    
def iteration_fact(n):
    if n<0:
        return -1
    else:
        fact=1
        for i in range (1, n+1):
            fact *= i
        return fact
print("***Recursive***")
rec=time.time()
print(recursive_fact(6))
print("Speed:" + str(time.time()-rec))
print()
print("***Iteration***")
itr=time.time()
print(iteration_fact(6))
print("Speed:" + str(time.time()-itr))