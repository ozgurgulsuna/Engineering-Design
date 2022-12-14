# Description: Generate a dataset of simple grayscale rectangles

# Import the necessary libraries
import random
from PIL import Image, ImageDraw
import pandas as pd

# Set the size of the image
width = 50
height = 50

# Create a list to store the coordinates of the rectangles
coordinates = []

# Generate 100 images
for i in range(100):
    # Create a new image
    image = Image.new("RGB", (width, height))

    # Set the rectangle's color
    rect_gray = random.randint(0,255)
    rect_color = (rect_gray, rect_gray, rect_gray)

    # Set the background color
    bg_gray = random.randint(rect_gray, 255)
    bg_color = (bg_gray, bg_gray, bg_gray)
    image.paste(bg_color, (0, 0, width, height))

    # Create a new drawing object
    draw = ImageDraw.Draw(image)

    # Set the coordinates of the rectangle
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    
    # Save the coordinates of the rectangle
    coordinates.append([x1, y1, x2, y2])

    # Draw the rectangle
    draw.rectangle((x1, y1, x2, y2), fill=rect_color)

    # Save the image with a different filename for each image
    image.save(f"dataset_img/simple_rectangle_sample_{i}.png")

# Save the coordinates of the rectangles in a csv file
pd.DataFrame(coordinates).to_csv('dataset.csv', index=False)

