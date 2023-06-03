import cv2
from PIL import Image
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import numpy as np

def extract_bndbox_values(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    bndbox_values = []

    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        xmin = float(bndbox.find('xmin').text)
        ymin = float(bndbox.find('ymin').text)
        xmax = float(bndbox.find('xmax').text)
        ymax = float(bndbox.find('ymax').text)
        bndbox_values.append((xmin, ymin, xmax, ymax))

    return bndbox_values

# Specify the path of the XML file
xml_file = "parking.xml"

# Extract the bounding box values
bndbox_values = extract_bndbox_values(xml_file)

image_cv = cv2.imread("parking.jpg")
image_image = Image.open("parking.jpg")

# Print the bounding box values
for bndbox in bndbox_values:
    # Extract coordinates from the bounding box
    xmin, ymin, xmax, ymax = bndbox
    
    # Draw rectangles over image
    cv2.rectangle(image_cv, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
    
    # Crop patch for thr image
    cropped_image = image_image.crop((xmin, ymin, xmax, ymax))
    
    # Convert the PIL Image to NumPy ndarray
    image_array = np.array(cropped_image)
    resized_image = cv2.resize(image_array, (150, 150))
    
    
cv2.imwrite("image_with_boxes.jpg", image_cv)


# for patch in patches:
#     x, y, w, h = patch
#   cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  
    #image2 = Image.open("parking.jpg")
    # left = x
    # top = y
    # right = x + w
    # bottom = y + h
    # cropped_image = image2.crop((left, top, right, bottom))
    # cropped_image.show()

#cv2.imwrite("image_with_boxes.jpg", image)



