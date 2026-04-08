
from .chromosome import Chromosome
from .items import Items

class Population:
    def __init__(self, size, length):
        self.individuals = [Chromosome.random(length) for _ in range(size)]

    def get_best_oneMax(self):
        return max(self.individuals, key=lambda c: c.onemax_fitness())
    
    def get_best_knapSack(self, items : Items):
        return max(self.individuals, key=lambda x : x.knapsack_fitness(items))