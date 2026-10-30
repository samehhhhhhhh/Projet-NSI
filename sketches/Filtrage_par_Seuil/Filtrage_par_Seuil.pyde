


size (250 , 335) 
img=loadImage("data/joconde.jpg")
img2=createImage(250, 335, RGB)

def base():
    
    for x in range(250):
        for y in range(334):
            index = x + y * width
            
            r = red(img.pixels[index])
            g = green(img.pixels[index])
            b = blue(img.pixels[index])
            
            if r < 127 :
                r = 0
            else:
                r = 255
            img2.pixels[index] = color(r, g, b)

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
        
def filtrage_par_seuil(seuil_r, seuil_g, seuil_b):
    
    for x in range(250):
        for y in range(334):
            index = x + y * width
            
            r = red(img.pixels[index])
            g = green(img.pixels[index])
            b = blue(img.pixels[index])
            
            if appartient(seuil_r):
                r = appliquer_seuil(seuil_r, r)
            
            if appartient(seuil_g):
                g = appliquer_seuil(seuil_g, g)
            
            if appartient(seuil_b):
                b = appliquer_seuil(seuil_b, b)
                
            img2.pixels[index] = color(r, g, b)
    
filtrage_par_seuil(127, 200, 256)
image(img2, 0, 0)
image(img, 0, 0, 62, 84)
