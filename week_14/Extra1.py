class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return data

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print()

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.print_all()      # A -> B -> C

print(q.dequeue()) # A

q.print_all()      # B -> C