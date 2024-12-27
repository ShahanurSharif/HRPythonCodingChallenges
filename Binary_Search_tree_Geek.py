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
            else:
                self.left = BSTNode(value)

        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

        print(self.value)



if "__main__" == __name__:
    # nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    nums = [12, 6, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)


