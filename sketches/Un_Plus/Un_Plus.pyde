matrix = [ [ -1, -1, -1 ],
           [ -1,  9, -1 ],
           [ -1, -1, -1 ] ]

"""
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

def convolution(x, y, matrix, img):
    rtotal = 0.0
    gtotal = 0.0
    btotal = 0.0
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            index=(x-i)+(y-j)*width
            rtotal=rtotal+red(img.pixels[index])*matrix[i+1][j+1]
            gtotal=gtotal+green(img.pixels[index])*matrix[i+1][j+1]
            btotal=btotal+blue(img.pixels[index])*matrix[i+1][j+1]
    rtotal = constrain(rtotal,0,255)
    gtotal = constrain(gtotal,0,255)
    btotal = constrain(btotal,0,255)
    return color(rtotal,gtotal,btotal)


def setup():
    global img
    size(408, 272)
    global img2
    img2=createImage(408,272,RGB)
    #print(matrix[2][2])
    frameRate(30)
    img = loadImage("data/joconde.png")
    for x in range(1,407):
        for y in range(1,271):
            index = x + y*width
            c = convolution(x,y,matrix,img)
            img2.pixels[index] = c
    #updatePixels()
    image(img2,0,0)
    image(img,0,0,102,68)
