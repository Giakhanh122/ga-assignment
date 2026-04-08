import random
from .abstract import SelectionStrategy
from .items import Items


class OneMaxSelection(SelectionStrategy):
    def __init__(self, k=3):
        self.k = k

    def select(self, population):
        selected = random.sample(population.individuals, self.k)
        return max(selected, key=lambda c: c.onemax_fitness())

class KnapSackSelection(SelectionStrategy):
    def __init__(self, k=3):
        self.k = k

    def select(self, population, items : Items):
        selected = random.sample(population.individuals, self.k)
        weights = items.weights
        values = items.values
        capacity = sum(weights) * 0.4

        return max(selected, key=lambda c: c.knapsack_fitness(items))