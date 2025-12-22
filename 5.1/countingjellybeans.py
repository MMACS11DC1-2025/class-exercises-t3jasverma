from PIL import Image

def get_color(r, g, b):
    
    r_norm = 1 if 170 <= r <= 255 else 0
    g_norm = 1 if 100 <= g <= 255 else 0
    b_norm = 1 if 170 <= b <= 255 else 0
    
    colors_map = {
        (1,0,0): "Red",
        (0,1,0): "Green",
        (0,0,1): "Blue",
        (1,1,1): "White",
        (0,0,0): "Black",
        (1,1,0): "Yellow",
        (1,0,1): "Purple",
    }
    
    normalized_rgb = (r_norm, g_norm, b_norm)
    
   
    return colors_map.get(normalized_rgb, "unknown")

file = Image.open("5.1/jelly_beans.jpg")
jbimg = file.load()
width, height = file.size

color_counts = {
    "Red": 0,
    "Yellow": 0,
    "Blue": 0,
    "Green": 0,
    "Purple": 0,
}

for x in range(width):
    for y in range(height):
        r, g, b = jbimg[x, y]
        color_name = get_color(r, g, b)
        if color_name in color_counts:
            color_counts[color_name] += 1

total_pixels = width * height
color_percentages = {}
for color, count in color_counts.items():
    color_percentages[color] = f"{round((count / total_pixels) * 100, 2)}%"

print(color_percentages)

