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

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        # If any of the given list are None (does not have elements)
        # return the other lsit
        if p is None:
            return q
        if q is None:
            return p

        # Selecting the starting element of the merged llist.
        if p and q:
            # If p.data le than q.data
            # p gonna be the first element
            # set s to p, and update p to the next element in its list
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            # save the first element, that will be the head of the merged llist
            new_head = s

        # while p and q are pointing to valid elements
        # we follow the logic above.
        # find the next element
        # set s.next with the lessthanequal element
        # update s with the finding
        # update p or q
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        # Quiting while loop if any of the list element
        # pointers hit the end of the llist
        # than founding the next element for s is easy,
        # if one hit the end, the next element must come from the other llist
        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head


llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
llist_2.append(8)

llist_1.show_list()
llist_2.show_list()

llist_1.merge_sorted(llist_2)
llist_1.show_list()
