import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "fp"))

try:
    import fp.run as fp_run
except ImportError as error:
    raise SystemExit(f"Unable to import fp.run: {error}")

# Select which levels to run. Comment/uncomment or change the list.
SELECTED_LEVELS = ["small", "medium", "large"]
# SELECTED_LEVELS = ["small"]
# SELECTED_LEVELS = ["medium"]
# SELECTED_LEVELS = ["large"]

CASE_CONFIGS = {
    "small": {"length": 10},
    "medium": {"length": 50},
    "large": {"length": 100},
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


def run_onemax_case(name, config):
    length = config["length"]
    print("\n" + "=" * 80)
    print(f"OneMax test: {name}")
    print("=" * 80)
    print("Configuration:")
    print(f"  length        = {length}")
    print(f"  population    = {fp_run.POP_SIZE}")
    print(f"  generations   = {fp_run.GENERATIONS}")
    print(f"  mutation_prob = {fp_run.MUTATION_PROB}")
    print(f"  seed          = {fp_run.SEED}")
    print("-" * 80)

    ensure_plot()
    best, best_fitness, history, runtime = fp_run.run_one_max(length=length)

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
    print("Running OneMax manual script tests")
    for level in SELECTED_LEVELS:
        config = CASE_CONFIGS.get(level)
        if config is None:
            print(f"Unknown level: {level}")
            continue
        run_onemax_case(level, config)


if __name__ == "__main__":
    main()
