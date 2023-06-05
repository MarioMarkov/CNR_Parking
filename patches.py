import cv2
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import numpy as np
import os
from utils.model import *
from utils.dataloader import *
import matplotlib 
import torch
import argparse
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
from utils.imshow import imshow
import cv2
from matplotlib import pyplot as plt
import numpy as np
transform = transforms.Compose([
    transforms.Resize(224),
    #transforms.RandomResizedCrop(224),
    transforms.ToTensor(),  # normalize to [0, 1]
    #transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
]) 



def show_image(image,image_path):
    image_data = np.transpose(image[0], (1, 2, 0))
    plt.imshow(image_data)
    plt.title(image_path)
    plt.show()
    


image_cv = cv2.imread("parking.jpg")
output_dir = "extracted_patches/"

img_path = "extracted_patches/"
predictions_path = "predicted_patches/"
targets_path = "splits/CNRParkAB/dummy2.txt"
data = Data(img_path,transform, target_path = None)
data_loader = DataLoader(data, batch_size=1, shuffle=False, \
                        num_workers=0, collate_fn=collate_fn)
net = mAlexNet()
net.load_state_dict(torch.load("model.pth"))

if os.path.exists('predictions.txt'):
    os.remove('predictions.txt')


# Get the predictions for each image and write it to a file
with torch.no_grad():
        for data, data2 in zip(data_loader,data):
            image, img_path = data
            #show_image(image,img_path)
            output = net(image)
            _, predicted = torch.max(output.data, 1)
            pred = int(predicted[0])
            print("Predicted: ", pred)
            
            with open('predictions.txt', 'a') as file:
                file.write(f'{img_path[0]} {pred}\n')
            #images = images.to(device)
            #image_data = np.transpose(images[0], (1, 2, 0))
            # plt.imshow(image_data)
            # plt.show()
           
# Go through the predictions file and fill the bounding boxes









# Print the bounding box values
# with torch.no_grad():
#     for i, bndbox in enumerate(bndbox_values):
#         # Extract coordinates from the bounding box
#         xmin, ymin, xmax, ymax, name = bndbox
#         # Crop patch for thr image
#         cropped_image = image_image.crop((xmin, ymin, xmax, ymax))
        
#         # Convert the PIL Image to NumPy ndarray
#         image_array = np.array(cropped_image)
#         resized_image = cv2.resize(image_array, (150, 150))
        
#         test_dataset = Data(output_dir + f"spot-{i}.jpg", target_path, transform)
        
#         test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, \
#                         num_workers=0, collate_fn=collate_fn)
#         # for data in test_loader:
#         #     images, labels = data
#         #     outputs = net(images)
#         #     _, predicted = torch.max(outputs.data, 1)
#         #     print("Predicted: ", int(predicted[0]))
#         # Draw rectangles over image
#         if(name == "busy"):
#             cv2.rectangle(image_cv, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
#         else:
#             cv2.rectangle(image_cv, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 2)

    
        #cv2.imwrite(output_dir + f"spot-{i}.jpg", resized_image)

    
    
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



