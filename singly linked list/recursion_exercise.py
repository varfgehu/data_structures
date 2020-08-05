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

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def recursive_length(self, node):
        if node.next is not None:
            return 1 + self.recursive_length(node.next)
        else:
            return 1

    def recursive_reverse(self):

        def _recursive_reverse(current, prev):

            if current.next is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next
                return _recursive_reverse(current, prev)
            else:
                self.head = current
                current.next = prev
                return

        _recursive_reverse(self.head, None)

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.show_list()
print(llist.recursive_length(llist.head))
llist.recursive_reverse()
llist.show_list()







def fact(n):
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fact(5))
print(fib(18))
