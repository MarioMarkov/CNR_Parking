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
    

img_path = "extracted_patches/"
predictions_path = "predicted_patches/"
data = DataInference(img_path,transform, target_path = None)
data_loader = DataLoader(data, batch_size=1, shuffle=False, \
                        num_workers=0, collate_fn=collate_fn)


net = AlexNet()
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
           


