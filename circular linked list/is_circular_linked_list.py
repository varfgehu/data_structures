class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node

    def show_list(self):
        cur = self.head
        print("LinkedList elements:")
        while cur != None:
            print(cur.data)
            cur = cur.next
        print()

class CircularLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def show_list(self):
        cur = self.head
        print("CircularLinkedList elements:")
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
        print()

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.show_list()

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.show_list()

print(cllist.is_circular_linked_list(cllist))
print(cllist.is_circular_linked_list(llist))
