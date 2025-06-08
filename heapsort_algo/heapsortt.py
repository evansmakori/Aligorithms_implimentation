# Heapsort implementation in Python
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def siftdown(lst, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if l < upper:
            if r < upper and lst[r] > lst[l]:
                max_child = r
            else:
                max_child = l
            if lst[i] < lst[max_child]:
                swap(lst, i, max_child)
                i = max_child
            else:
                break
        else:
            break

def heapsort(lst):
    n = len(lst)
    for j in range(n // 2 - 1, -1, -1):
        siftdown(lst, j, n)
    for i in range(n - 1, 0, -1):
        swap(lst, 0, i)
        siftdown(lst, 0, i)

lst = [i for i in range(100, -1, -1)]
heapsort(lst)
print(lst)
