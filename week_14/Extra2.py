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


# Test
test_list = LinkedList()

n1 = test_list.insert_front("B")
n2 = test_list.insert_front("A")
n3 = test_list.insert_back("C")

print("showing nodes")
test_list.print_all()
print("")

print("Adding other")
test_list.insert_front("D")
test_list.print_all()
print("")

print("Deleting 'D'")
test_list.delete("D")
test_list.print_all()
print("")