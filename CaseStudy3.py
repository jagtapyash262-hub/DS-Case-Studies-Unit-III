
# Case Study 3: Stack and Queue Using Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack implementation using a linked list
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        print(self.top.data, "popped from stack")
        self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        current = self.top
        print("Stack elements (top to bottom):", end=" ")

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


# Queue implementation using a linked list
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "added to queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        print(self.front.data, "removed from queue")
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        current = self.front
        print("Queue elements (front to rear):", end=" ")

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


# Demonstration of stack operations
print("STACK OPERATIONS")
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.peek()
stack.pop()
stack.display()

# Demonstration of queue operations
print("\nQUEUE OPERATIONS")
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.peek()
queue.dequeue()
queue.display()
