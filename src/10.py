import py5

"""

!!!!!! LE PROGRAMME PREND DU TEMPS A CHARGER !!!!!!!!!!

Voici quelques matrices que j'ai essayé :
    
# Flou moyen 
a = 1/9.0
matrix = [[a,a,a],
          [a,a,a],
          [a,a,a]]

# Flou gaussien 
matrix = [[1/16.0, 2/16.0, 1/16.0],
          [2/16.0, 4/16.0, 2/16.0],
          [1/16.0, 2/16.0, 1/16.0]]

# Éclaircir 
matrix = [[0,0,0],
          [0,1.5,0],
          [0,0,0]]
"""

matrix = [[-1, -1, -1],
          [-1, 9, -1],
          [-1, -1, -1]]

def convolution(x, y, matrix, img):
    rtotal = 0.0
    gtotal = 0.0
    btotal = 0.0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            index = (x - i) + (y - j) * py5.width
            rtotal = rtotal + py5.red(img.pixels[index]) * matrix[i + 1][j + 1]
            gtotal = gtotal + py5.green(img.pixels[index]) * matrix[i + 1][j + 1]
            btotal = btotal + py5.blue(img.pixels[index]) * matrix[i + 1][j + 1]

    # On doit les convertir en entier sinon py5 retourne une erreur.
    rtotal = int(py5.constrain(rtotal, 0, 255))
    gtotal = int(py5.constrain(gtotal, 0, 255))
    btotal = int(py5.constrain(btotal, 0, 255))
    return py5.color(rtotal, gtotal, btotal)


def settings():
    py5.size(408, 272)


def setup():
    global img
    global img2
    # print(matrix[2][2])
    py5.frame_rate(30)
    img2 = py5.create_image(408, 272, py5.RGB)
    img = py5.load_image("../assets/photocasa.png")
    for x in range(1, 407):
        for y in range(1, 271):
            index = x + y * py5.width
            c = convolution(x, y, matrix, img)
            img2.pixels[index] = c
    # py5.update_pixels()
    py5.image(img2, 0, 0)
    py5.image(img, 0, 0, 102, 68)


py5.run_sketch()
