class Man:
    def __init__(self, data):
        self.data = data
        # Initialize left and right as new Man instances
        self.left = 2
        self.right = 3

    def adding(self, data):
        return 10

    def testing_value(self, data):
        # Call testing_value recursively on the left child
        return self.left

# Create the initial object
man = Man(3)
print(man.testing_value(1))