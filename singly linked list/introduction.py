class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print()

    def append(self, data):
        new_node = Node(data)
        if self.head is None:       # HEAD pointer does not point anywhere, no elements in the Linked List
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return False

        new_node = Node(data)

        new_node.next = prev_node.next

        prev_node.next = new_node

    def delete_node(self, key):

        current_node = self.head
        # llist is not empty and we would like to delete the first element
        if current_node != None and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node is not None and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def delete_node_at_position(self, position):

        current_node = self.head

        if position == 0:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        count = 0
        while current_node and count != position:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            print("The position given is greater than the number of elements in the Linked List")
            return

        prev_node.next = current_node.next
        current_node = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()

llist.insert_after_node(llist.head.next, "E")

llist.print_list()

llist.delete_node("B")

llist.print_list()

# llist.delete_node_at_position(1)
#
# llist.print_list()
