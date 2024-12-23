class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        print(self.data, self.left, self.right, data)
        if self.data == data:
            return


        if data < self.data:
            if self.left:
                self.left.add_child(data)
                print('self left', self.left, self.right)
            else:
                self.left = BinarySearchTreeNode(data)
                print('when data is greater than self left', self.left, self.right)
        else:
            print('greater', data)

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    # print('from root',root)
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root



if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
