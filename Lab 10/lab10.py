"""
    Author: Kaitlyn Clements
    KUID: 3072622
    Lab: 10- Sorting Algorithms
"""

# A. Implementation of Sorting Algorithms
# Following skeleton implements constructors for "HashMap". Note tat each value is inserted as a set of
# (key, value) in the hash bucket calculated based on key. 
from random import randint, seed
import time

class Sorting:
    def __init__(self, size):
        self.arr = []  # Initialize an empty list
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")
    # A.1 Implement Selection Sort
    def selection_sort(self): 
        """Implements selection sort"""
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        
    # A.2 Implement Heap Sort
    def max_heapify(self, n, i):
        """Implements Heapify for array"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(n, largest)
    
    def build_max_heap(self):
        n = len(self.arr)
        for i in range(n //2 -1, -1, -1):
            self.max_heapify(n, i)
        
    def heap_sort(self):
        " ""Implements Heap sort"""
        n = len(self.arr)
        self.build_max_heap()
        for i in range(n-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.max_heapify(i, 0)
        
    # A.3 Implement Merge Sort
    # When dealing with an array of an odd number of elements in the merge sort algorithm, calculate the 
    # middle index by taking the floor of the array length divided by 2
    def merge_sort(self):
        """Implements Merge sort"""
        if len(self.arr) > 1:
            mid = len(self.arr) // 2
            left_half = self.arr[:mid]
            right_half = self.arr[mid:]
            
            left_sorting = Sorting(len(left_half))
            right_sorting = Sorting(len(right_half))
            
            left_sorting.arr = left_half
            right_sorting.arr = right_half
            
            left_sorting.merge_sort()
            right_sorting.merge_sort()
            
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    self.arr[k] = left_half[i]
                    i += 1
                else:
                    self.arr[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                self.arr[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                self.arr[k] = right_half[j]
                j += 1
                k += 1

# B. Runtime Analysis of each sorting algorithms
    # B.1 Record the time taken
    # Record time taken for each sorting algorithm implemented for array
    def test_sorting_time(self, sorting_method): # -> Time
        start_time = time.time()
        
        if sorting_method == 'selection':
            self.selection_sort()
        elif sorting_method == 'heap':
            self.heap_sort()
        elif sorting_method == 'merge':
            self.merge_sort()
            
        end_time = time.time()
        return end_time - start_time
# B.2 Runtime complexity of each sorting algorithms
# Different sorting algorithms have different time complexities based on how they work. 
# Selection Sort: O(n^2) - Quadratic time complexity
# Heap sort: O(n log n) - Log-linear time complexity
# Merge sort: O(n log n) - Log-linear time complexity


#Testing Logic
#Test Sorted array
def is_sorted(arr):
    if arr == sorted(arr):
        print("Passed!")
    else:
        print("Failed!")
    return arr == sorted(arr)

# Test each sorting technique
def test_sort_algorithms(sorting_method, set_seed=None):
    if seed is not None:
        seed(set_seed)
    sorting = Sorting(10)
    # Add 10 random elements
    for _ in range(10):
        sorting.add(randint(1, 100))
    # Apply the sorting algorithm
    if sorting_method == 'selection':
        sorting.selection_sort()
        print("Selection Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'heap':
        sorting.heap_sort()
        print("Heap Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'merge':
        sorting.merge_sort()
        print("Merge Sort:", is_sorted(sorting.arr))
        
#Test run time
def run_time_tests():
    seeding = 45
    array_sizes = [10000,20000,30000,40000,50000]
    methods = ['selection', 'heap', 'merge']
    print("Array Size\t\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
    for size in array_sizes: 
        times = []
        for m in methods:
            sorting = Sorting(size)
            seed(seeding)
            for _ in range(size):
                sorting.add(randint(1, 50000))
            interval = sorting.test_sorting_time(m)
            times.append(interval)
        print(f"{size}\t\t{times[0]:.6f}\t\t{times[1]:.6f}\t\t{times[2]:.6f}")
        
#test case execution
seed_num = 43   
test_sort_algorithms('selection', seed_num)
test_sort_algorithms('heap', seed_num)
test_sort_algorithms('merge', seed_num)
run_time_tests()