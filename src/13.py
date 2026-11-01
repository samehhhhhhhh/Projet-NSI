import py5


def settings():
    py5.size(250, 335)


def setup():
    global img
    img = py5.load_image("../assets/joconde.jpg")
    py5.background(0)


def draw():
    x = int(py5.random(py5.width))
    y = int(py5.random(py5.height))
    pixel = img.pixels[x + y * py5.width]

    py5.no_stroke()
    py5.fill(pixel, 128)
    py5.rect(x, y, 10, 10)


py5.run_sketch()
