from src.GA import OneMax_GeneticAlgorithm, KnapSack_GeneticAlgorithm
from src.selection import OneMaxSelection, KnapSackSelection
from src.crossover import OnePointCrossover
from src.mutation import BitFlipMutation
from src.population import Population
from src.items import Items

import json
import random

SEED = 42
POP_SIZE = 100
LENGTH = 100
GENERATIONS = 300
MUTATION_PROB = 1 / LENGTH



def plot_result(history, title_=""):
    import matplotlib.pyplot as plt
    plt.plot(range(len(history)), history)
    plt.title(title_)
    plt.xlabel("generations")
    plt.ylabel("fitness")
    plt.grid()
    plt.show()


def get_json(problem, best, best_fitness, runtime):
    data = {
        "Problem": problem,
        "Best Solution": best,
        "Best Fitness": best_fitness,
        "Runtime": runtime,
    }
    with open("result.json", "w") as f:
        json.dump(data, f, indent=4)


def run_one_max(*, seed=SEED, population_size=POP_SIZE, length=LENGTH, generations=GENERATIONS, mutation_prob=MUTATION_PROB, title_="One max problem"):
    random.seed(seed)
    population = Population(size=population_size, length=length)
    ga = OneMax_GeneticAlgorithm(
        population=population,
        selection=OneMaxSelection(),
        crossover=OnePointCrossover(length=length),
        mutation=BitFlipMutation(prob=mutation_prob),
        generations=generations,
    )
    best, best_fitness, history, runtime = ga.run()
    print(best)
    print("Best fitness : ",best_fitness)
    # print(history)
    print("Runtime : ",runtime)

    plot_result(history, title_)
    get_json("One Max", best, best_fitness, runtime)
    return best, best_fitness, history, runtime


def run_knap_sack(seed=SEED, population_size=POP_SIZE, length=LENGTH, generations=GENERATIONS, mutation_prob=MUTATION_PROB, weights=None, values=None, title_="Knap sack problem"):
    random.seed(seed)
    population = Population(size=population_size, length=length)
    items = Items(numberOfItems=length, weights=weights, values=values)
    ga = KnapSack_GeneticAlgorithm(
        population=population,
        selection=KnapSackSelection(),
        crossover=OnePointCrossover(length=length),
        mutation=BitFlipMutation(prob=mutation_prob),
        generations=generations,
        items=items,
    )
    best, best_fitness, history, runtime = ga.run()
    print(best)
    print("Best fitness : ",best_fitness)
    # print(history)
    print("Runtime : ",runtime)
    plot_result(history, title_)
    get_json("Knapsack", best, best_fitness, runtime)
    return best, best_fitness, history, runtime



# onemax_pop = Population(size=50, length=100)
# generations = 100
# ga_onemax = OneMax_GeneticAlgorithm(
#     population=onemax_pop,
#     selection=OneMaxSelection(),
#     crossover=OnePointCrossover(length=100),
#     mutation=BitFlipMutation(prob=0.01),
#     generations=generations
# )

# knapsack_pop = Population(size=50, length=100)
# items = Items(numberOfItems=100)
# ga_knapsack = KnapSack_GeneticAlgorithm(
#     population=knapsack_pop,
#     selection=KnapSackSelection(),
#     crossover=OnePointCrossover(length=100),
#     mutation=BitFlipMutation(prob=0.01),
#     generations=generations,
#     items=items
# )


# best, best_fitness, onemax_fitness_history, runtime = ga_onemax.run()
# print(best)
# print(best_fitness)
# print(onemax_fitness_history)
# print(runtime)

# plot_result(generations, onemax_fitness_history)
# get_json("One Max", best, best_fitness, runtime)




# best, knapsack_fitness_history = ga_knapsack.run()
# print("Best:", best)
# print("Fitness:", best.knapsack_fitness(items))
# print(knapsack_fitness_history)

if __name__ == "__main__":
    print("__ ONE MAX ___")
    run_one_max()
    print("__ KNAPSACK ___")
    run_knap_sack()