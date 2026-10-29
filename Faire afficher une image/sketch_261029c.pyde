x = 1000
y = 1000
size(1000,1000)
img=loadImage("data/yumeko.jpg")

h = img.height
w = img.width

n = 4

for i in range(0,x,x/n):
    print(i)
    for j in range(0,y,y/n):
        image(img, i, j, x / n, y / n)
   
