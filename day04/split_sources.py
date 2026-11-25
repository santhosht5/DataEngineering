
import json
import random
from pathlib import Path

# Step 1: Define the settings
SEED = 42
SOURCES = [f"src{i:02d}" for i in range(10)]
VAL_COUNT = 2


# Step 2: Split sources into training and validation
def split_sources(sources: list[str], val_count: int, seed: int) -> dict:
    order = list(sources)

    # Shuffle the source names
    random.Random(seed).shuffle(order)

    # Select validation and training sources
    val = sorted(order[:val_count])
    train = sorted(order[val_count:])

    # Check that no source appears in both groups
    overlap = sorted(set(val) & set(train))

    if overlap:
        raise RuntimeError(f"leak: {overlap}")

    return {
        "seed": seed,
        "order": order,
        "train": train,
        "val": val
    }


# Step 3: Run the split and save the result
def main() -> None:
    result = split_sources(SOURCES, VAL_COUNT, SEED)

    # Save split.json in the current day04 folder
    out = Path(".")
    out.mkdir(parents=True, exist_ok=True)

    (out / "split.json").write_text(
        json.dumps(result, indent=2),
        encoding="utf-8"
    )

    print("Validation sources:", result["val"])
    print("Training sources:", result["train"])
    print("Saved split.json successfully!")


if __name__ == "__main__":
    main()
