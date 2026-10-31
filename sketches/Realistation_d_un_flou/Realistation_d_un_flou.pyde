size(250, 335)

img = loadImage("data/joconde.jpg")
img2 = createImage(250,335, RGB)

def loc(x, y):
    return x + y * width

Lr = [red(i) for i in img.pixels]
Lg = [green(i) for i in img.pixels]
Lb = [blue(i) for i in img.pixels]

for x in range(1, width - 1):
    for y in range(1, height - 1):
        indices = [
            loc(x-1, y-1), loc(x, y-1), loc(x+1, y-1),
            loc(x-1, y),   loc(x, y),   loc(x+1, y),
            loc(x-1, y+1), loc(x, y+1), loc(x+1, y+1)
        ]

        reds = [Lr[i] for i in indices]
        greens = [Lg[i] for i in indices]
        blues = [Lb[i] for i in indices]
        
        r = 0
        g = 0
        b = 0
        for rr in reds:
            r += rr
        for gg in greens:
            g += gg
        for bb in blues:
            b += bb
        r/=9
        g/=9
        b/=9
        
        for indice in indices:
            img2.pixels[indice] = color(r,g,b)
            
image(img2, 0, 0)
image(img, 0, 0, 63, 84)
