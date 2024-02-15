"""
Author: Kaitlyn Clements
KUID: 3072622
Date: 09/21/2023
Lab: 4A
"""


# A. Design "Dequeue" using Linked-List data structure
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


# Implementation of Dequeue (Usinf Doubly-Linked-List)
class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    # B.1 Check whether the deque is empty
    def empty(self):
        """Check whether the deque is empty."""
        return (self.size) == 0

        # B.2 Check the size

    def get_size(self) -> int:
        """Return total number of elements in deque."""
        return self.size

    # B.3 Add element at front
    def push_front(self, data):
        """Push an element to the front of the deque."""
        new_node = Node(data)
        if self.empty():
            self.front = self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
        self.size += 1

    # B.4 Add element at the end
    def push(self, data):
        """Push an element at the back of the deque."""
        new_node = Node(data)
        if self.empty():
            self.front = self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
        self.size += 1

    # B.5 Remove element from the front
    def pop_front(self) -> int:
        """Pop an element from the front of the deque."""
        if self.empty():
            raise IndexError("Deque is empty")
        data = self.front.item
        if self.size == 1:
            self.front = self.back = None
        else:
            self.back = self.front.next
            self.front.prev = None
        self.size -= 1
        return data

    # B.6 Remove element from the end
    def pop(self) -> int:
        """Pop an element from the back of the deque."""
        if self.empty():
            raise IndexError("Deque is empty")
        data = self.back.item
        if self.size == 1:
            self.front = self.back = None
        else:
            self.back = self.back.prev
            self.back.next = None
        self.size -= 1
        return data

        # B.7 Access first element

    def front(self) -> int:
        """Access first element of deque."""
        if self.empty():
            raise IndexError("Deque is empty")
        else:
            return self.front.item

    # B.8 Access last element
    def back(self) -> int:
        """Access last element of deque."""
        if self.empty():
            raise IndexError("Deque is empty")
        else:
            return self.back.item

    # D. Implementation of isPalindrome using previously implemented deque


def isPalindrome(s: str) -> bool:
    # Initialize Deque using Deque class.
    deque = Deque()
    for letter in s:
        deque.push(letter)
    '''TODO: Implement your comparison logic.'''
    while not deque.empty():
        if deque.front != deque.back:
            return False
        deque.pop_front()
        deque.pop()
    return True

    # E. Implementation of Dequeue Reversal


def reverse_deque(deque):
    # Initialize an object for your new deque.
    reversed_deque = Deque()
    # TODO: Iterate through the deque and add items to reversed_deque.
    while not deque.empty():
        reversed_deque.push(deque.pop())
    # The items should be added in the reverse order.
    # The new deque reversed_deque should contain elements in exact reverse
    # of your current deque.
    return reversed_deque


# Testing logic
deque = Deque()
deque.push(1)
deque.push(2)
deque.push(3)

reversed_deque = reverse_deque(deque)
while not reversed_deque.empty():
    print(reversed_deque.pop_front())  # Should output 3, 2, 1.
