size(310, 309)

img = loadImage("data/bruit.png")
img.loadPixels()

current = img
next_img = createImage(img.width, img.height, RGB)

def loc(x,y):
    return x + y * img.width

iterations = 3
seuil = 20

for n in range(iterations):
    print("Starting iteration", n+1)
    current.loadPixels()
    next_img.loadPixels()

    for i in range(len(current.pixels)):
        next_img.pixels[i] = current.pixels[i]

    for x in range(1,img.width-1):
        for y in range(1,img.height-1):

            liste = []

            for i in range(-1,2):
                for j in range(-1,2):
                    index = loc(x+i,y+j)
                    liste.append(red(current.pixels[index]))

            liste.sort()

            mediane = liste[4]

            index5 = loc(x,y)
            centre = red(current.pixels[index5])

            if abs(centre-mediane) > seuil:
                next_img.pixels[index5] = color(mediane,mediane,mediane)

    next_img.updatePixels()
    print("Finished iteration", n+1)

    temp = current
    current = next_img
    next_img = temp
    seuil+= 5

image(current,0,0)
image(img,0,0,92,90)
