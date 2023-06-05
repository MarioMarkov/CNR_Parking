import xml.etree.ElementTree as ET
from PIL import Image
import os 
import numpy as np
import cv2
def extract_bndbox_values(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    bndbox_values = []

    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        name = obj.find('name').text

        xmin = float(bndbox.find('xmin').text)
        ymin = float(bndbox.find('ymin').text)
        xmax = float(bndbox.find('xmax').text)
        ymax = float(bndbox.find('ymax').text)
        bndbox_values.append((xmin, ymin, xmax, ymax,name))

    return bndbox_values

# Specify the path of the XML file
xml_file = "parking.xml"
full_image = Image.open("parking.jpg")
output_dir = "extracted_patches/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Extract the bounding box values
bndbox_values = extract_bndbox_values(xml_file)

# if os.path.exists(output_dir):
#     os.remove(output_dir) #Operation not permitted: 'extracted_patches'
for value in bndbox_values:
    xmin, ymin, xmax, ymax, name = value
     #Extract coordinates from the bounding box
    # Crop patch for thr image
    patch = full_image.crop((xmin, ymin, xmax, ymax))
    image_array = np.array(patch)
    resized_image = cv2.resize(image_array, (150, 150))
    cv2.imwrite(f"{output_dir}{name}.jpg", resized_image)
    #resized_image.save()


