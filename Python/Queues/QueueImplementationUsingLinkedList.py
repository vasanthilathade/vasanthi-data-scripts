class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.rear = self.front = new_node
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.value

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.front.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

    def printQueue(self):
        temp = self.front
        while temp:
            print(f"{temp.value} end is ->")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.printQueue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.printQueue()
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.stackSize())

k="ssss"
k.replace('s','q')
print(k)