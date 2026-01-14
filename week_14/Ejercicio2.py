class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Deque:
    def __init__(self):
        self.head = None


    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop_left(self):
        if self.head is not None:
            self.head = self.head.next

    def push_right(self, new_node):
        if self.head is None:
            self.head = new_node
            return


        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node


    def pop_right(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None

    def print_deque(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next



deque = Deque()

print("Push left:")
deque.push_left(Node("A"))
deque.push_left(Node("B"))
deque.push_left(Node("C"))
deque.print_deque()

print("\nPush right:")
deque.push_right(Node("D"))
deque.push_right(Node("E"))
deque.print_deque()

print("\nPop left:")
deque.pop_left()
deque.print_deque()

print("\nPop right:")
deque.pop_right()
deque.print_deque()

print("\nVaciando la deque:")
deque.pop_left()
deque.pop_left()
deque.pop_left()
deque.print_deque()

print("\nPop en deque vacía (no debe fallar):")
deque.pop_left()
deque.pop_right()