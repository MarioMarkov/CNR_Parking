from utils.image_utils import extract_bndbox_values
from PIL import Image
import numpy as np
import cv2
import torch
from utils.model import *
from torch.utils.data import DataLoader
from utils.dataloader import *
from torchvision import transforms
import matplotlib.pyplot as plt
import time 
# Full image 
image_file = "inference/images/pk_lot.jpg"
full_image = Image.open(image_file) 
image_to_draw = cv2.imread(image_file)

# Annotations
xml_file = "inference/annotations/pk_lot.xml"

# Get Bounding box values
bndbox_values = extract_bndbox_values(xml_file)
# Transformations
transform = transforms.Compose([
    transforms.Resize((224,224)),
    #transforms.RandomResizedCrop(224),
    transforms.ToTensor(),  # normalize to [0, 1]
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
]) 

model = AlexNet()
start_time = time.time()

# puc very good, 04 
model.load_state_dict(torch.load("model.pth",map_location=torch.device('cpu')))

for key in bndbox_values:
    values = bndbox_values[key]
    #Extract coordinates from the bounding box
    xmin= values["xmin"]
    ymin= values["ymin"]
    xmax= values["xmax"]
    ymax= values["ymax"]
    # Crop patch for thr image
    patch = full_image.crop((xmin, ymin, xmax, ymax))
    #resized_image = cv2.resize(image_array, (150, 150))
    #img = Image.open(patch)
    img = transform(patch)
    
    # Adding batch dimension
    img = img[None, :]
    
    # image_to_show = np.transpose(np.array(img[0]),(1, 2, 0))
    # plt.imshow(image_to_show)
    # plt.show()
    
    is_busy = model.predict(img)
    
    if(is_busy == 1):
        # Busy 1 Red
        cv2.rectangle(image_to_draw, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 2)

    else:
        # Free 0 green
        cv2.rectangle(image_to_draw, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)

print("Execution time: %s seconds" % (time.time() - start_time))

cv2.imwrite("image_with_boxes.jpg", image_to_draw)


    