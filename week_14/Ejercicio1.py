class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is not None:
            self.head = self.head.next


    def print_stack(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


first_node = Node("I'm the first one")
second_node = Node("I'm the second one")

stacker = Stack()
stacker.push(second_node)
stacker.push(first_node)

stacker.print_stack()

stacker.pop()

print("test")
print(stacker.head.data)