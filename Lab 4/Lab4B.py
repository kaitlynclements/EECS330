'''
Author: Kaitlyn Clements
KUID: 3072622
Date: 09/21/2023
Lab: 4B
'''
from Lab4A_Deque import Deque, Node

# A. WordToDeque
def wordToDeque(input):
    deque = Deque()
    # Write your code here and return the Deque() object
    for char in input:
        node = Node(char)
        if deque.front is None:
            deque.front = node 
            deque.back = node
        else:
            node.prev = deque.back
            deque.back.next = node
            deque.back = node
        return deque

def testWordToDeque(test_string, test_deque):
    temp = test_deque
    for i in range(len(test_string)):
        if temp.front == None or test_string[i] != temp.front.item:
            return False
        else:
            temp.front = temp.front.next
    if temp.front != None:
        return False
    return True
test1_string = "hello"
test1_deque = wordToDeque(test1_string)
print(testWordToDeque(test1_string, test1_deque)) # Should return True

# B. OffByOne
def OffByOne(char1, char2):
    # Write your logic here 
    return abs(ord(char1) - ord(char2)) == 1
char1 = 'b'
char2 = 'a'
print(OffByOne(char1, char2))  # Should print True

# C. OffByN
def OffByN(char1, char2, N):
    # Write your code here and return either True or False
    return abs(ord(char1) - ord(char2)) == N
char1 = 'b'
char2 = 'e'
N = 3
print(OffByN(char1, char2, N))  # Should print True