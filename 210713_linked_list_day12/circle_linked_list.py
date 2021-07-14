class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self, nodes=None):
        node = self.head
        for i in range(self.size):
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        for i in range(self.size):
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node
        self.size += 1
        temp = self.head
        for i in range(self.size):
            temp = temp.next
        temp.next = node

    def add_last(self, node):
        self.size += 1
        if self.head is None:
            self.head = node
            node.next = self.head
            return
        temp = self.head
        for i in range(self.size):
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def remove_node(self, target_node):
        if self.head is None:
            raise Exception("list empty")

        if self.head.data == target_node.data:
            self.head = self.head.next
            temp = self.head
            for i in range(self.size):
                temp = temp.next
            temp.next = self.head
            self.size -= 1
            return
        previous_node = self.head
        for node in self:
            if node.data == target_node.data:
                previous_node.next = node.next
                self.size -= 1
                return
            previous_node = node
        raise Exception("not found")


my_list = CircleLinkedList()
print(my_list)
my_list.add_last(Node("one"))
print(my_list)
my_list.add_last(Node("two"))
print(my_list)
my_list.add_first(Node("zero"))
print(my_list)
my_list.add_first(Node("tt"))
print(my_list)
my_list.remove_node(Node("zero"))
print(my_list)
my_list.remove_node(Node("tt"))
print(my_list)