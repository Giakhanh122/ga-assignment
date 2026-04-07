import random

class Individual:
    def __init__(self, bits):
        self.individual = bits
    @classmethod

    def random(self, bit_length):
        gens = [random.randint(0,1) for _ in range(bit_length)]
        return Individual(gens)

    def fitness(self):
        return sum(self.individual)
    
    def __str__(self): 
        return str(self.individual)
    
class GA:
    def __init__(self, length = 100, population_size = 50, mutation_prob =  0.01 , generations_count = 80):
        self.population = [Individual.random(length) for _ in range(population_size)]
        self.population_size = population_size
        self.mutation_prob = mutation_prob
        self.generations_count = generations_count
        self.length = length

    def selection(self):
        selected = random.sample(self.population, k=3)
        return max(selected, key= lambda indi : indi.fitness())
    
    def crossover(self, p1 : Individual , p2 : Individual):
        point = random.randint(0, self.length - 1)
        child1 =  Individual(p1.individual[:point] + p2.individual[point:])
        child2 =  Individual(p2.individual[:point] + p1.individual[point:])
        return child1, child2
    def mutate(self, indi : Individual):
        return Individual([bit if random.random() > self.mutation_prob else 1 - bit for bit in indi.individual])
    
    def next_generation(self):
        next_gen = []
        for _ in range((self.population_size + 1) // 2):
            for child in self.crossover(self.selection(), self.selection()):
                next_gen.append(self.mutate(child))
        return next_gen

    def run(self):
        for _ in range(self.generations_count):
            self.population = self.next_generation()
            best = max(self.population, key = lambda indi : indi.fitness())
            # print(f"Gen {_}: Best fitness = {best.fitness()}")
        return best

