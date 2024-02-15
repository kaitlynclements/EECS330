'''
Author: Kaitlyn Clements
KUID: 3072622
Date: 09/05/2023
Lab: 3
'''


class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item  # int
            self.next = next_node  # IntNode

    def __init__(self):
        self.first = None  # initialize an empty list

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)

    # 1.1 Insert an Item
    def insert(self, item, position):
        # write code here
        if position <= 0:
                self.addFirst(item)
        else:
            current = self.first
            for x in range(position - 1):
                if current is None:
                    break
                current = current.next
            if current is not None:
                current.next = self.IntNode(item, current.next)
            else:
                self.addFirst(item)

    # 1.2 Reverse the List
    def reverse(self):
        # write code here
        before = None
        current = self.first
        while current is not None:
            next_node = current.next
            current.next = before
            before = current
            current = next_node
        self.first = before
        return

    # 1.3 Replicate the list
    def replicate(self):
        # write code here
        new_list = SLList()
        current = self.first
        while current is not None:
            item = current.item
            current = current.next
            new_list.addFirst(item)
            if current is not None:
                for x in range(item - 1):
                    new_list.addFirst(item)
        return new_list

    #1.4 (Extra) Another Implementation
    def equals(self, anotherList):
        # write code here
        current_self = self.first
        current_other = anotherList.first
        while current_self is not None and current_other is not None:
            if current_self.item != current_other.item:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None

    #1.4 Write the Test Case
if __name__ == '__main__':
    #create linked list
    L = SLList()
    L.addFirst(15)
    L.addFirst(10)
    L.addFirst(5)
    L.reverse()

    L_expect = SLList()
    L_expect.addFirst(5)
    L_expect.addFirst(10)
    L_expect.addFirst(15)

    if L.equals(L_expect):
        print("Two lists are equal, tests passed")
    else:
        print("Two lists are not equal, tests failed")