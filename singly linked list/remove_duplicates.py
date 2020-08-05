class Node():
    def __init__(self, data):
        self.data = data
        self. next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def show_list(self):
        current_node = self.head
        print("Linked List elements:")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print()

    def remove_duplicates(self):

        cur = self.head
        prev = None

        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before, add to dict
                dup_values[cur.data] = 1 # look-up in hash-table much faster than checking an item in a list
                prev = cur
            cur = prev.next





llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)
llist.show_list()
llist.remove_duplicates()
llist.show_list()
