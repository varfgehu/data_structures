class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

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

    def remove(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next


# A -> B -> C -> D -> E -> ...
# Remove key = "B"
# A -> C -> D -> E -> ...

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.show_list()

cllist.remove("B")
cllist.remove("E")
cllist.show_list()

cllist.remove("F")
cllist.show_list()
