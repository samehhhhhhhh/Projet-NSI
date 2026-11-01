def setup():
    global img
    size(250,335)
    img = loadImage("data/joconde.jpg")
    background(0,0,0)

def draw():
    x = int(random(width))
    y = int(random(height))
    
    index = x + y * width
    pixel = img.pixels[index]
    noStroke()
    fill(pixel,128)
    rect(x,y,10,10)
    
    
# le programme choisis un pixel au hasard prend sa couleur et remplis les 100 pixels autours avec la meme couleur
# on peut imaginer que si on met la taille du pinceau a un pixel, apres quelques minutes on se retrouve avec l'image de base
# plus le pinceau est gros plus on pert en precision

#fill(r,g,b,128) baisse l'opacite ce qui permet de superposer les cubes les un sur les autres et de fausser une precision
#tout en gardant la vitesse que nous donne la taille du pinceau

#ellipse nous permet de creer une elipse d'hauteur y et de largeur x, si x == y alors cela nous donne un cercle
