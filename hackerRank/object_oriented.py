class Man:
    def __init__(self, data):
        self.data = data
        self.left = None  # Default to None
        self.right = None  # Default to None

    def adding(self, data):
        return 10

    def testing_value(self, data):
        # Base case: If no left child, return the current data
        if self.left is None:
            return self.data
        # Recursive case
        return self.left.testing_value(1)

# Create the initial object
man = Man(3)
man.left = Man(2)  # Assign a left child
print(man.testing_value(1))