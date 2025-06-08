def heapify(arr, n, i):
    """
    Maintain heap property for a subtree rooted at index i
    n is size of heap
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left child
    right = 2 * i + 2    # right child
    
    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def build_max_heap(arr):
    """Build a max heap from an unsorted array"""
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr

def heap_sort(arr):
    """Main heap sort function"""
    n = len(arr)
    
    # Step 1: Build max heap
    print("Original array:", arr)
    build_max_heap(arr)
    print("After building max heap:", arr)
    
    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        print(f"After moving max element {arr[i]} to position {i}:", arr[:i+1])
        
        # Call heapify on the reduced heap
        heapify(arr, i, 0)
        print(f"After heapifying remaining elements:", arr[:i])
    
    return arr

# Step-by-step demonstration
def demonstrate_heap_sort():
    """Demonstrate heap sort with the original input"""
    # Original input from the screenshot
    input_array = [71, 15, 36, 57, 101]
    
    print("=== HEAP SORT STEP-BY-STEP DEMONSTRATION ===\n")
    
    # Make a copy to avoid modifying original
    arr = input_array.copy()
    
    print("Step 1: Understanding the input")
    print(f"Input array: {input_array}")
    print(f"Array length: {len(input_array)}")
    print()
    
    print("Step 2: Building Max Heap")
    print("We start from the last non-leaf node and heapify upwards")
    n = len(arr)
    print(f"Last non-leaf node index: {n // 2 - 1}")
    
    # Build heap step by step
    for i in range(n // 2 - 1, -1, -1):
        print(f"Heapifying at index {i} (value: {arr[i]})")
        heapify(arr, n, i)
        print(f"Array after heapifying index {i}: {arr}")
    
    print(f"\nMax heap built: {arr}")
    print("(Root is the maximum element)")
    print()
    
    print("Step 3: Sorting by extracting maximum elements")
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        print(f"\nIteration {n-i}:")
        print(f"Current heap: {arr[:i+1]}")
        print(f"Moving max element {arr[0]} to position {i}")
        
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        print(f"After swap: {arr}")
        
        # Heapify the reduced heap
        heapify(arr, i, 0)
        print(f"After heapifying remaining {i} elements: {arr[:i]}")
        print(f"Sorted portion: {arr[i:]}")
    
    print(f"\nFinal sorted array: {arr}")
    return arr

# Run the demonstration
if __name__ == "__main__":
    demonstrate_heap_sort()
    
    print("\n" + "="*50)
    print("TESTING WITH OTHER EXAMPLES:")
    print("="*50)
    
    # Test with other arrays
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [3, 3, 3, 3]
    ]
    
    for test_arr in test_arrays:
        original = test_arr.copy()
        sorted_arr = heap_sort(test_arr)
        print(f"Original: {original} → Sorted: {sorted_arr}")
        print()