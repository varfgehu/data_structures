class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    # Pre-order traversal:
    # 1, Check if current node is null
    # 2, Display data of the current node
    # 3, Traverse to the left subtree by calling the pre-order func
    # 4, Traverse to the right subtree by calling the pre-order func
    def preorder_print(self, start, traversal):
        """
        Root -> Left -> Right
        """
        if start: # if start is not None
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """
        Left->Root->Right
        """
        if start:     # if start is not None
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """
        Left->Right->Root
        """
        if start:     # if start is not None
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

# Preorder: 1-2-4-5-3-6-7-
# Inorder: 4-2-5-1-6-3-7-
# Postorder: 4-5-2-6-7-3-1-

#          1
#        /    \
#     2        3
#    / \     /  \
#   4  5    6    7


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
