class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        # here root node setup
        if not self.value:
            self.value = value
            return

        if self.value == value:
            return

        if value < self.value:
            if self.left:
                self.left.insert(value)
                return

            self.left = BSTNode(value)
            return

        if value > self.value:
            if self.right:
                self.right.insert(value)
                return
            self.right = BSTNode(value)
            return


    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals



if "__main__" == __name__:
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    # nums = [12, 6, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)

    print(bst.preorder([]))


