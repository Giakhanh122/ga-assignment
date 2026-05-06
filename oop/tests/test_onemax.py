import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # Go up to ga-assignment root
OOP_DIR = ROOT / "oop"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(OOP_DIR))

try:
    import oop.run as oop_run
except ImportError as error:
    raise SystemExit(f"Unable to import oop.run: {error}")

# Select which levels to run. Comment/uncomment or change the list.
SELECTED_LEVELS = ["small", "medium", "large"]
# SELECTED_LEVELS = ["small"]
# SELECTED_LEVELS = ["medium"]
# SELECTED_LEVELS = ["large"]

CASE_CONFIGS = {
    "small": {"length": 75, "title" : "One max small test : bit length 75"},
    "medium": {"length": 150, "title" : "One max small test : bit length 150"},
    "large": {"length": 230, "title" : "One max small test : bit length 230"},
}


def ensure_plot():
    try:
        import matplotlib
        backend = matplotlib.get_backend().lower()
    except ImportError:
        print("matplotlib is not installed. Charts are disabled.")
        oop_run.plot_result = lambda history: None
        return

    if backend in ("agg", "template", "pdf", "ps", "svg"):
        print(f"matplotlib backend '{backend}' is non-interactive. Charts are disabled.")
        oop_run.plot_result = lambda history: None


def run_onemax_case(name, config):
    length = config["length"]
    tit = config["title"]
    print("\n" + "=" * 80)
    print(f"OneMax test: {name}")
    print("=" * 80)
    print("Configuration:")
    print(f"  length        = {length}")
    print(f"  population    = {oop_run.POP_SIZE}")
    print(f"  generations   = {oop_run.GENERATIONS}")
    print(f"  mutation_prob = {oop_run.MUTATION_PROB}")
    print(f"  seed          = {oop_run.SEED}")
    print("-" * 80)

    ensure_plot()
    best, best_fitness, history, runtime = oop_run.run_one_max(length=length, title_=tit)

    print("-" * 80)
    print("Result:")
    print(f"  best_fitness   = {best_fitness}")
    print(f"  best_solution  = {best}")
    print(f"  history length = {len(history)}")
    print(f"  runtime        = {runtime:.4f} seconds")
    print(f"  expected sum   = {sum(best)}")
    if history:
        print(f"  final history  = {history[-1]}")
    print("=" * 80)


def main():
    print("Running OOP OneMax manual script tests")
    for level in SELECTED_LEVELS:
        config = CASE_CONFIGS.get(level)
        if config is None:
            print(f"Unknown level: {level}")
            continue
        run_onemax_case(level, config)


if __name__ == "__main__":
    main()