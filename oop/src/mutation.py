from .abstract import MutationStrategy
import random
from .chromosome import Chromosome

class BitFlipMutation(MutationStrategy):
    def __init__(self, prob):
        self.prob = prob

    def mutate(self, chromosome):
        new_genes = [
            bit if random.random() > self.prob else 1 - bit
            for bit in chromosome.individual
        ]
        return Chromosome(new_genes)