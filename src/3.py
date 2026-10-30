 

import py5

# Taille de la fenêtre
x = 1000
y = 1000

def settings():
    
    py5.size(x, y)


def setup():

    img=py5.load_image("../assets/yumeko.jpg")

    h = img.height
    w = img.width

    n = 4

    for i in range(0, x , x//n ):

        print(i)
        
        for j in range(0 , y , y//n ):
            py5.image(img, i, j, x / n, y / n)

py5.run_sketch()