from .abstract import CrossoverStrategy
import random
from .chromosome import Chromosome


class OnePointCrossover(CrossoverStrategy):
    def __init__(self, length):
        self.length = length

    def crossover(self, p1, p2):
        point = random.randint(1, self.length - 1)
        c1 = Chromosome(p1.individual[:point] + p2.individual[point:])
        c2 = Chromosome(p2.individual[:point] + p1.individual[point:])
        return c1, c2
