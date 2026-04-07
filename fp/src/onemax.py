import random
from functools import reduce



def create_individual(length : int):
    return [random.randint(0,1) for _ in range(length)]

def fitness(bits : list):
    return sum(bits)

def selection(Population : list, sample : int = 3):
    selected = random.sample(Population, k=sample)
    return max(selected, key=fitness)

def crossover(p1, p2):
    point = random.randint(0, len(p1))
    child1 =  p1[:point] + p2[point:]
    child2 =  p2[:point] + p1[point:]
    return child1, child2


def mutate(individual, prob=0.02):
    return [bit if random.random() > prob else 1 - bit for bit in individual]

def next_generation(population, mutation_prob):
    n = len(population)
    children = [
        child
        for _ in range((n + 1) // 2)
        for child in crossover(selection(population), selection(population))
    ]
    return [mutate(c, mutation_prob) for c in children[:n]]

def ga(length = 100, population_size = 50,mutation_prob =  0.01 , generations = 80):
    population = [create_individual(length) for _ in range(population_size)]
    final_gen = reduce(lambda x, _ : next_generation(x, mutation_prob), range(population_size), population)
    return max(final_gen, key=fitness)

def main():
    print(ga())

if __name__ == "__main__":
    main()