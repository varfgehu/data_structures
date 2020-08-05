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
            new_node.next = None
            new_node.prev = None
        else:
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


    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs

# (1,2), (1,3), (1,4), (1,5)
# (2,3), (2,4), (2,5)
# (3,4), (3,5)
# (4,5)

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.show_list()

print(dllist.pairs_with_sum(5))
print(dllist.pairs_with_sum(0))
