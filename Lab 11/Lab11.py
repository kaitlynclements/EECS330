"""
Author: Kaitlyn Clements
KUID: 3072622
Lab: 11- Advanced Sorting
"""

# A. Quick Sort
# Quicksort is an efficient divide-and-conquer sorting algorithm that selects a pivot element, 
# partitions the array into sub-arrays of elements less than and greater than this pivot, 
# and then recursively sorts these partitions. Its average-case time complexity is O(n log n), 
# making it one of the fastest sorting algorithms for large datasets. However, its worst-case 
# complexity can reach O(n^2), particularly with poorly chosen pivot elements.

# Implementation of Sorting Algorithm
# Following skeleton implements constructors for "HashMap". Note that each value is inserted as
# a set of (key, value) in the hash bucket calculated based on key.
# importing necessary modules
from random import randint, seed
import time

# Sorting class
class Sorting:
    # initialization of class
    def __init__(self, size):
        self.arr = []  # Initialize an empty list
        self.size = size

    # add method for Sorting class
    def add(self, element):
        if len(self.arr) < self.size: 
            # comparing length of the array to the size. If it's less than, then execute the code below
            self.arr.append(element) 
            # append the element to the array
        else: # otherwise:
            print("Array is already full, cannot add more elements.") 
            # the array is full so the element could not be added 

    # Implement Quick Sort
    # Implement the Quicksort algorithm focusing on the in-place partitioning process
    # (In-place partitioning means rearranging the elements within the array itself, 
    # without the need for additional memory space for another array structure).
    # Quicksort method for Sorting class
    def quicksort(self, low, high):
        if low < high: # if the low parameter is less than the high parameter, execute the code below: 
            pi = self.partition(low, high)  # Partitioning index
            self.quicksort(low, pi - 1)  # Recursively sort elements before partition
            self.quicksort(pi + 1, high)  # Recursively sort elements after partition

    # partition method for Sorting class
    def partition(self, low, high):
        """
        Implements in-place partitioning around a pivot.
        Elements less than the pivot are moved to its left, and greater to its right.
        The pivot is chosen using the median_of_three method.
        It is crucial to rearrange the elements within the array itself,
        avoiding the use of additional arrays or significant extra space.
        low : Starting index, high : Ending index
        Returns the partitioning index.
        """
        p_index = self.median_of_three(low, high) # assign the pivot index to the median of three given low and high
        p_value = self.arr[p_index] # assign the pivot value
        #Move the pivot to the end
        self.arr[p_index], self.arr[high] = self.arr[high], self.arr[p_index] 
        i = low-1
        for j in range(low, high):
            if self.arr[j] < p_value:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        # move the pivot to its final position
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        return i+1

    def median_of_three(self, low, high):
        """
        Selects the median of the first, middle, and last elements as the pivot.
        This method is used to improve performance by avoiding worst-case scenarios.
        low : Starting index, high : Ending index
        Returns the index of the median element.
        """
        mid = (low+high)//2 # middle
        #compare arr[low], arr[mid], arr[high] and return the middle index
        if self.arr[low] < self.arr[mid]: #array low compared to array mid
            if self.arr[mid] < self.arr[high]: # array mid compared to array high
                return mid
            elif self.arr[low] < self.arr[high]: # array low compared to array high
                return high
            else:
                return low
        else:
            if self.arr[low] < self.arr[high]:
                return low
            elif self.arr[mid] < self.arr[high]:
                return high
            else:
                return mid
        # covers every case on what to return for the given conditions after comparing low, mid, and high


# Outside of Sorting class now!!

# B. Radix Sort
# Radix sort is a non-comparative sorting algorithm that works by distributing elements
# into buckets according to their individual digits or radix. It functions by sorting the 
# input numbers per one digit at a time. Please consider following skeleton for implementation.
def counting_sort(arr, exp):
    # Count occurrences of each digit.
    # Update count to store the position of the next occurrence.
    # Build the output array.
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    # Count occurences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    # Update count to store the position of the next occurence
    for i in range(1, 10):
        count[i] += count[i-1]
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    # Copy the output array to arr, so that arr contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

# radix sort function
def radix_sort(arr):
    # Return if array is empty.
    if not arr:
        return 
    # Find the maximum number to know the number of digits.
    max_num = max(arr)
    # Do counting sort for every digit.
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
arr = [234, 34, 34, 2, 1, 0, 2, 3422]
radix_sort(arr)
print("Sorted array:", arr)
# Sorted array: [0, 1, 2, 2, 34, 34, 234, 3422]


# Testing Logic
# Test quick sorting technique
def is_sorted(arr):
    if arr == sorted(arr):
        return "Passed!"
    else:
        return "Failed!"


def test_quicksort():
    """Test the Quicksort algorithm"""
    seed_num = 43
    seed(seed_num)  # Set the seed for reproducibility
    sorting = Sorting(10)
    for _ in range(10):
        sorting.add(randint(1, 100))

    sorting.quicksort(0, len(sorting.arr) - 1)  # Apply the Quicksort algorithm
    print("Quick Sort:", is_sorted(sorting.arr))


# Test case execution
test_quicksort()


# Test radix sorting technique
def test_radix_sort():
    # Test case 1
    arr1 = [234, 34, 34, 2, 1, 0, 2, 3422]
    radix_sort(arr1)
    assert arr1 == [0, 1, 2, 2, 34, 34, 234, 3422], f"Test case 1 failed: {arr1}"

    # Test case 2
    arr2 = [329, 457, 657, 839, 436, 720, 355]
    radix_sort(arr2)
    assert arr2 == [329, 355, 436, 457, 657, 720, 839], f"Test case 2 failed: {arr2}"

    # Test case 3
    arr3 = [1, 200, 3, 400, 5]
    radix_sort(arr3)
    assert arr3 == [1, 3, 5, 200, 400], f"Test case 3 failed: {arr3}"

    # Test case 4 (empty array)
    arr4 = []
    radix_sort(arr4)
    assert arr4 == [], f"Test case 4 failed: {arr4}"

    # Test case 5 (array with one element)
    arr5 = [42]
    radix_sort(arr5)
    assert arr5 == [42], f"Test case 5 failed: {arr5}"

    print("All test cases passed!")


# Run the test cases
test_radix_sort()