"""
    Author: Kaitlin Clements
    KU ID: 3072622
    Date: 09/26/2023
    Lab: 5- Disjoint Sets
"""

# A. Implementation of Disjoint Set
"""
You have been given a skeleton of a Disjoint set. 
Following skeleton implements constructor for "Disjoint Set".
"""


class DisjointSet:
    def __init__(self, size):
        self.vertex = [i for i in range(size)]
        self.weight = [1] * size
        self.rank = [0] * size

    # A.1 Implement Utility Methods
    def validate(self, v1):
        # check if v1 is a valid index
        if len(self.vertex) >= 1:
            return True
        else:
            raise IndexError("Invalid Index")

    def size(self, v1):
        # return the size of the set v1 belongs to
        if not self.validate(v1):
            raise IndexError("Invalid Index")
        root = self.find(v1)
        return self.weight[root]

    def parent(self, v1):
        # return the parent of v1. if v1 is the root of a tree,
        # return the negative size of the tree for which v1 is the root
        if not self.validate(v1):
            raise IndexError("Invalid Index")
        parent = self.vertex[v1]
        if parent == v1:
            return -self.weight[v1]
        else:
            return parent

    # A.2 Implement isConnected
    def isConnected(self, v1, v2):
        # Check if given vertex are connected or not.
        # Return True if connected, if not return False
        return self.find(v1) == self.find(v2)

    # A.3 Implement find
    def find(self, v1):
        # Returns the root of the set v1 belongs to
        if self.vertex[v1] == v1:
            return v1
        else:
            root = self.find(self.vertex[v1])
            return root

    # A.4 Implement Union by Weight
    def unionByWeight(self, v1, v2):
        # Connects two elements, v1 and v2, together. v1 and v2 can be any valid elements,
        # and a union-by-size heuristic is used. If the sizes of the sets are equal, 
        # tie break by connecting v1's root to v2's root. Unioning a vertex with itself or 
        # vertices that are already connected should not change the sets, but it may alter 
        # the internal structure of the data structure. 
        if not self.validate(v1) or not self.validate(v2):
            raise IndexError("Invalid Index")
        root1 = self.find(v1)
        root2 = self.find(v2)
        size1 = self.size(root1)
        size2 = self.size(root2)
        if size1 == size2 or size1 > size2:
            # tie-break by connecting v1's root to v2's root
            self.vertex[root2] = root1
            self.weight[root1] += size2
        else:  # if size2 > size1
            self.vertex[root1] = root2
            self.weight[root2] += size1

    # A.5 Implement Union by Rank
    def unionByRank(self, v1, v2):
        # Change self.weight to self.rank in DisjoingSet. While applying union,
        # set with higher rank will represent as root. Re-implement B.4 using rank mechanism
        if not self.validate(v1) or not self.validate(v2):
            raise IndexError("Invalid Index")
        root1 = self.find(v1)
        root2 = self.find(v2)
        rank1 = self.rank[root1]
        rank2 = self.rank[root2]
        if rank1 == rank2 or rank1 < rank2:
            self.vertex[root2] = root1
            self.rank[root2] += rank1 + 1
        else:
            self.vertex[root1] = root2
            self.rank[root1] += rank2 + 1

    # B Find number of connected block sets in a given grid
    '''
    Given n blocks, some of them are connected, while some are not. If block 1 is connected directly with block 2,
    and block 2 is connected directly with block 3, then block 1 and 3 are connected.
    You are given an n x n matrix Connected where Connected[i][j] = 1 if the i-th block and the j-th block are directly connected,
    and Connected[i][j] = 0 otherwise.
    For example, shown by the below matrix. There are 4 blocks let say 0, 1, 2, 3. 
    To check if block 0 is connected to block 1 consider index i=0 and j=1 and Connected[0][1]=1 . Block 0 and 1 are connected
    [1,1,0,1]
    [1,1,0,0]
    [0,0,1,1]
    [1,0,1,1]
    Here block 1 is connected to 2 and 4:1--2--4 is a block set
    '''

    # B.1 Return a disjoint set using Connected matrix as input
    def joinBlocks(self, Connected):
        # Given the DisjointSet data structure you have, and Connected matrix showing the connectivity
        # among blocks, write a method to construct a DisjointSet at one time
        n = len(Connected)
        for i in range(n):
            for j in range(n):
                if Connected[i][j] == 1:
                    self.unionByWeight(i, j)
        return self.vertex

    # B.2 Return the total number of block sets
    def findBlockSets(self):
        # Return number of connected block sets available in the grid
        block_sets = 0
        for i in range(len(self.vertex)):
            if self.vertex[i] == i:
                block_sets += 1
        return block_sets

    # B.3 Return number of blocks in a connected block set
    def findBlockCount(self, blockid):
        # Return number of blocks in block set where the inquiry blockid belongs to.
        # If the blockid is not connected to any, then return 1.
        root = self.find(blockid)
        num = 0
        for i in range(len(self.vertex)):
            if self.vertex[i] == root:
                num += 1
        return num


# C. Testing your code for disjoint sets
# Below is the testing logic for code:
if __name__ == '__main__':
    # Tasks A
    uf = DisjointSet(10)
    # 0 1-2-5-6-7 3-8-9 4
    uf.unionByRank(1, 2)
    uf.unionByRank(2, 5)
    uf.unionByRank(5, 6)
    uf.unionByWeight(6, 7)
    uf.unionByRank(3, 8)
    uf.unionByWeight(8, 9)
    print(uf.isConnected(1, 5))  # true
    print(uf.isConnected(5, 7))  # true
    print(uf.isConnected(4, 9))  # false
    # 0 1-2-5-6-7 3-8-9-4
    uf.unionByWeight(9, 4)
    print(uf.isConnected(4, 9))  # true

    # Tasks B
    Connected = [[1,1,0,1], [1,1,0,0], [0,0,1,1], [1,0,1,1]]
    uf = DisjointSet(4)
    uf.joinBlocks(Connected)
    uf.findBlockCount(1)
