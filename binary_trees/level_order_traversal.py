class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item_to_add):
        self.items.insert(0, item_to_add)  # Add item_to_add to the beginning of the list

    def dequeue(self):
        if not self.is_empty():    # If the queue is not empty return the last element (which is a Node object)
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value    # Return the value of the last element

    def __len__(self):
        return self.size()

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
        if traversal_type == "level_order":
            return self.levelorder_print(self.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not defined!")

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print(tree.print_tree("level_order"))
