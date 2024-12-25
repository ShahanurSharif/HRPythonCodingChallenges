class Man:
    def __init__(self, data):
        self.data = data
        self.left = 2
        self.right = 3

    def adding(self, data):
        return 10

    def testing_value(self):
        return self.left.testing_value(1)

man = Man(3)
print(man.testing_value())