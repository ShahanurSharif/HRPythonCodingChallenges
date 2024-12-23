class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, node):
        pass


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    print('from root',root)
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root



if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
