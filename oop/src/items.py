import random

class Items:
    def __init__(self, numberOfItems=None, weights=None, values=None):
        if weights is not None and values is not None:
            self.weights = weights
            self.values = values
        elif numberOfItems is not None:
            self.weights = [random.randint(1,50) for _ in range(numberOfItems)]
            self.values  = [random.randint(1,20) for _ in range(numberOfItems)]
        else:
            raise ValueError("Either numberOfItems or weights and values must be provided")