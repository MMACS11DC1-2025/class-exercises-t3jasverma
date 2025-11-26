from PIL import Image


def is_light(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    average = int((r+g+b)/3)
    return average >=128
white_pixel = (255,255,255)
print(is_light(white_pixel))
print(is_light((255,255,255)))

my_image = Image.open("5.1/kid-green.jpg").load()
output_image = Image.open("5.1/kid-green.jpg")

width = output_image.width
height = output_image.height
for i in range(width):
    for j in range(height):
        if is_light(my_image[i,j]):
            output_image.putpixel((i,j),(255,255,255))
        else:
            output_image.putpixel((i,j),(0,0,0))
output_image.save("5.1/output_light.png","png")