


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

        r = -reds[1] - reds[3] + 5*reds[4] - reds[5] - reds[7]
        g = -greens[1] - greens[3] + 5*greens[4] - greens[5] - greens[7]
        b = -blues[1] - blues[3] + 5*blues[4] - blues[5] - blues[7]

        index = loc(x, y)
        img2.pixels[indices[4]] = color(r, g, b)


image(img2, 0, 0)
image(img, 0, 0, 63, 84)
