import random
from .items import Items

class Chromosome:
    def __init__(self, bits):
        self.individual = bits
    @classmethod
    def random(self, bit_length):
        gens = [random.randint(0,1) for _ in range(bit_length)]
        return Chromosome(gens)

    def onemax_fitness(self):
        return sum(self.individual)
       
    def knapsack_fitness(self, items: Items):
        # length = len(self.individual)
        weights = items.weights
        values = items.values
        capacity = sum(weights) * 0.4
        cap = sum([weight * bit for weight, bit in zip(weights, self.individual)])
        if cap <= capacity:
            return sum([value * bit for value, bit in zip(values, self.individual)])
        return 0
        # return sum([values[_] for _ in range(length) if self.individual[_]]) if cap <= capacity else 0
    
    def data(self):
        return self.individual
        
    def __str__(self): 
        return str(self.individual)