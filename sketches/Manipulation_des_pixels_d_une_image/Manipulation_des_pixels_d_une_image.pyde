
size(250, 335)

img=loadImage("data/joconde.jpg")

img2 = createImage(250, 335, RGB)
def base():
    
    for x in range(250):
        for y in range(335):
            
            index = x +y*width
            
            r = red(img.pixels[index])
            g = green(img.pixels[index])
            b = blue(img.pixels[index])
            
            img2.pixels[index] = color(255, g, b)

# base()

# ---------------------------------------------------------------------------------------------------------

# Réalisons une fonction qui nous permet de passer les valeurs r, g, b de l'image filtrée
# si jamais la valeur passée n'appartient pas à l'intervalle [0, 255] Alors on prendra la valeur existante. 

# Retourne True si val appartient à l'intervalle [0, 255] sinon False
def appartient(val):
     return 0 <= val <= 255
     
# Transforme img2 en un filtre de couleur de img
def create_filter(r, g, b):
    
    for x in range(250):
        for y in range(335):
            
            index = x +y*width
            
            rr, gg, bb = r, g, b
            
            if(not appartient(r)):
                rr = red(img.pixels[index])
            if(not appartient(g)):
                
                gg = green(img.pixels[index])
            if(not appartient(b)):
                
                bb = blue(img.pixels[index])
            
            img2.pixels[index] = color(rr, gg, bb)
    
create_filter(123, 256, 255)

updatePixels()
image(img2, 0, 0)
image(img, 0, 0, 62, 83)
