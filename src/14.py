
import py5



"""
    Ce programme semble diviser la fenêtre en cellules de 2 pixel de coté,

    Ensuite, en fonction de la position de la souris, 
    sur l'axe x et la luminosité du pixel surlequel on se trouve,
    on aura les coordonées z du pixel, qui seront ensuite données 
    
    à processing afin d'avoir un effet de perspective (3D)

"""

cellsize = 2 # Dimensions of each cell in the grid

def setup():
    global img, cols, rows, cellsize
    py5.size(480, 638, py5.P3D)
    img  = py5.load_image("../assets/sunflower.jpg")  # Load the source image
    cols = py5.width//cellsize             # Calculate number of columns
    rows = py5.height//cellsize            # Calculate number of rows

def draw():
    global img, cols, rows, cellsize

    py5.background(0)
    py5.load_pixels()
    # Begin loop for columns
    for i in range(cols):
        # Begin loop for rows
        for j in range(rows):
            x = i*cellsize + cellsize//2  # x position
            y = j*cellsize + cellsize//2  # y position
            loc = x + y*py5.width            # Pixel array location
            c = img.pixels[loc]          # Grab the color
            # Calculate a z position as a function of mouseX and pixel brightness
            z = (py5.mouse_x/(float(py5.width))) * py5.brightness(img.pixels[loc]) - 100.0
            # Translate to the location, set fill and stroke, and draw the rect
            py5.push_matrix()
            py5.translate(x,y,z)
            py5.fill(c)
            py5.no_stroke()
            py5.rect_mode(py5.CENTER)
            py5.rect(0,0,cellsize,cellsize)
            py5.pop_matrix()

py5.run_sketch()