import py5


matrix = [
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
]


def settings():
    py5.size(692, 507)


def convolution(x, y, img):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            index = (x - i) + (y - j) * img.width
            pixel = img.pixels[index]
            gray = (py5.red(pixel) + py5.green(pixel) + py5.blue(pixel)) / 3
            total += gray * matrix[i + 1][j + 1]

    return py5.color(int(py5.constrain(abs(total), 0, 255)))


def setup():
    img = py5.load_image(
        "../sketches/Detection_de_contours/data/parc.jpg"
    )
    result = py5.create_image(img.width, img.height, py5.RGB)
    img.load_pixels()
    result.load_pixels()

    for x in range(1, img.width - 1):
        for y in range(1, img.height - 1):
            result.pixels[x + y * img.width] = convolution(x, y, img)

    result.update_pixels()
    py5.image(result, 0, 0)
    py5.image(img, 0, 0, 69, 50)


py5.run_sketch()
