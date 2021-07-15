class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, node):
        temp_node = self.root
        if self.root is None:
            self.root = node
            return
        else:
            pre_node = self.root
            while pre_node is not None:
                temp_node = pre_node
                if node.data < pre_node.data:
                    pre_node = pre_node.left
                else:
                    pre_node = pre_node.right
            if node.data < temp_node.data:
                temp_node.left = node
            else:
                temp_node.right = node

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node)
            self.in_order(node.right)

    def pre_order(self, node):
        if node is not None:
            print(node)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node)


tree = Tree(Node('A'))
tree.add(Node('B'))
tree.add(Node('E'))
tree.add(Node('G'))
tree.add(Node('F'))
tree.add(Node('C'))
tree.add(Node('H'))
tree.add(Node('I'))
tree.add(Node('D'))
tree.in_order(tree.root)
