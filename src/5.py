import py5


def settings():
    py5.size(250, 335)


def gray_filter(img):
    img2 = py5.create_image(img.width, img.height, py5.RGB)
    img.load_pixels()
    img2.load_pixels()

    for index, pixel in enumerate(img.pixels):
        gray = (py5.red(pixel) + py5.green(pixel) + py5.blue(pixel)) / 3
        img2.pixels[index] = py5.color(gray, gray, gray)

    img2.update_pixels()
    return img2


def setup():
    img = py5.load_image("../assets/joconde.jpg")
    py5.image(gray_filter(img), 0, 0)
    py5.image(img, 0, 0, 62, 83)


py5.run_sketch()
