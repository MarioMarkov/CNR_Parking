import torch
import os
from PIL import Image

def collate_fn(batch):
    batch = list(filter(lambda x: x is not None, batch))
    return torch.utils.data.default_collate(batch)

class DataInference:
    def __init__(self, img_path, transforms = None, target_path= None):
        self.transforms = transforms
        if target_path is None:
            self.img_list= [os.path.join(img_path, i) for i in os.listdir(img_path)] 
        else:
            with open(target_path, 'r') as f:
                lines = f.readlines()
                self.img_list = [os.path.join(img_path, i.split()[0]) for i in lines]
                self.label_list = [i.split()[1] for i in lines]
        
    def __getitem__(self, index):
        img_path = self.img_list[index]
        img = Image.open(img_path)
        img = self.transforms(img)
        if  hasattr(self, 'label_list'):
            label = self.label_list[index]
            return img, img_path, label 
        return img, img_path

    def __len__(self):
        return len(self.img_list)


class Data:
    def __init__(self, img_path, target_path, transforms = None):
        with open(target_path, 'r') as f:
            lines = f.readlines()
            self.img_list = [os.path.join(img_path, i.split()[0]) for i in lines]
            self.label_list = [i.split()[1] for i in lines]
            self.transforms = transforms
    
    def __getitem__(self, index):
        try:
            img_path = self.img_list[index]
            img = Image.open(img_path)
            img = self.transforms(img)
            label = self.label_list[index]
        except:
            return None
        return img, label
    
    def __len__(self):
        return len(self.label_list)