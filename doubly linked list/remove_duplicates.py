class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def show_list(self):
        cur = self.head
        print("DoublyLinkedList elements:")
        while cur:
            print(cur.data)
            cur = cur.next
        print()

    def delete_by_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1: delete first node, when it is the only one
                if cur.next is None:
                    cur = None
                    self.head = None
                    return
                else:
                    next = cur.next
                    cur.next = None
                    cur = None
                    next.prev = None
                    self.head = next
                    return
            elif cur == node:
                if cur.next is not None:
                    next = cur.next
                    prev = cur.prev
                    prev.next = next
                    next.prev = prev
                    cur.next = None
                    cur.prev = None
                    return
                else:
                    prev = cur.prev
                    cur.prev = None
                    prev.next = None
                    cur = None
                    return
            cur = cur.next

    def remove_duplicaties(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                next = cur.next
                self.delete_by_node(cur)
                cur = next






dllist = DoublyLinkedList()
dllist.append(8)
dllist.append(4)
dllist.append(4)
dllist.append(6)
dllist.append(4)
dllist.append(8)
dllist.append(4)
dllist.append(10)
dllist.append(12)
dllist.append(12)
dllist.show_list()

dllist.remove_duplicaties()
dllist.show_list()
