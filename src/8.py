import py5


def settings():
    py5.size(250, 335)


def loc(x, y):
    return x + y * py5.width


def setup():
    img = py5.load_image("../assets/joconde.jpg")
    img2 = py5.create_image(250, 335, py5.RGB)

    Lr = [py5.red(i) for i in img.pixels]
    Lg = [py5.green(i) for i in img.pixels]
    Lb = [py5.blue(i) for i in img.pixels]

    for x in range(1, py5.width - 1):
        for y in range(1, py5.height - 1):
            indices = [
                loc(x - 1, y - 1), loc(x, y - 1), loc(x + 1, y - 1),
                loc(x - 1, y), loc(x, y), loc(x + 1, y),
                loc(x - 1, y + 1), loc(x, y + 1), loc(x + 1, y + 1)
            ]

            reds = [Lr[i] for i in indices]
            greens = [Lg[i] for i in indices]
            blues = [Lb[i] for i in indices]

            r = -reds[1] - reds[3] + 5 * reds[4] - reds[5] - reds[7]
            g = -greens[1] - greens[3] + 5 * greens[4] - greens[5] - greens[7]
            b = -blues[1] - blues[3] + 5 * blues[4] - blues[5] - blues[7]

            index = loc(x, y)
            img2.pixels[indices[4]] = py5.color(r, g, b)

    py5.image(img2, 0, 0)
    py5.image(img, 0, 0, 63, 84)


py5.run_sketch()
