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
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def show_list(self):
        cur = self.head
        print("CircularLinkedList elemets:")
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
        print()

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return
        if size == 1:
            return self.head

        mid = size//2
        count = 0
        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next

        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.show_list()
        split_cllist.show_list()

# A -> B -> C -> D-> ..
# A -> B -> .. and C -> D ->..

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.show_list()
print(len(cllist))
cllist.split_list()
