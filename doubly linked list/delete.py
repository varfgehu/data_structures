class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None


    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1
                if not cur.next: # if the next points to a node
                    cur = None
                    self.head = None
                    return
                # Case 2
                else:
                    next = cur.next
                    cur.next = None
                    cur = None
                    next.prev = None
                    self.head = next
                    return
            elif cur.data == key:
                # Case 3
                if cur.next:
                    next = cur.next
                    prev = cur.prev
                    prev.next = next
                    next.prev = prev
                    cur.next = None
                    cur.prev = None
                    return

                # Case 4
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next


    def show_list(self):
        cur = self.head
        print("DoublyLinkedList elements:")
        while cur:
            print(cur.data)
            cur = cur.next
        print()

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.show_list()

dllist.delete(1)
dllist.delete(6)
dllist.delete(4)

dllist.delete(2)
dllist.show_list()
