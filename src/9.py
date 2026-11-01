import py5


def settings():
    py5.size(250, 335)


def loc(x, y):
    return x + y * py5.width


def blur(img):
    result = py5.create_image(img.width, img.height, py5.RGB)
    img.load_pixels()
    result.load_pixels()

    for x in range(1, py5.width - 1):
        for y in range(1, py5.height - 1):
            indices = [
                loc(x - 1, y - 1), loc(x, y - 1), loc(x + 1, y - 1),
                loc(x - 1, y), loc(x, y), loc(x + 1, y),
                loc(x - 1, y + 1), loc(x, y + 1), loc(x + 1, y + 1),
            ]
            red = sum(py5.red(img.pixels[i]) for i in indices) / 9
            green = sum(py5.green(img.pixels[i]) for i in indices) / 9
            blue = sum(py5.blue(img.pixels[i]) for i in indices) / 9
            blurred = py5.color(red, green, blue)

            for index in indices:
                result.pixels[index] = blurred

    result.update_pixels()
    return result


def setup():
    img = py5.load_image("../assets/joconde.jpg")
    py5.image(blur(img), 0, 0)
    py5.image(img, 0, 0, 63, 84)


py5.run_sketch()
