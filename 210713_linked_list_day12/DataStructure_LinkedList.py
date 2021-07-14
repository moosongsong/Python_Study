class MyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    # 2 iteration init
    # def __init__(self, nodes=None):
    #     self.head = None
    #     if nodes is not None:
    #         node = MyNode(data=nodes.pop(0))
    #         self.head = node
    #         for elem in nodes:
    #             node.next = MyNode(data=elem)
    #             node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # 2 iteration
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # 3 add first/last
    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

# mylinkedlist = MyLinkedList()
# print(mylinkedlist)
#
# first_node = MyNode("one")
# mylinkedlist.head = first_node
# print(mylinkedlist)
#
# second_node = MyNode("two")
# third_node = MyNode("three")
# first_node.next = second_node
# second_node.next = third_node
# print(mylinkedlist)

#############################

# 2 : iteration
# mylinkedlist = MyLinkedList(["one", "two", "three", "four"])
# print(mylinkedlist)
#
# for node in mylinkedlist:
#     print(node)

# 3 : add (first) / whether head is None or not
# first
# mylinkedlist = MyLinkedList()
# print(mylinkedlist)
#
# mylinkedlist.add_first(MyNode("different_two"))
# print(mylinkedlist)
#
# mylinkedlist.add_first(MyNode("different_one"))
# print(mylinkedlist)

# last
# mylinkedlist = MyLinkedList(["one", "two", "three", "four"])
# print(mylinkedlist)
#
# mylinkedlist.add_last(MyNode("e"))
# print(mylinkedlist)
#
# mylinkedlist.add_last(MyNode("f"))
# print(mylinkedlist)

### add_after
# mylinkedlist = MyLinkedList()
# mylinkedlist.add_after("a", MyNode("b"))
#
# mylinkedlist = MyLinkedList(["a", "b", "c", "d"])
# print(mylinkedlist)
#
# mylinkedlist.add_after("c", MyNode("cc"))
# print(mylinkedlist)
#
# mylinkedlist.add_after("f", MyNode("g"))

### add_before

# mylinkedlist = MyLinkedList()
# mylinkedlist.add_before("a", MyNode("a"))
#
# mylinkedlistlist = MyLinkedList(["b", "c"])
# print(mylinkedlist)
#
# mylinkedlist.add_before("b", MyNode("a"))
# print(mylinkedlist)
#
# mylinkedlist.add_before("b",MyNode("aa"))
# mylinkedlist.add_before("c", MyNode("bb"))
#
# mylinkedlist.add_before("n", MyNode("m"))

### remove
# mylinkedlist = MyLinkedList()
# mylinkedlist.remove_node("a")
#
# mylinkedlist = MyLinkedList(["a", "b", "c", "d", "e"])
# print(mylinkedlist)
#
# mylinkedlist.remove_node("a")
# print(mylinkedlist)
#
# mylinkedlist.remove_node("e")
# print(mylinkedlist)
#
# mylinkedlist.remove_node("c")
# print(mylinkedlist)
#
# mylinkedlist.remove_node("a")
