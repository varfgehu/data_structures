class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show_list(self):
        current_node = self.head
        print("LinkedList elements:")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print()

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_key(self, key, data):
        new_node = Node(data)

        current_node = self.head
        while current_node is not None and current_node.data != key:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def delete_by_key(self, key):

        current_node = self.head

        if current_node is not None and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node is not None and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("No Node with the given key!")
            return

        prev_node.next = current_node.next
        current_node = None

    def delete_by_position(self, position):
        current_node = self.head

        if position == 0:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        count = 0

        while current_node is not None and count != position:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            print("No position in Linked List!")
            return

        prev_node.next = current_node.next
        current_node = None



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")
llist.show_list()
llist.insert_after_key(key = "D", data = "E")
llist.show_list()
llist.insert_after_key("C", "F")
llist.show_list()
llist.delete_by_key("B")
llist.show_list()
llist.delete_by_key("F")
llist.show_list()
llist.delete_by_position(2)
llist.show_list()
