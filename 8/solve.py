WIDTH = 25
HEIGHT = 6
PIXELS_PER_LAYER = WIDTH * HEIGHT


def load():
    with open("input.txt") as f:
        pixels = f.read().strip()
    return pixels


pixels = load()
layers = []
for i in range(0, len(pixels), PIXELS_PER_LAYER):
    layers.append(pixels[i : i + PIXELS_PER_LAYER])

zeroes = [layer.count("0") for layer in layers]
min_zeroes = zeroes.index(min(zeroes))
print(f'Part 1: {layers[min_zeroes].count("1") * layers[min_zeroes].count("2")}')

image = ["2"] * PIXELS_PER_LAYER
for layer in layers:
    for index, pixel in enumerate(layer):
        if image[index] != "2":
            continue
        if pixel == "0":
            image[index] = " "
        elif pixel == "1":
            image[index] = "X"

print("Part 2:")
for y in range(HEIGHT):
    offset = y * WIDTH
    print("".join(image[offset : offset + WIDTH]))
