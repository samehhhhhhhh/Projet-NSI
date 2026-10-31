size(250,335)

img = loadImage("data/joconde.jpg")
#fonction qui permet d'appliquer un filtre gris sur une image

def gray_filter(i):
    img2 = createImage(250,335, RGB)

    for x in range(i.width):
        for y in range(i.height):
            
            index = x + y * i.width
            
            newColor = (red(i.pixels[index]) + green(i.pixels[index]) + blue(i.pixels[index])) / 3
            img2.pixels[index] = color(newColor, newColor, newColor)
            
    return img2
    

updatePixels()

image(gray_filter(img) , 0 , 0)
image(img, 0 , 0, 62, 83)
