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


def black_and_white(img):
    result = img.copy()
    result.load_pixels()

    for index, pixel in enumerate(result.pixels):
        value = 0 if py5.red(pixel) < 127 else 255
        result.pixels[index] = py5.color(value, value, value)

    result.update_pixels()
    return result


def setup():
    img = py5.load_image("../assets/joconde.jpg")
    gray_img = gray_filter(img)
    py5.image(black_and_white(gray_img), 0, 0)
    py5.image(img, 0, 0, 62, 84)


py5.run_sketch()
