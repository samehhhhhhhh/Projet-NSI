size(692,507)

img = loadImage("data/parc.jpg")
img2 = createImage(img.width, img.height, RGB)

matrix = [[-1, -1, -1],
          [-1,  8, -1],
          [-1, -1, -1]]


def convolution(x,y,matrix,img):

    total = 0.0

    for i in range(-1,2):
        for j in range(-1,2):

            index = (x-i) + (y-j) * img.width
            pixel = img.pixels[index]
            gris = (red(pixel) + green(pixel) + blue(pixel)) / 3.0
            total += gris * matrix[i+1][j+1]

    total = constrain(abs(total),0,255)

    return color(total)


img.loadPixels()
img2.loadPixels()


for x in range(1,img.width-1):
    for y in range(1,img.height-1):

        index = x + y * img.width

        c = convolution(x,y,matrix,img)

        img2.pixels[index] = c

img2.updatePixels()


image(img2,0,0)
image(img,0,0,69,50)
