import random
from functools import reduce

# n = 100 items


def create_chromosome(length : int):
    return [random.randint(0,1) for _ in range(length)]

def fitness(chromosome : list, weights : list, values : list, capacity: int):
    length = len(chromosome)
    cap = sum([weights[_] for _ in range(length) if chromosome[_]])
    return sum([values[_] for _ in range(length) if chromosome[_]]) if cap <= capacity else 0

def selection(Population : list, weights, values, capacity, sample : int = 3):
    selected = random.sample(Population, k=sample)
    return max(selected, key=lambda x : fitness(x, weights, values, capacity))

def crossover(p1, p2):
    point = random.randint(0, len(p1) - 1)
    child1 =  p1[:point] + p2[point:]
    child2 =  p2[:point] + p1[point:]
    return child1, child2


def mutate(individual, prob=0.02):
    return [bit if random.random() > prob else 1 - bit for bit in individual]

def next_generation(population, mutation_prob, weights, values, capacity):
    n = len(population)
    children = [
        child
        for _ in range((n + 1) // 2)
        for child in crossover(selection(population, weights, values, capacity), selection(population, weights, values, capacity))
    ]
    #debug
    print(fitness(max(children, key= lambda x : fitness(x, weights, values, capacity)), weights, values, capacity))
    return [mutate(c, mutation_prob) for c in children[:n]]

def ga(length = 100, population_size = 50,mutation_prob =  0.01 , generations = 500):

    population = [create_chromosome(length) for _ in range(population_size)]
    
    weights = [random.randint(1,50) for _ in range(length)]
    values  = [random.randint(1,20) for _ in range(length)]

    capacity = (int)(0.4 * sum(weights))

    
    final_gen = reduce(lambda x, _ : next_generation(x, mutation_prob, weights, values, capacity), range(generations), population)
    result = max(final_gen, key=lambda x : fitness(x, weights, values, capacity))
    return result
