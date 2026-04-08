import random
from .abstract import SelectionStrategy, MutationStrategy, CrossoverStrategy
from .items import Items
from .chromosome import Chromosome
from .population import Population
from .selection import OneMaxSelection, KnapSackSelection
from .mutation import BitFlipMutation
from .crossover import OnePointCrossover

import time


class OneMax_GeneticAlgorithm:
    def __init__(self, population, selection, crossover, mutation, generations):
        self.population = population
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.generations = generations
        self.history = []
    def run(self):
        start = time.time()
        for gen in range(self.generations):
            new_individuals = []

            # elitism
            best = self.population.get_best_oneMax()
            new_individuals.append(best)

            while len(new_individuals) < len(self.population.individuals):
                p1 = self.selection.select(self.population)
                p2 = self.selection.select(self.population)

                c1, c2 = self.crossover.crossover(p1, p2)

                new_individuals.append(self.mutation.mutate(c1))
                if len(new_individuals) < len(self.population.individuals):
                    new_individuals.append(self.mutation.mutate(c2))

            self.population.individuals = new_individuals
            current_fitness = best.onemax_fitness()
            self.history.append(current_fitness)
            # debug
            # print(f"Gen {gen}: Best = {current_fitness}")
        end = time.time()
        runtime = end - start
        
        best = self.population.get_best_oneMax()
        best_fitness = best.onemax_fitness()
        
        return best.data(), best_fitness, self.history, runtime

class KnapSack_GeneticAlgorithm:
    def __init__(self, population, selection, crossover, mutation, generations, items : Items):
        self.population = population
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.generations = generations
        self.items = items
        self.history = []

    def run(self):
        start = time.time()
        for gen in range(self.generations):
            new_individuals = []

            # elitism
            best = self.population.get_best_knapSack(self.items)
            new_individuals.append(best)

            while len(new_individuals) < len(self.population.individuals):
                p1 = self.selection.select(self.population, self.items)
                p2 = self.selection.select(self.population, self.items)

                c1, c2 = self.crossover.crossover(p1, p2)

                new_individuals.append(self.mutation.mutate(c1))
                if len(new_individuals) < len(self.population.individuals):
                    new_individuals.append(self.mutation.mutate(c2))

            self.population.individuals = new_individuals
            
            current_fitness = best.knapsack_fitness(self.items)
            self.history.append(current_fitness)
            # debug
            # print(f"Gen {gen}: Best = {current_fitness}")
        end = time.time()
        runtime = end - start
        
        best = self.population.get_best_knapSack(self.items)
        best_fitness = best.knapsack_fitness()
        
        return best.data(), best_fitness, self.history, runtime