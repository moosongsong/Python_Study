class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, node):
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return
        retval = Node(self.front.data)
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return retval

    def isempty(self):
        return self.front is None

    def peek(self):
        if not self.isempty():
            return self.front.data
        else:
            return None


myqueue = MyQueue()
myqueue.enqueue(Node("1"))
myqueue.enqueue(Node("2"))
myqueue.enqueue(Node("3"))
myqueue.dequeue()
temp = myqueue.dequeue()
print(temp)
