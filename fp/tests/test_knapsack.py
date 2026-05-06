import sys
import random
from pathlib import Path


# Do you want json file ?
GET_JSON_FILE = False



ROOT = Path(__file__).resolve().parents[2]  # Go up to ga-assignment root
FP_DIR = ROOT / "fp"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(FP_DIR))

try:
    import fp.run as fp_run
    from fp.src import knapsack as fp_knapsack
except ImportError as error:
    raise SystemExit(f"Unable to import fp.run or fp.src.knapsack: {error}")

# Select which levels to run. Comment/uncomment or change the list.
SELECTED_LEVELS = ["small", "medium", "large"]
# SELECTED_LEVELS = ["small"]
# SELECTED_LEVELS = ["medium"]
# SELECTED_LEVELS = ["large"]

CASE_CONFIGS = {
    "small": {"length": 30, "seed": 42, "title" : "Knap sack small test : number of items: 30"},
    "medium": {"length": 50, "seed": 84, "title" : "Knap sack medium test : number of items: 50"},
    "large": {"length": 100, "seed": 126, "title" : "Knap sack large test : number of items: 100"},
}


def ensure_plot():
    try:
        import matplotlib
        backend = matplotlib.get_backend().lower()
    except ImportError:
        print("matplotlib is not installed. Charts are disabled.")
        fp_run.plot_result = lambda history: None
        return

    if backend in ("agg", "template", "pdf", "ps", "svg"):
        print(f"matplotlib backend '{backend}' is non-interactive. Charts are disabled.")
        fp_run.plot_result = lambda history: None


def generate_case_data(length, seed):
    rng = random.Random(seed)
    weights = [rng.randint(1, 50) for _ in range(length)]
    values = [rng.randint(1, 20) for _ in range(length)]
    capacity = int(0.4 * sum(weights))
    return weights, values, capacity


def run_knapsack_case(name, config):
    length = config["length"]
    seed = config["seed"]
    weights, values, capacity = generate_case_data(length, seed)
    tit = config["title"]
    print("\n" + "=" * 80)
    print(f"Knapsack test: {name}")
    print("=" * 80)
    print("Problem setup:")
    print(f"  length   = {length}")
    print(f"  seed     = {seed}")
    print(f"  capacity = {capacity}")
    print(f"  population    = {fp_run.POP_SIZE}")
    print(f"  generations   = {fp_run.GENERATIONS}")
    print(f"  mutation_prob = {fp_run.MUTATION_PROB}")
    print("-" * 80)
    print(f"  weights = {weights}")
    print(f"  values  = {values}")
    print("-" * 80)

    ensure_plot()
    best, best_fitness, history, runtime = fp_run.run_knap_sack(
        length=length,
        seed=seed,
        weights=weights,
        values=values,
        capacity=capacity,
        title_=tit,
        get_json_file=GET_JSON_FILE
    )

    selected_indices = [index for index, bit in enumerate(best) if bit]
    total_weight = sum(weight * bit for weight, bit in zip(weights, best))
    total_value = sum(value * bit for value, bit in zip(values, best))
    expected_fitness = fp_knapsack.fitness(best, weights, values, capacity)

    print("Result:")
    print(f"  best_fitness       = {best_fitness}")
    print(f"  computed_fitness   = {expected_fitness}")
    print(f"  best_solution      = {best}")
    print(f"  selected_indices   = {selected_indices}")
    print(f"  total_weight       = {total_weight}")
    print(f"  total_value        = {total_value}")
    print(f"  valid solution     = {total_weight <= capacity}")
    print(f"  history length     = {len(history)}")
    print(f"  runtime            = {runtime:.4f} seconds")
    if history:
        print(f"  final history      = {history[-1]}")
    print("=" * 80)


def main():
    print("Running FP Knapsack manual script tests")
    for level in SELECTED_LEVELS:
        config = CASE_CONFIGS.get(level)
        if config is None:
            print(f"Unknown level: {level}")
            continue
        run_knapsack_case(level, config)


if __name__ == "__main__":
    main()