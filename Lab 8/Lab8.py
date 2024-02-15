"""
    Author: Kaitlyn Clements
    KUID: 3072622
    Lab: 7- Implementation of Tree and Graph Traversals
"""

# A. Implementation of a Tree Traversal
# You are given a binary tree structure represented by the classes TreeNode and BinaryTree. 
# Your task is to implement three different tree traversal algorithms: Preorder, Inorder, and Postorder. 
# The TreeNode class defines the individual nodes with a value, a Left child, right child, 
# while the Binary Tree class manages the root node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    # A.1 Implement Preorder Traversal 
    # Implement the Preorder Traversal for the given binary tree. Preorder traversal involves
    # visiting the current node, then its LST, and finally its RST. The operations should be in the following order:
    # Current Root -> LST -> RST
    def preorder_traversal(self) -> list:
        """Implement preorder traversal."""
        def _rec_pre(node, result):
            if node: 
                result.append(node.value)
                _rec_pre(node.left, result)
                _rec_pre(node.right, result)
        result = []
        _rec_pre(self.root, result)
        return result
        

    # A.2 Implement Inorder Traversal
    # Implement the Inorder Traversalfor the given binary tree. Inorder traversal involves visiting
    # the LST first, then the current node, and finally the RST. The operations should be in the following order:
    # LST -> Current Root -> RST
    def inorder_traversal(self) -> list:
        """Implement inorder traversal."""
        def _rec_in(node, result):
            if node:
                _rec_in(node.left, result)
                result.append(node.value)
                _rec_in(node.right, result)
        result = []
        _rec_in(self.root, result)
        return result
                
        

    # A.5 Implement Postorder Traversal
    # Implement the Postorder Traversal algorithm for the given binary tree. Postorder travesal involves
    # visiting the LST first, the the RST, and finally the Current node. Ther operations should be in the following order:
    # LST -> RST -> Current root
    def postorder_traversal(self) -> list:
        """Implement postorder traversal."""
        def _rec_post(node, result):
            if node:
                _rec_post(node.left, result)
                _rec_post(node.right, result)
                result.append(node.value)
        result = []
        _rec_post(self.root, result)
        return result

# Testing Logic

# Create a binary tree
bt = BinaryTree()
bt.root = TreeNode(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)
bt.root.right.left = TreeNode(6)
bt.root.right.right = TreeNode(7)
bt.root.left.left.left = TreeNode(8)
bt.root.left.left.right = TreeNode(9)
bt.root.right.right.right = TreeNode(10)

# Test the traversals
print("Preorder Traversal:", bt.preorder_traversal())
print("Inorder Traversal:", bt.inorder_traversal())    
print("Postorder Traversal:", bt.postorder_traversal())  



# B. Implementation of Graph Traversal
# You are provided with a graph represented as an adjacency list. The graph is defined using the Graph class with
# nodes and edges. Your task is to implement Depth-First Seach and Breadth-First Search traversal algorithms for this graph
from collections import deque
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        """Add an edge between vertices u and v."""
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
        

    # B.1 Implement DFS (Depth First Search)
    # Implement the DFS traversal algorithm for the given graph. DFS explores as far as possible along each branch
    # before backtracking. Your DFS implementation should start from a given source vertex and visit all reachable variables. 
    def dfs(self, source):
        """Implement Depth-First Search (DFS) starting from the source vertex."""
        visited = [False] * self.vertices
        result = []
        def _rec_dfs(v):
            visited[v] = True
            result.append(v)
            for u in self.adjacency_list[v]:
                if not visited[u]:
                    _rec_dfs(u)
        _rec_dfs(source)
        return result

    # B.2 Implement BFS (Breadth First Search)
    # Implement the Breadth-First Search traversal algorithm for the given graph. BFS explores all the vertices at
    # the current level before moving to the next level. Your BFS implementation should start from a given source vertex
    # and visit all reachable nodes. 
    def bfs(self, source):
        """Implement Breadth-First Search (BFS) starting from the source vertex."""
        visited = [False]*self.vertices
        result = []
        queue = deque([source])
        visited[source] = True
        
        while queue:
            v = queue.popleft()
            result.append(v)
            for u in self.adjacency_list[v]:
                if not visited[u]:
                    queue.append(u)
                    visited[u] = True
        return result
        pass
    
# Testing logic

# Create a graph with 20 vertices
graph = Graph(20)

# Add edges (change as needed)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 7)
graph.add_edge(3, 8)
graph.add_edge(4, 9)
graph.add_edge(4, 10)
graph.add_edge(5, 11)
graph.add_edge(5, 12)
graph.add_edge(6, 13)
graph.add_edge(6, 14)
graph.add_edge(7, 15)
graph.add_edge(7, 16)
graph.add_edge(8, 17)
graph.add_edge(8, 18)
graph.add_edge(9, 19)

# Test DFS and BFS from a source vertex
print("DFS from vertex 0:", graph.dfs(0))  
print("BFS from vertex 0:", graph.bfs(0))

# Create a graph with 4 vertices
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Test DFS and BFS from a source vertex
print("DFS from vertex 2:", graph.dfs(2))
print("BFS from vertex 2:", graph.bfs(2)) 