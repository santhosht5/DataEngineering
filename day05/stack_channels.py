import numpy as np
from PIL import Image

SIZE = 8


def solid(rgb: tuple[int, int, int]) -> np.ndarray:
    image = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)
    image[:, :] = rgb
    return image


def stack_rgb(frames: list[np.ndarray]) -> np.ndarray:
    # frames are RGB, shape (H, W, 3). Output is (9, H, W).
    channels = [frame[:, :, color] for frame in frames for color in range(3)]
    return np.stack(channels, axis=0)


frames = [
    solid((255, 0, 0)),  # t-2 red
    solid((0, 255, 0)),  # t-1 green
    solid((0, 0, 255)),  # t blue
]
stack9 = stack_rgb(frames)
assert stack9.shape == (9, SIZE, SIZE)
assert int(stack9[0].mean()) == 255
assert int(stack9[4].mean()) == 255
assert int(stack9[8].mean()) == 255
print("9-channel stack ok", stack9.shape)


mask = np.zeros((SIZE, SIZE), dtype=np.uint8)
mask[:, 4:] = 255
stack12 = np.concatenate([stack9, np.stack([mask, mask, mask], axis=0)], axis=0)
assert stack12.shape == (12, SIZE, SIZE)
assert int(stack12[9, 0, 0]) == 0
assert int(stack12[9, 0, 4]) == 255
assert int(stack12[11, 0, 4]) == 255

pages = [Image.fromarray(stack12[index]) for index in range(12)]
pages[0].save(
    "sample12.tif",
    save_all=True,
    append_images=pages[1:],
)
print("wrote sample12.tif")

with Image.open("sample12.tif") as img:
    count = 1

    try:
        while True:
            img.seek(count)
            count += 1
    except EOFError:
        pass

print("Total TIFF pages:", count)
