import py5


def settings():
    py5.size(310, 309)


def loc(x, y, width):
    return x + y * width


def remove_noise(img):
    current = img
    next_img = py5.create_image(img.width, img.height, py5.RGB)
    threshold = 20

    for iteration in range(3):
        print("Starting iteration", iteration + 1)
        current.load_pixels()
        next_img.load_pixels()

        for index, pixel in enumerate(current.pixels):
            next_img.pixels[index] = pixel

        for x in range(1, img.width - 1):
            for y in range(1, img.height - 1):
                values = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        index = loc(x + i, y + j, img.width)
                        values.append(py5.red(current.pixels[index]))

                median = sorted(values)[4]
                index = loc(x, y, img.width)
                center = py5.red(current.pixels[index])
                if abs(center - median) > threshold:
                    next_img.pixels[index] = py5.color(median, median, median)

        next_img.update_pixels()
        print("Finished iteration", iteration + 1)
        current, next_img = next_img, current
        threshold += 5

    return current


def setup():
    img = py5.load_image(
        "../sketches/Eliminer_le_bruit_d_une_image/data/bruit.png"
    )
    py5.image(remove_noise(img), 0, 0)
    py5.image(img, 0, 0, 92, 90)


py5.run_sketch()
