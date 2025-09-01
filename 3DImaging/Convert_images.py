from PIL import Image
import os

#NEEDS PNGS - 3rd

# Define the paths
input_directory = 'F:/Test/test-masks/'
output_directory = 'F:/Corrected_masks/'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through the files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png"):
        # Open the image
        image = Image.open(os.path.join(input_directory, filename))

        # Convert the image to the range 0-1
        image = image.convert('L')  # Convert to grayscale
        image = image.point(lambda p: p / 255)  # Normalize pixel values to 0-1

        # Save the normalized image to the output directory
        image.save(os.path.join(output_directory, filename))
