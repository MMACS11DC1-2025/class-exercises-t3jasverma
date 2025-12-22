from PIL import Image

def is_green(r, g, b):
    if r >= 0 and r < 120 and g > 150 and g <= 255 and b >= 0 and b < 120:
        return True
    else:
        return False

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height
for i in range(width):
    for j in range(height):
        im_r = image_green[i, j][0]
        im_g = image_green[i, j][1]
        im_b = image_green[i, j][2]

        if is_green(im_r,im_g,im_b):
            beach = image_beach[i, j]
            xy= (i,j)
            image_output.putpixel(xy,beach)
image_output.save("5.1/output.png","png")