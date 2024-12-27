class BSNode:
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
                self.left = BSNode(value)

        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSNode(value)




if "__main__" == __name__:
    value = BSNode(5)


