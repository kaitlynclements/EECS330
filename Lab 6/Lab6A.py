'''
    Author: Kaitlyn Clements
    KU ID: 3072622
    Lab: 6A
'''


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self._root = None
        '''Number of Nodes in the Tree'''
        self.size = 0

    # A.1 Insert a node with value in BST
    def insert(self, key):
        """Implement your insertion algo."""
        self.size += 1
        return self._rec_insert(self._root, key)

    def _rec_insert(self, cur_node, key):
        if cur_node is None:
            cur_node = TreeNode(key)
            return cur_node
        if key < cur_node.value:
            cur_node.left = self._rec_insert(cur_node.left, key)
        elif key > cur_node.value:
            cur_node.right = self._rec_insert(cur_node.right, key)
        elif key == cur_node.value:
            cur_node.right = self._rec_insert(cur_node.right, key)

            # A.2 Search a value in BST and return TreeNode

    '''
    Note that you have to return the first node using preorder traversal if multiple 
    values are present.
    '''

    def search(self, key) -> TreeNode:
        """Return TreeNode Corresponding to the value."""
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        if cur_node is None:
            return None
            # empty tree case
        if key == cur_node.value:
            return cur_node
            # current node is the target being searched for
        elif key < cur_node.value:
            return self._rec_search(key, cur_node.left)
        else:
            return self._rec_search(key, cur_node.right)
            # recursive case: look into both the LST and RST

    # B. Imlementation of level-order Traversal
    '''
    You can traverse the tree level by level in a breadth first search fashion. 
    Start at the root node and visit nodes level by level, from left to right 
    including all the nodes in that level. The order of operations is: 
    Level1 -> Level2 -> Level3 -> ... -> LevelN.
    '''

    def level_order_traversal(self) -> list:
        result = []
        root = self._root
        if root is None:
            return result
        queue = [root]
        while queue:
            current_level = []
            next_level = []
            for node in queue:
                current_level.append(node.value)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.extend(current_level)
            queue = next_level
        return result


# C. Implement TreeMap(SortedMap) using BST
'''
    A TreeMap (or a SortedMap) using BST is a common data structure that leverages 
    Binary Search Trees (BSTs) to implement a map interface where the keys are sorted 
    according to the BST implementation. TreeMap contains key and value as member variables 
    and the Tree is organized according to the "key". Following is the skeleton.
'''


class TreeNode2:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self._root = None

    def put(self, key, value):
        self._root = self._rec_put(self._root, key, value)

    def _rec_put(self, cur_node, key, value):
        if cur_node is None:
            return TreeNode2(key, value)
        if key < cur_node.key:
            cur_node.left = self._rec_put(cur_node.left, key, value)
        elif key > cur_node.key:
            cur_node.right = self._rec_put(cur_node.right, key, value)
        else:
            cur_node.value = value
        return cur_node

    def get(self, key):
        return self._rec_get(self._root, key)

    def _rec_get(self, cur_node, key):
        if cur_node is None:
            return None
        if key < cur_node.key:
            return self._rec_get(cur_node.left, key)
        elif key > cur_node.key:
            return self._rec_get(cur_node.right, key)
        else:
            return cur_node.value


# Initialize BST
bst = BinarySearchTree()

# Test inserting nodes
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)

# Test size method.
assert bst.size == 7
assert bst.search(1) is None

# Test inserting additional nodes.
bst.insert(1)
bst.insert(6)

assert bst.size == 9
result = bst.search(1)
assert result is not None and result.value == 1

# Finally, also test by inserting duplicate values.

# Test level order traversal with duplicates.
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)
bst.insert(5)
bst.insert(7)
bst.insert(1)
bst.insert(6)
bst.insert(1)
bst.insert(6)

# Test level order traversal.
assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9, 1, 5, 7, 1, 6, 6]

# TreeMap.

# Create a TreeMap
tree_map = TreeMap()

# Test putting and getting key-value pairs.
tree_map.put(3, "A")
tree_map.put(1, "B")
tree_map.put(2, "C")
tree_map.put(4, "D")

assert tree_map.get(2) == "C"
assert tree_map.get(1) == "B"
assert tree_map.get(4) == "D"
# Non-existent key should return None.
assert tree_map.get(5) is None
