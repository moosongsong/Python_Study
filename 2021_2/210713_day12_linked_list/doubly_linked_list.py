class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self, nodes=None):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def size(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def add_first(self, node):
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.size += 1

    def add_last(self, node):
        self.tail = node
        self.size += 1
        global current_node
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        node.prev = current_node

    def remove_node(self, target_node):
        if self.head is None:
            raise Exception("list empty")
        if self.head.data == target_node.data:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return
        previous_node = self.head
        for node in self:
            if node.data == target_node.data:
                previous_node.next = node.next
                previous_node.prev = node.prev
                self.size -= 1
                return
            previous_node = node
        raise Exception("not found")


my_list = DoublyLinkedList()
print(my_list)
my_list.add_last(Node("one"))
print(my_list)
print(my_list.size)
my_list.add_last(Node("two"))
print(my_list)
my_list.add_first(Node("zero"))
print(my_list)
print(my_list.size)
my_list.remove_node(Node("one"))
print(my_list)
print(my_list.size)
