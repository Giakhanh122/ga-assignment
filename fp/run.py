import src.onemax as onemax
import src.knapsack as knapsack

import json
import random

SEED = 42
POP_SIZE = 100
LENGTH = 100
GENERATIONS = 300
MUTATION_PROB = 1 / LENGTH


def plot_result(history):
    import matplotlib.pyplot as plt
    plt.plot(range(len(history)), history)
    plt.xlabel("generations")
    plt.ylabel("fitness")
    plt.grid()
    plt.show()


def get_json(problem_name, best, best_fitness, runtime):
    result = {
        "Problem": problem_name,
        "Result": best,
        "Fitness": best_fitness,
        "Runtime": runtime,
    }
    with open("result.json", "w") as f:
        json.dump(result, f, indent=4)


def run_one_max(*, length=LENGTH, population_size=POP_SIZE, mutation_prob=MUTATION_PROB, generations=GENERATIONS, seed=SEED):
    random.seed(seed)
    best, best_fitness, history, runtime = onemax.ga(
        length=length,
        population_size=population_size,
        mutation_prob=mutation_prob,
        generations=generations,
    )
    print(best)
    print("Best fitness : ",best_fitness)
    # print(history)
    print("Runtime : ",runtime)

    plot_result(history)
    get_json("One Max", best, best_fitness, runtime)
    return best, best_fitness, history, runtime


def run_knap_sack(*, length=LENGTH, population_size=POP_SIZE, mutation_prob=MUTATION_PROB, generations=GENERATIONS, seed=SEED, weights=None, values=None, capacity=None):
    random.seed(seed)
    best, best_fitness, history, runtime = knapsack.ga(
        length=length,
        population_size=population_size,
        mutation_prob=mutation_prob,
        generations=generations,
        weights=weights,
        values=values,
        capacity=capacity,
    )
    print(best)
    print("Best fitness : ",best_fitness)
    # print(history)
    print("Runtime : ",runtime)
    plot_result(history)
    get_json("Knapsack", best, best_fitness, runtime)
    return best, best_fitness, history, runtime


if __name__ == "__main__":
    print("__ ONE MAX ___")
    run_one_max()
    print("__ KNAPSACK ___")
    run_knap_sack()


