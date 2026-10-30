size(250, 335)

img=loadImage("data/joconde.jpg")
img2 = createImage(250, 335, RGB)

def sym_verticale():
    for x in range(250):
        for y in range(335):
            indices = [ x+y*width, x+(height-1-y)*width]
            
            img2.pixels[indices[0]]= img.pixels[indices[1]]
            img2.pixels[indices[1]] = img.pixels[indices[0]]

def sym_horizontale():
    for x in range(250):
        for y in range(335):
            indices = [ x+y*width, (width-1-x)+y*width]
            
            img2.pixels[indices[0]]= img.pixels[indices[1]]
            img2.pixels[indices[1]] = img.pixels[indices[0]]

# Pourquoi ne pas essayer de faire une symétrique centrale ?

def sym_centrale():
    for x in range(250):
        for y in range(335):
            indices = [ x+y*width, (width-1-x)+(height-1-y)*width]
            
            img2.pixels[indices[0]]= img.pixels[indices[1]]
            img2.pixels[indices[1]] = img.pixels[indices[0]]
            
image(img2, 0, 0)
image(img, 0, 0, 63, 84)
