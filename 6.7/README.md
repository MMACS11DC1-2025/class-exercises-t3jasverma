# Project: Infrastructure Rust Detection

## Project Overview

This project looks at detecting rust and corrosion on metal infrastructure using image analysis. By scanning the pixels in each image, the program calculates a **Feature Density Score**, which is the percentage of pixels identified as rust. This score gives a rough idea of how much corrosion is present and can be used to compare images or flag areas that may need closer inspection.

## Feature Identification

The program identifies rust using a simple but effective two-step color check:

1. **Red dominance and brightness check:** Rust usually appears more red than green or blue, so the program first checks if the red value is the strongest channel and makes sure the pixel is not too dark. This helps remove shadows and unrelated dark areas.
2. **HSV color check:** After that, the pixel is converted from RGB to HSV. HSV makes it easier to focus on color rather than lighting, which helps when images are taken under different conditions. The program then checks if the pixel’s hue falls in the orange-brown range that rust typically shows.

Using both checks together makes the detection more reliable than using RGB values alone.

## Performance and Profiling

* **Optimization:** The program was originally slow when processing full-size images. To fix this, the images are resized using `image.thumbnail((800, 800))`, which reduced the total runtime for 10 images from over 10 seconds to around 3 seconds.
* **Bottleneck:** The slowest part of the program is the nested loop that checks every pixel in each image.
* **Efficiency:** Selection Sort and Binary Search run very quickly because they only work on a small list of image scores.

## Testing and Validation

* **Detection testing:** Images of blue sky and grey concrete were tested to make sure they were not incorrectly detected as rust, resulting in scores close to 0%.
* **Sorting:** The Selection Sort was checked to confirm that images with higher rust percentages appear at the top of the list.
* **Searching:** Binary Search was tested using known rust percentages, with a small tolerance to handle rounding errors.

## Challenges

* **Slow runtime:** Large image sizes caused long processing times at first. Resizing the images was the most effective solution.
* **Floating-point values:** Searching for exact percentage values was unreliable because of decimals, so a tolerance was added.
* **False positives:** Some dark shadows were counted as rust early on. Adding a minimum brightness check reduced this issue.

## Limitations

* **Painted surfaces:** Orange or brown paint can sometimes be mistaken for rust since the colors are similar.
* **Lighting:** Strong reflections or glare can wash out rust colors, causing the program to miss some areas.

## Future Improvements

A possible improvement would be adding a texture-based check. Rusted metal is usually rough, while painted metal is smoother. Looking at how much nearby pixel values change could help tell the difference.

## Real-World Use

This type of program could be used to scan drone images of bridges or other metal structures. Instead of manually checking every photo, inspectors could focus on the images with higher rust scores, saving time and effort.
