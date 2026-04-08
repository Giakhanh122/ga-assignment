from src.GA import *

import json
import matplotlib.pyplot as plt


def plot_result(generations, history):
    plt.plot(range(generations), history)
    plt.xlabel("generations")
    plt.ylabel("fitness")
    plt.grid()
    plt.show()
    
import json

def get_json(problem, best, best_fitness, runtime):
    data = {
        "Problem": problem,
        "Best Solution": best,
        "Best Fitness": best_fitness,
        "Runtime": runtime
    }

    with open("result.json", "w") as f:
        json.dump(data, f, indent=4)



onemax_pop = Population(size=50, length=100)
generations = 100
ga_onemax = OneMax_GeneticAlgorithm(
    population=onemax_pop,
    selection=OneMaxSelection(),
    crossover=OnePointCrossover(length=100),
    mutation=BitFlipMutation(prob=0.01),
    generations=generations
)

knapsack_pop = Population(size=50, length=100)
items = Items(numberOfItems=100)
ga_knapsack = KnapSack_GeneticAlgorithm(
    population=knapsack_pop,
    selection=KnapSackSelection(),
    crossover=OnePointCrossover(length=100),
    mutation=BitFlipMutation(prob=0.01),
    generations=generations,
    items=items
)


best, best_fitness, onemax_fitness_history, runtime = ga_onemax.run()
print(best)
print(best_fitness)
print(onemax_fitness_history)
print(runtime)

plot_result(generations, onemax_fitness_history)
get_json("One Max", best, best_fitness, runtime)




# best, knapsack_fitness_history = ga_knapsack.run()
# print("Best:", best)
# print("Fitness:", best.knapsack_fitness(items))
# print(knapsack_fitness_history)