class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class MyStack:
    def __init__(self):
        self.top = None

    def push(self, node):
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return
        retval = Node(self.top.data)
        self.top = self.top.next
        return retval

    def isempty(self):
        return self.top is None

    def peek(self):
        if not self.isempty():
            return self.top
        return None


mystack = MyStack()
mystack.push(Node("1"))
mystack.push(Node("2"))
mystack.push(Node("3"))
print(mystack.peek())
mystack.pop()
mystack.push(Node("4"))
mystack.push(Node("5"))