
import py5

def settings():
    py5.size(250, 335)

def base(img, img2):
    
    for x in range(250):
        for y in range(335):
            
            index = x + y * py5.width
            
            r = py5.red(img.pixels[index])
            g = py5.green(img.pixels[index])
            b = py5.blue(img.pixels[index])
            
            img2.pixels[index] = py5.color(255, g, b)

# ---------------------------------------------------------------------------------------------------------

# Réalisons une fonction qui nous permet de passer les valeurs r, g, b de l'image filtrée
# si jamais la valeur passée n'appartient pas à l'intervalle [0, 255] Alors on prendra la valeur existante. 

# Retourne True si val appartient à l'intervalle [0, 255] sinon False
def appartient(val):
    return 0 <= val <= 255
   
# Transforme img2 en un filtre de couleur de img
def create_filter(r, g, b, img, img2):
    for x in range(250):
        for y in range(335):
            index = x + y * py5.width

            rr, gg, bb = r, g, b

            if not appartient(r):
                rr = py5.red(img.pixels[index])
            if not appartient(g):
                gg = py5.green(img.pixels[index])
            if not appartient(b):
                bb = py5.blue(img.pixels[index])

            img2.pixels[index] = py5.color(rr, gg, bb)


def setup():
    img = py5.load_image("../assets/joconde.jpg")
    img2 = py5.create_image(250, 335, py5.RGB)

    create_filter(256, 255, 256, img, img2)
    # base()
    py5.image(img2, 0, 0)
    py5.image(img, 0, 0, 62, 83)


py5.run_sketch()
