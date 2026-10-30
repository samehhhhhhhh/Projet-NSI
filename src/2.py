import py5


def settings():
    py5.size(400, 300)


# Programme de base
def base():
    for x in range(0, 400, 1):

        for y in range(0, 300, 1):

            # Index du pixel
            index = x + y * py5.width

            # S'il est multilple de 10, alors il doit être rouge. Sinon il doit être vert
            if index % 10 == 0:
                py5.pixels[index] = py5.color(255, 0, 0)
            else:
                py5.pixels[index] = py5.color(0, 255, 0)


# Programme avec la figure en haut à gauche
def top_left():
    for x in range(0, 200, 1):

        for y in range(0, 150, 1):

            # Index du pixel
            index = x + y * py5.width

            # S'il est multilple de 10, alors il doit être rouge. Sinon il doit être vert
            if index % 10 == 0:
                py5.pixels[index] = py5.color(255, 0, 0)
            else:
                py5.pixels[index] = py5.color(0, 255, 0)


def bottom_right():
    for x in range(200, 400, 1):

        for y in range(150, 300, 1):

            # Index du pixel
            index = x + y * py5.width

            # S'il est multilple de 10, alors il doit être rouge. Sinon il doit être vert
            if index % 10 == 0:
                py5.pixels[index] = py5.color(255, 0, 0)
            else:
                py5.pixels[index] = py5.color(0, 255, 0)

"""
    J'ai préféré faire cela un peu différement pour écrire moins de code,
    En gros j'ai tout d'abord catégorisé les pixels dans des "blocs" 
    
    pour ensuite en fonction du bloc et les coordonnées du bloc,
    savoir quel couleur utiliser
"""
def carreaux():
    for x in range(400):
        for y in range(300):

            # Index du pixel
            index = x + y * py5.width

            position = [int(x / (py5.width / 4)) + 1, int(y / (py5.height / 4)) + 1]

            if position[1] % 2 == 1:  # Impair
                if position[0] % 2 == 0:  # pair
                    py5.pixels[index] = py5.color(255)
                else:
                    py5.pixels[index] = py5.color(0)
            else:  # On fait l'inverse
                if position[0] % 2 == 1:  # impair
                    py5.pixels[index] = py5.color(255)
                else:
                    py5.pixels[index] = py5.color(0)


def setup():
    py5.load_pixels()

    carreaux()

    py5.update_pixels()


py5.run_sketch()
