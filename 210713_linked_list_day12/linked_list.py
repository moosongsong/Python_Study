class MyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

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

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        global current_node
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def remove_node(self, target_node):
        if self.head is None:
            raise Exception("list empty")

        if self.head.data == target_node.data:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == target_node.data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("not found")


my_list = MyLinkedList()
print(my_list)
my_list.add_last(MyNode("one"))
print(my_list)
my_list.add_last(MyNode("two"))
print(my_list)
my_list.add_first(MyNode("zero"))
print(my_list)
my_list.remove_node(MyNode("one"))
print(my_list)
