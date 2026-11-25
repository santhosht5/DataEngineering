
import csv
from iou import iou

CASES = [
    {"id": "a", "existing": (0, 0, 2, 2), "generated": (0, 0, 2, 2), "nobody": False},
    {"id": "b", "existing": (0, 0, 2, 2), "generated": (1, 1, 3, 3), "nobody": False},
    {"id": "c", "existing": (0, 0, 2, 2), "generated": None, "nobody": True},
]

THRESHOLD = 0.5

rows = []

for case in CASES:

    # Rule 1: Check whether nobody is present
    if case["nobody"]:
        overlap = ""
        status = "no_positive"

    # Rule 2: Calculate IoU when a generated box exists
    else:
        overlap = iou(case["existing"], case["generated"])

        if overlap >= THRESHOLD:
            status = "matched"
        else:
            status = "unmatched"

    # Rule 3: Decide whether this row is trainable
    trainable = status in ("matched", "no_positive")

    rows.append({
        "id": case["id"],
        "iou": overlap,
        "status": status,
        "trainable": trainable
    })

# Write the results into a CSV file
with open("status.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "iou", "status", "trainable"]
    )
    writer.writeheader()
    writer.writerows(rows)

# Display the results
for row in rows:
    print(row)

print("\nstatus.csv created successfully!")
