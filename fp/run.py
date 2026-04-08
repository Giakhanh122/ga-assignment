import src.onemax as onemax
import src.knapsack as knapsack

import json
import matplotlib.pylab as plt

def plot_result(generations, history):
    plt.plot(range(generations), history)
    plt.xlabel("generations")
    plt.ylabel("fitness")
    plt.grid()
    plt.show()

def get_json(problem_name ,best, best_fitness, runtime):
    result = {
        "Problem" : problem_name,
        "Result"  : best,
        "Fitness" : best_fitness,
        "Runtime" : runtime
    }
    with open("result.json", "w") as f:
        json.dump(result, f, indent = 4)

# One Max
generations = 100
best, best_fitness, history, runtime = onemax.ga(generations=generations)

# print(history)

    
plot_result(generations, history)
get_json("One Max", best, best_fitness, runtime)
# Knapsack
# print(knapsack.ga())

