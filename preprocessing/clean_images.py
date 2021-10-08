import os
from PIL import Image
from PIL.ExifTags import TAGS
import logging


logging.basicConfig(
    filename='preprocessing/preprocessing.log', level=logging.DEBUG)

isLoading = True
path = 'data/'

pathlists = []

for root, dirs, files in os.walk(path):
    for dir in dirs:
        pathlists.append(os.path.join(dir))

for pathlist in pathlists:
    baseFile = path + pathlist
    for filename in os.listdir(baseFile):
        image_filename = f"{baseFile}/{filename}"
        image_file = open(image_filename, "rb")
        image_type = filename.split('.')

        # Check if file extension is JPG or PNG
        if image_type[1] == 'png' or image_type[1] == 'jpg':
            image = Image.open(image_file)
            if image.getexif():
                data = list(image.getdata())
                mode = image.mode
                size = image.size
                os.remove(image_filename)
                image_without_exif = Image.new(image.mode, image.size)
                image_without_exif.putdata(data)
                image_without_exif.save(image_filename)
                print(f"{image_filename} metadata cleaned")
    print(f'{pathlist} clean meta done\n')
