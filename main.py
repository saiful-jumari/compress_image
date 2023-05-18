# Import the Images module from pillow
from PIL import Image, ImageCms
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Open the image by specifying the image path by iterating through files
output_folder = "compressed/"
for image_filename in files:
    if ".jpg" not in image_filename:
        continue

    image_file = Image.open(image_filename)
    profile = ImageCms.createProfile("sRGB")
    print("Compressing: " + image_filename)
    image_file.save(output_folder + image_filename, quality=25, icc_profile=ImageCms.ImageCmsProfile(profile).tobytes())