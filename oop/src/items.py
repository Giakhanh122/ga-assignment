import random

class Items:
    def __init__(self, numberOfItems):
        self.weights = [random.randint(1,50) for _ in range(numberOfItems)]
        self.values  = [random.randint(1,20) for _ in range(numberOfItems)]