class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show_list(self):
        current_node = self.head
        print("Linked List elements:")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print()

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        current_1 = self.head
        while current_1 is not None and current_1.data != key_1:
            prev_1 = current_1
            current_1 = current_1.next

        # print(prev_1.data)
        # print(current_1.data)

        prev_2 = None
        current_2 = self.head
        while current_2 is not None and current_2.data != key_2:
            prev_2 = current_2
            current_2 = current_2.next

        # print(prev_2.data)
        # print(current_2.data)

        if current_1 is None or current_2 is None:
            print("One of the given key does not exist!")
            return

        # current_1 is not HEAD
        if prev_1 is not None:
            prev_1.next = current_2
        else:
            self.head = current_2

        if prev_2 is not None:
            prev_2.next = current_1
        else:
            self.head = current_1

        current_1.next, current_2.next = current_2.next, current_1.next











llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.show_list()
llist.swap_nodes("A", "C")
llist.show_list()
