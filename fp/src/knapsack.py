import random
from functools import reduce
import time
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
    best = max(population, key=lambda x: fitness(x, weights, values, capacity))
    children = [best]

    while len(children) < n:
        p1 = selection(population, weights, values, capacity)
        p2 = selection(population, weights, values, capacity)
        c1, c2 = crossover(p1, p2)
        children.append(mutate(c1, mutation_prob))
        if len(children) < n:
            children.append(mutate(c2, mutation_prob))

    return children

def ga(length = 100, population_size = 50,mutation_prob =  0.01 , generations = 500, weights=None, values=None, capacity=None):
    start = time.time()

    population = [create_chromosome(length) for _ in range(population_size)]
    if weights is None:
        weights = [random.randint(1,50) for _ in range(length)]
    if values is None:
        values = [random.randint(1,20) for _ in range(length)]
    if capacity is None:
        capacity = int(0.4 * sum(weights))
        
    history = []
    best_so_far = max(population, key=lambda x: fitness(x, weights, values, capacity))

    for _ in range(generations):
        population = next_generation(population, mutation_prob, weights, values, capacity)
        current_best = max(population, key=lambda x: fitness(x, weights, values, capacity))
        best_so_far = max([best_so_far, current_best], key=lambda x: fitness(x, weights, values, capacity))
        history.append(fitness(best_so_far, weights, values, capacity))
    
    end = time.time()
    runtime = end - start
    
    best = best_so_far
    best_fitness = fitness(best, weights, values, capacity)
    return best, best_fitness, history, runtime
