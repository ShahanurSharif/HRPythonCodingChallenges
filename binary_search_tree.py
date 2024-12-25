class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # print(data, self.data, self.left, self.right)
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)


    def in_order_traversal(self):
        elements = []
        if self.left:
            # print('before', elements)
            elements += self.left.in_order_traversal()
            # print('after', elements)
        elements.append(self.data)

        if self.right:
            elements += self.left.in_order_traversal()

        return elements


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    arr = [17, 4, 1, 9, 2, 7]
    number_tree = build_tree(arr)
    number_tree.in_order_traversal()
