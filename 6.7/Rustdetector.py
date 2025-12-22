from PIL import Image
import colorsys
import time

folder = "6.7/images"

# hardcoded list of image files
image_files = [
    "Rust1.jpeg",
    "Rust2.jpg",
    "Rust3.jpeg",
    "Rust4.jpg",
    "Rust5.jpeg",
    "Rust6.jpg",
    "Rust7.png",
    "Rust8.jpg",
    "Rust9.jpg",
    "Rust10.jpg"
]

# This function checks if a pixel is rust. It filters out colors 
# that aren't red-dominant first, then uses HSV to check if the color 
# falls in the specific orange-brown range. 
# It serves as the primary detection logic for the program.
def is_target_feature(pixel):
    r, g, b = pixel
    
    # Check for red dominance and minimum brightness
    if r < 80 or r < g or r < b:
        return False
    
    rh, gh, bh = r/255.0, g/255.0, b/255.0
    h, s, v = colorsys.rgb_to_hsv(rh, gh, bh)
    
    # Final check against the known rust hue range
    return 0.02 <= h <= 0.12 and s >= 0.3 and v >= 0.15

# This goes through the list of images, resizes them to 800px 
# to save time, and calculates the rust percentage for each one.
# It uses .load() for fast pixel access to optimize processing speed.
def get_all_scores():
    # main program
    image_scores = []
    # start timing
    start = time.time()

    # Process each image
    for img in image_files:
        print("Processing: " + img)
        image = Image.open(folder + "/" + img).convert("RGB")
        
        # Downscaling to optimize performance
        image.thumbnail((800, 800))
        
        width, height = image.size
        total_pixels = width * height
        rust_pixels = 0

        # Pixel analysis
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                if is_target_feature(pixels[x, y]):
                    rust_pixels += 1

        # Calculate rust percentage and store to list
        rust_percent = rust_pixels / total_pixels * 100
        image_scores.append([img, rust_percent])

    end = time.time()
    print("\nProcessing time: " + str(round(end - start, 3)) + " seconds")
    return image_scores

# This sorts the list from highest score to lowest using 
# Selection Sort. It finds the biggest value and swaps it to the front.
# This ensures the most "at risk" images are presented first.
def sort_my_list(image_scores):
    # Selection sort (descending by rust %)
    for i in range(len(image_scores)):
        largest_index = i
        for j in range(i + 1, len(image_scores)):
            if image_scores[j][1] > image_scores[largest_index][1]:
                largest_index = j
        image_scores[i], image_scores[largest_index] = image_scores[largest_index], image_scores[i]

# This searches the sorted list for a specific score. It 
# splits the list in half over and over until it finds the target.
# It uses a small tolerance (tol) to handle floating point comparisons.
def search_for_rust(image_scores):
    # Binary search for user-input rust %
    query = input("\nEnter rust % to find (or skip): ")
    if query != "":
        target = float(query)
        first = 0
        last = len(image_scores) - 1
        tol = 0.01
        found = False

        while first <= last:
            mid = (first + last) // 2
            mid_value = image_scores[mid][1]

            if abs(mid_value - target) <= tol:
                print("Found: " + image_scores[mid][0] + " - " + str(round(mid_value, 2)) + "%")
                found = True
                break
            elif mid_value < target:
                last = mid - 1
            else:
                first = mid + 1

        if not found:
            print("No match")

# Execute program

# Run analysis
master_list = get_all_scores()

# Sort results
sort_my_list(master_list)

# Print top 5 images
print("\nTop images:")
for i in range(min(5, len(master_list))):
    print(master_list[i][0] + " - " + str(round(master_list[i][1], 2)) + "%")

# Run search
search_for_rust(master_list)