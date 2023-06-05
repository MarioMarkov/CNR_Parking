from PIL import Image
import os 
import numpy as np
import cv2
from utils.image_utils import extract_bndbox_values
from utils.image_utils import extract_rotated_box_values
from utils.image_utils import crop_rotated_box
import matplotlib.pyplot as plt 
import math
# Specify the path of the XML file
xml_file = "parking2_id.xml"
full_image = Image.open("parking2.jpg")
output_dir = "extracted_patches2/"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
bndbox_values = extract_bndbox_values(xml_file)

for key in bndbox_values:
    values = bndbox_values[key]
    cropped_image = full_image.crop((values["xmin"], values["ymin"],
                                    values["xmax"], values["ymax"]))
    image_array = np.array(cropped_image)
    resized_image = cv2.resize(image_array, (150, 150))
    # plt.imshow(resized_image)
    # plt.show()
    cv2.imwrite(f"{output_dir}{key}.jpg", resized_image)


    
    
    
    
# Extract the bounding box values
# bndbox_values = extract_bndbox_values(xml_file)


# for value in bndbox_values:
#        values = rotated_box_values[key]
#     xmin =  values["xmin"]
    # ymin= values["ymin"]
    # xmax= values["xmax"]
    # ymax= values["ymax"]
    # name = value

#      #Extract coordinates from the bounding box
#     # Crop patch for thr image
#     patch = full_image.crop((xmin, ymin, xmax, ymax))
#     image_array = np.array(patch)
#     resized_image = cv2.resize(image_array, (150, 150))
#     cv2.imwrite(f"{output_dir}{name}.jpg", resized_image)
#     #resized_image.save()


