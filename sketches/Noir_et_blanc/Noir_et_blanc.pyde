size(250,335)
img = loadImage("data/joconde.jpg")

#Fonctions de sami venant de l'exercice du filtrage par seuil
#---------------------------------------------------------------------
def appartient(val):
    return val >= 0 and val <= 255

def appliquer_seuil(val, var):
    if var < val:
        return 0
    else:
        return 255

def filtrage_par_seuil(seuil_r, seuil_g, seuil_b, i):
    
    for x in range(250):
        for y in range(334):
            index = x + y * width
            
            r = red(i.pixels[index])
            g = green(i.pixels[index])
            b = blue(i.pixels[index])
            
            if appartient(seuil_r):
                r = appliquer_seuil(seuil_r, r)
            
            if appartient(seuil_g):
                g = appliquer_seuil(seuil_g, g)
            
            if appartient(seuil_b):
                b = appliquer_seuil(seuil_b, b)
                
            i.pixels[index] = color(r, g, b)
            
#---------------------------------------------------------------------

#Fonction qui applique un filtre noir et blanc a une image

def gray_filter(i):
    img2 = createImage(250,335, RGB)

    for x in range(i.width):
        for y in range(i.height):
            
            index = x + y * i.width
            
            newColor = (red(i.pixels[index]) + green(i.pixels[index]) + blue(i.pixels[index])) / 3
            img2.pixels[index] = color(newColor, newColor, newColor)
            
    return img2

def filtre_noir_et_blanc(i):
    img2=i.copy()
    
    filtrage_par_seuil(127,127,127,img2)
    
    return img2

updatePixels()

gray_img = gray_filter(img)

image(filtre_noir_et_blanc(gray_img),0,0)
image(img,0,0,62,84) 
            
            
            
            
            
            
            
            
            
            
