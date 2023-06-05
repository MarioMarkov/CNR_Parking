#!/usr/bin/python3
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

im = cv2.imread('prediction_images/car.jpg')
resized_image = cv2.resize(im, (150, 150))
device = "cpu"
# Display the resized image in the console
# cv2.imshow('',resized_image)
# cv2.waitKey(0)

# cv2.imshow('Original Image', im)
# cv2.imshow('Resized Image', new_image)
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.RandomResizedCrop(224),
    transforms.ToTensor(),  # normalize to [0, 1]
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
]) 
# transforms = torch.nn.Sequential(
#     transforms.Resize([256]),
#     transforms.RandomResizedCrop([224]),
#     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
# )
# scripted_transforms = torch.jit.script(transforms)

img_path = "prediction_images/"
target_path = "splits/CNRParkAB/dummy.txt"

# New dimensions for resizing
# new_width = 150
# new_height = 150

# #Iterate over the images in the directory
# for filename in os.listdir(img_path):
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         # Read the image
#         image_path = os.path.join(img_path, filename)
#         image = cv2.imread(image_path)
#         # Resize the image
#         resized_image = cv2.resize(image, (new_width, new_height))
        
#         output_path = os.path.join(img_path, filename)
#         cv2.imwrite(output_path, resized_image)
        
test_dataset = Data(img_path, target_path, transform)
test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, \
                        num_workers=0, collate_fn=collate_fn)


#print(next(iter(test_loader)))
#imshow(test_loader)
net = mAlexNet()
net.load_state_dict(torch.load("model.pth"))
with torch.no_grad():
        for data in test_loader:
            images, labels = data
            labels = list(map(int, labels))
            labels = torch.Tensor(labels)
            #images = images.to(device)
            #image_data = np.transpose(images[0], (1, 2, 0))
            # plt.imshow(image_data)
            # plt.show()
            print("Label: " ,int(labels[0]))

            # # labels = labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            print("Predicted: ", int(predicted[0]))


