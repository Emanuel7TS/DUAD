class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node= Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_back(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

        my_test_list = [18, -11, 68, 6, 32, 53, -2]

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data == data:
                previous.next = current.next
                return
            previous = current
            current = current.next

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def bubble_sort_list(self):
        while True:
            swap = False
            current = self.head
            while current.next is not None:
                temporal = current.data
                neighbour = current.next.data
                if temporal > neighbour:
                    current.next.data = temporal
                    current.data = neighbour
                    swap = True
                current = current.next
            if swap == False:
                break

test_list = LinkedList()


print("linked list")
test_list.insert_front(5)
test_list.insert_front(1)
test_list.insert_front(3)
test_list.insert_front(2)
test_list.insert_front(4)

test_list.print_all()
print("")

print("sorted list")

test_list.bubble_sort_list()

test_list.print_all()