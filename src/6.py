
import py5

def settings():
    py5.size(250 , 335) 

def base(img, img2):
    
    for x in range(250):
        for y in range(334):
            index = x + y * py5.width
            
            r = py5.red(img.pixels[index])
            g = py5.green(img.pixels[index])
            b = py5.blue(img.pixels[index])
            
            if r < 127 :
                r = 0
            else:
                r = 255
            img2.pixels[index] = py5.color(r, g, b)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Nous pouvons créer une fonction filtrage_par_seuil() qui prend trois nombres. Les nombres appartennant à l'intervalle 0, 255 seront considéré comme seuil
# Les autres seront ignorés.

def appartient(val):
    return val >= 0 and val <= 255

def appliquer_seuil(val, var):
    if var < val:
        return 0
    else:
        return 255
        
def filtrage_par_seuil(seuil_r, seuil_g, seuil_b, img, img2):
    
    for x in range(250):
        for y in range(334):
            index = x + y * py5.width
            
            r = py5.red(img.pixels[index])
            g = py5.green(img.pixels[index])
            b = py5.blue(img.pixels[index])
            
            if appartient(seuil_r):
                r = appliquer_seuil(seuil_r, r)
            
            if appartient(seuil_g):
                g = appliquer_seuil(seuil_g, g)
            
            if appartient(seuil_b):
                b = appliquer_seuil(seuil_b, b)
                
            img2.pixels[index] = py5.color(r, g, b)

def setup():

    img=py5.load_image("../assets/joconde.jpg")
    img2 = py5.create_image(250, 335, py5.RGB)

    filtrage_par_seuil(127, 200, 256, img, img2)

    py5.image(img2, 0, 0)
    py5.image(img, 0, 0, 62, 84)

py5.run_sketch()