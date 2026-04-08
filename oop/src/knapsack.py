import random
from src.abstract import SelectionStrategy, MutationStrategy, CrossoverStrategy

class Items:
    def __init__(self, numberOfItems):
        self.weights = [random.randint(1,50) for _ in range(numberOfItems)]
        self.values  = [random.randint(1,20) for _ in range(numberOfItems)]
    def calculateCapacity(self):
        capacity = (int)(0.4 * sum(self.weights))

class Chromosome:
    def __init__(self, bits):
        self.individual = bits
    @classmethod
    def random(self, bit_length):
        gens = [random.randint(0,1) for _ in range(bit_length)]
        return Chromosome(gens)

    def fitness(self, items: Items):
        length = len(self.individual)
        weights = items.weights
        values = items.values
        capacity = items.calculateCapacity()

        cap = sum([weights[_] for _ in range(length) if self.individual[_]])
        return sum([values[_] for _ in range(length) if self.individual[_]]) if cap <= capacity else 0
        
    def __str__(self): 
        return str(self.individual)

class KnapSackSelection(SelectionStrategy):
    def __init__(self, k=3):
        self.k = k

    def select(self, population, items : Items):
        selected = random.sample(population.individuals, self.k)
        weights = items.weights
        values = items.values
        capacity = items.calculateCapacity()

        return max(selected, key=lambda c: c.fitness(population, items))


# class OnePointCrossover(CrossoverStrategy):
#     def __init__(self, length):
#         self.length = length

#     def crossover(self, p1, p2):
#         point = random.randint(1, self.length - 1)
#         c1 = Chromosome(p1.individual[:point] + p2.individual[point:])
#         c2 = Chromosome(p2.individual[:point] + p1.individual[point:])
#         return c1, c2


# class BitFlipMutation(MutationStrategy):
#     def __init__(self, prob):
#         self.prob = prob

#     def mutate(self, chromosome):
#         new_genes = [
#             bit if random.random() > self.prob else 1 - bit
#             for bit in chromosome.individual
#         ]
#         return Chromosome(new_genes)


class Population:
    def __init__(self, size, length):
        self.individuals = [Chromosome.random(length) for _ in range(size)]

    def get_best(self):
        return max(self.individuals, key=lambda c: c.fitness())


class GeneticAlgorithm:
    def __init__(self, population, selection, crossover, mutation, generations, items : Items):
        self.population = population
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.generations = generations
        self.items = items

    def run(self):
        for gen in range(self.generations):
            new_individuals = []

            # elitism
            best = self.population.get_best()
            new_individuals.append(best)

            while len(new_individuals) < len(self.population.individuals):
                p1 = self.selection.select(self.population, self.items)
                p2 = self.selection.select(self.population, self.items)

                c1, c2 = self.crossover.crossover(p1, p2)

                new_individuals.append(self.mutation.mutate(c1))
                if len(new_individuals) < len(self.population.individuals):
                    new_individuals.append(self.mutation.mutate(c2))

            self.population.individuals = new_individuals

            print(f"Gen {gen}: Best = {best.fitness()}")

        return self.population.get_best()

