import turtle
import random

# Colour schemes
color_schemes = {
    "1": {
        "name": "Winter Night",
        "bg": "#0b132b",
        "colors": ["#1c2541", "#3a506b", "#5bc0be", "#a9d6e5"]
    },
    "2": {
        "name": "Sunset",
        "bg": "#ff7b00",
        "colors": ["#ff9500", "#ffb627", "#ffd670", "#ffeecf"]
    },
    "3": {
        "name": "Ocean",
        "bg": "#001d3d",
        "colors": ["#003566", "#0077b6", "#00b4d8", "#90e0ef"]
    },
    "4": {
        "name": "Forest",
        "bg": "#081c15",
        "colors": ["#1b4332", "#2d6a4f", "#40916c", "#95d5b2"]
    },
    "5": {
        "name": "Lava",
        "bg": "#1a0000",
        "colors": ["#660000", "#cc3300", "#ff6600", "#ffcc00"]
    },
    "6": {
        "name": "Custom",
        "bg": None,
        "colors": None
    }
}

print("Welcome to the Koch Snowflake Generator!")

# Recursion depth input
try:
    depth = int(input("Enter recursion depth (0-5 recommended): "))
    if depth < 0:
        depth = 3
except:
    depth = 3

# Colour scheme selection
print("\nChoose a color scheme:")
for key in color_schemes:
    scheme = color_schemes[key]
    print(key + ". " + scheme["name"])

choice = input("Enter number (1–6): ").strip()
if choice not in color_schemes:
    choice = "1"

selected = color_schemes[choice]

# Custom colors (limit of 3 colors)
if choice == "6":
    print("\nCreate your custom color palette (up to 3 colors)!")

    bg_color = input("Enter your background color (name or hex, e.g. black or #000000): ").strip() or "black"

    fg_colors = []
    while len(fg_colors) < 3:
        color_input = input("Add color " + str(len(fg_colors)+1) + " for the snowflake: ").strip()
        if color_input:
            fg_colors.append(color_input)
        if len(fg_colors) == 3:
            break
        more = input("Add another color? (y/n): ").lower()
        if more != "y":
            break

    if not fg_colors:
        fg_colors = ["white"]

    print("\nYour custom palette:")
    print("Background:", bg_color)
    print("Colors:", fg_colors)
else:
    fg_colors = selected["colors"]
    bg_color = selected["bg"]

# Line thickness
try:
    line_size = int(input("\nEnter line thickness (1-10 recommended): "))
    if line_size < 1:
        line_size = 2
except:
    line_size = 2

# Show drawing live
show_drawing = input("\nDo you want to see the turtle drawing live? (yes/no): ").strip().lower() in ["yes", "y"]

# Fractal settings
fractal_settings = {
    "snowflake": {
        "colors": fg_colors,
        "bg": bg_color,
        "angle": 60,
        "length": 300
    }
}

# Recursive Koch curve
def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
        return 1
    length /= 3.0
    calls = 0
    calls += koch_curve(t, length, level - 1)
    t.left(60)
    calls += koch_curve(t, length, level - 1)
    t.right(120)
    calls += koch_curve(t, length, level - 1)
    t.left(60)
    calls += koch_curve(t, length, level - 1)
    return calls

# Draw full snowflake
def draw_snowflake(level):
    settings = fractal_settings["snowflake"]
    screen = turtle.Screen()
    screen.bgcolor(settings["bg"])

    if not show_drawing:
        screen.tracer(0)

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(line_size)

    t.penup()
    t.goto(-settings["length"] / 2, settings["length"] / 3)
    t.pendown()

    total_calls = 0
    color_count = len(settings["colors"])
    for i in range(3):
        t.color(settings["colors"][i % color_count])  # pick color in order
        total_calls += koch_curve(t, settings["length"], level)
        t.right(120)

    t.hideturtle()
    if not show_drawing:
        screen.update()

    return total_calls

# Run program
print("\nDrawing fractal snowflake...")
total_calls = draw_snowflake(depth)
print("\nDepth:", depth)
print("Color scheme:", selected["name"])
print("Line thickness:", line_size)
print("Total recursive calls:", total_calls)
print("Done! Re-run to try different values.")
