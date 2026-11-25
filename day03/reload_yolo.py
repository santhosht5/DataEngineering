def xyxy_to_yolo(box, width, height, class_id):
    left, top, right, bottom = box

    bw = right - left
    bh = bottom - top

    cx = left + bw / 2
    cy = top + bh / 2

    return f"{class_id} {cx / width:.6f} {cy / height:.6f} {bw / width:.6f} {bh / height:.6f}"

box = (10, 20, 50, 60)

# Convert XYXY to YOLO format
yolo_line = xyxy_to_yolo(box, 100, 100, 1)

print("YOLO format:", yolo_line)

def yolo_to_xyxy(line, width, height):
    class_id, cx, cy, bw, bh = line.split()
    cx, cy, bw, bh = (float(v) for v in (cx, cy, bw, bh))

    cx *= width
    cy *= height
    bw *= width
    bh *= height

    left = cx - bw / 2
    top = cy - bh / 2

    return int(class_id), (left, top, left + bw, top + bh)


# Read the YOLO label file
with open("labels/example_100.txt", "r") as file:
    line = file.read().strip()

# Convert YOLO coordinates back to xyxy
class_id, box = yolo_to_xyxy(line, 100, 100)

print("Class ID:", class_id)
print("Original bounding box:", box)