from PIL import Image
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

def is_rust(pixel):
    r, g, b = pixel
    #colour thresholds for rust
    if r >= 120 and r <= 255 and \
       g >= 60 and g <= 160 and \
       b >= 0 and b <= 90 and \
       r > g and g > b:
        return True
    else:
        return False

# main program
image_scores = []
# start timing
start = time.time()
# loop through images
for img in image_files:
    print("Processing:", img)
    
    # Open the image (assuming the file exists))
    image = Image.open(f"{folder}/{img}")
    image = image.convert("RGB")
    width, height = image.size
    total_pixels = width * height
    rust_pixel_count = 0

    #Count the rust pixels
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if is_rust((r, g, b)):
                rust_pixel_count += 1    
    rust_percent = rust_pixel_count / total_pixels * 100
    image_scores.append([img, rust_percent])

# end timing
end = time.time()
print(f"\nProcessing time: {end - start:.3f} seconds")

#Selection Sort to sort images by rust % (descending)
for i in range(len(image_scores)):
    # Track the largest score found so far in the unsorted section
    largest_score = image_scores[i][1]
    largest_index = i
    for j in range(i + 1, len(image_scores)):
        # Compare current item's score with our tracked largest
        if image_scores[j][1] > largest_score:
            largest_score = image_scores[j][1]
            largest_index = j
    # Swap the found largest item with the item at position i
    image_scores[largest_index], image_scores[i] = image_scores[i], image_scores[largest_index]

# print top 5 images
print("\nTop images:")
for i in range(min(5, len(image_scores))):
    print(image_scores[i][0], "-", round(image_scores[i][1], 2), "%")

# Binary Search for user-input rust %
query = input("\nEnter rust % to find (or skip): ")
if query != "":
    target = float(query)
    found = False
    first = 0
    last = len(image_scores) - 1
    tol = 0.01

    while first <= last:
        mid = (first + last) // 2
        mid_value = image_scores[mid][1]
        # Check if we found the value (within tolerance)
        if abs(mid_value - target) <= tol:
            print("Found:", image_scores[mid][0], "-", round(mid_value, 2), "%")
            found = True
            break
        # If mid_value is less than target, target must be to the LEFT (lower index)
        elif mid_value < target:
            last = mid - 1
        # If mid_value is greater than target, target must be to the RIGHT (higher index)
        else: 
            first = mid + 1
    if not found:
        print("No match")