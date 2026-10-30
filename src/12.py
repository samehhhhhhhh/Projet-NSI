import py5


def settings():
    py5.size(250, 335)


# Pourquoi ne pas essayer de faire une symétrique centrale ?

def sym_verticale(img, img2):
    for x in range(250):
        for y in range(335):
            indices = [x + y * py5.width, x + (py5.height - 1 - y) * py5.width]
            
            img2.pixels[indices[0]] = img.pixels[indices[1]]
            img2.pixels[indices[1]] = img.pixels[indices[0]]


def sym_horizontale(img, img2):
    for x in range(250):
        for y in range(335):
            indices = [x + y * py5.width, (py5.width - 1 - x) + y * py5.width]

            img2.pixels[indices[0]] = img.pixels[indices[1]]
            img2.pixels[indices[1]] = img.pixels[indices[0]]


def sym_centrale(img, img2):
    for x in range(250):
        for y in range(335):
            indices = [
                x + y * py5.width,
                (py5.width - 1 - x) + (py5.height - 1 - y) * py5.width
            ]

            img2.pixels[indices[0]] = img.pixels[indices[1]]
            img2.pixels[indices[1]] = img.pixels[indices[0]]


def setup():
    img = py5.load_image("../assets/joconde.jpg")
    img2 = py5.create_image(250, 335, py5.RGB)

    sym_centrale(img, img2)

    py5.image(img2, 0, 0)
    py5.image(img, 0, 0, 63, 84)


py5.run_sketch()
