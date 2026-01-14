class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    def delete(self, data):
        current = self.head

        while current is not None:
            if current.data == data:

                # Caso 1: único nodo
                if current.prev is None and current.next is None:
                    self.head = None
                    self.tail = None

                # Caso 2: es el head
                elif current.prev is None:
                    self.head = current.next
                    self.head.prev = None

                # Caso 3: es el tail
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None

                # Caso 4: está en medio
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return

            current = current.next


    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def print_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" -> ")
            current = current.prev
        print("None") #solo es visual para entender



dll = DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")

dll.print_forward()    # A -> B -> C -> None
dll.print_backward()   # C -> B -> A -> None

dll.prepend("X")

dll.print_forward()    # X -> A -> B -> C -> None
dll.print_backward()   # C -> B -> A -> X -> None

dll.delete("B")

dll.print_forward()    # X -> A -> C -> None
dll.print_backward()   # C -> A -> X -> None