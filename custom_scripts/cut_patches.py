from PIL import Image
import os 
import numpy as np
import cv2
from utils.image_utils import extract_bndbox_values
from utils.image_utils import extract_patches

import matplotlib.pyplot as plt 

# Specify the path of the XML file
xml_file = "inference/annotations/parking.xml"
full_image = Image.open("inference/images/parking.jpg")
output_dir = "inference/extracted_patches/"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
bndbox_values = extract_bndbox_values(xml_file)

# extract_patches(bndbox_values= bndbox_values,
#                 full_image=full_image,
#                 output_dir = output_dir)




#rotated_box_values = extract_polygon_box_values(xml_file)
# rotated_box_values = extract_rotated_box_values(xml_file)

# def crop_image(image, cx, cy, width, height, angle):
#     # Calculate the coordinates of the corners of the rotated rectangle
#     #((cx, cy), (width, height), angle ) = cv2.minAreaRect((cx, cy), (width, height), angle)
    
#     #rect = cv2.minAreaRect(((cx, cy), (width, height), angle))
#     box = cv2.boxPoints(((cx, cy), (width, height), angle +5))
#     box = np.int0(box)

#     # Get the minimum and maximum x and y coordinates of the rotated rectangle
#     xmin = np.min(box[:, 0])
#     xmax = np.max(box[:, 0])
#     ymin = np.min(box[:, 1])
#     ymax = np.max(box[:, 1])

#     # Crop the image based on the coordinates
#     #cropped_image = image[ymin:ymax, xmin:xmax]
#     patch = image.crop((xmin, ymin, xmax, ymax))

#     return patch

# for key in rotated_box_values:
#     values = rotated_box_values[key]
#     # cropped_image = crop_image(full_image, 
#     #                            values["x1"], values["x2"], values["y1"], values["y2"],
#     #                                values["x3"], values["x4"], values["y3"], values["y4"], )
#     cropped_image = crop_image(full_image,values["cx"], values["cy"], values["width"], 
#                                values["height"], values["rot"])
    
#     image_array = np.array(cropped_image)
#     # plt.imshow(image_array)
#     # plt.show()
#     resized_image = cv2.resize(image_array, (150, 150))
#     cv2.imwrite(f"{output_dir}{key}.jpg", resized_image)


