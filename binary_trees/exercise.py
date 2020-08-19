class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item_to_add):     # Add item to the beginning of the list
        self.items.insert(0, item_to_add)

    def dequeue(self):                  # Return the last element of the list
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return self.size()

    def peek(self):
        if not self.is_empty():         # Return the value of the last element
            return self.items[-1].value

    def size(self):
        return len(self.items)

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
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
            print("Traversal type: " + str(traversal_type) + " is not supported!")

    def preorder_print(self, root, traversal):
        """
        Root -> Left -> Right
        """
        if root is not None:
            traversal += str(root.value) + "-"
            traversal = self.preorder_print(root.left, traversal)
            traversal = self.preorder_print(root.right, traversal)
        return traversal

    def inorder_print(self, root, traversal):
        """
        Left -> Root -> Right
        """
        if root is not None:
            traversal = self.inorder_print(root.left, traversal)
            traversal += str(root.value) + "-"
            traversal = self.inorder_print(root.right, traversal)
        return traversal

    def postorder_print(self, root, traversal):
        """
        Left -> Right -> Root
        """
        if root is not None:
            traversal = self.postorder_print(root.left, traversal)
            traversal = self.postorder_print(root.right, traversal)
            traversal += str(root.value) + "-"
        return traversal

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

q = Queue()
q.enqueue(Node(3))
q.enqueue(Node(2))
q.enqueue(Node(1))
print(q.dequeue().value)
print(q.peek())
