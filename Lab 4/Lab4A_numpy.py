"""
Author: Kaitlyn Clements
KUID: 3072622
Date: 09/21/2023
Lab: 4A
"""

import numpy as np


# Implementation of dequeue (using numpy.array)
class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        # Initialize front and rear pointers.
        self.front = -1
        self.back = -1
        # Initialize size of the deque.
        self.size = 0
        # Use a zero initialized NumPy array to store elements.
        self.array = np.zeros(self.capacity, dtype=object)

    # C.1 Implement deque functions
    # 1. empty(self)
    def empty(self):
        return self.size == 0

    # 2. get_size(self)
    def get_size(self):
        return self.size

    # 3. push_front(self, data)
    def push_front(self, data):
        if self.size == self.capacity:
            self.resize()
        if self.empty():
            self.front = self.back = 0
        else:
            self.front = (self.front - 1) % self.capacity

        self.array[self.front] = data
        self.size += 1
        return

    # 4. push(self, data)
    def push(self, data):
        if self.size == self.capacity:
            self.resize()
        if self.empty():
            self.front = self.back = 0
        else:
            self.array[self.back + 1] % self.capacity

        self.array[self.back] = data
        self.size += 1
        return

    # 5. pop_front(self)
    def pop_front(self):
        if self.empty():
            raise IndexError("Deque is empty")
            pass
        else:
            data = self.array[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
        return data

    # 6. pop(self)
    def pop(self):
        if self.empty():
            raise IndexError("Deque is empty")
            pass
        else:
            data = self.array[self.back]
            self.array[self.back] = 0
        if self.front == self.back:
            self.front = self.back = -1  # resetting deque
        elif self.back == 0:
            self.back = self.capacity - 1
        self.size -= 1
        return data

    # C.2 Implement resize function
    def resize(self):
        # Set the new capacity.
        new_capacity = self.capacity * 2
        # TODO: Create a new numpy array.
        new_array = np.zeros(new_capacity, dtype=object)
        # TODO: Copy elements from the old array to the new one.
        for i in range(self.size):
            new_array[i] = self.array[(self.front + 1) % self.capacity]
        # TODO: Set memeber variables accordingly.
        self.front = 0
        self.back = self.size
        self.capacity = new_capacity
        self.array = new_array


# Testing logic
deque = Deque()
deque.push(1)
deque.push(2)
deque.push(3)
