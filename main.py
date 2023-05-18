# Import the Images module from pillow
from PIL import Image, ImageCms
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Open the image by specifying the image path.
output_folder = "compressed/"
for image_path in files:
    if ".jpg" not in image_path:
        continue
    image_file = Image.open(image_path)
    profile = ImageCms.createProfile("sRGB")
    print("Compressing: " + image_path)
    image_file.save(output_folder + image_path, quality=25, icc_profile=ImageCms.ImageCmsProfile(profile).tobytes())