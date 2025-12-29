class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return True

        current = self.root
        while True:
            if current.value > value:
                if current.left is None:
                    current.left = node
                    return True

                current = current.left

            elif current.value < value:
                if current.right is None:
                    current.right = node
                    return True

                current = current.right

            else:
                return False


my_tree = BinarySearchTree()

print(my_tree.root)


"""
    EXPECTED OUTPUT:
    ----------------
    None

"""


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print("Root:", my_tree.root.value)
print("Root->Left:", my_tree.root.left.value)
print("Root->Right:", my_tree.root.right.value)


"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""
