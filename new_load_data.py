import torch
from torchvision import datasets, transforms, TensorDataset
import os 

transforms = torch.nn.Sequential(
    transforms.Resize([256]),
    transforms.RandomResizedCrop([224]),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
)

scripted_transforms = torch.jit.script(transforms)
target_path = "splits/CNRParkAB/dummy.txt"
input_path = "prediction_images/"

class SimpleCustomBatch:
    def __init__(self, data):
        transposed_data = list(zip(*data))
        self.inp = torch.stack(transposed_data[0], 0)
        self.tgt = torch.stack(transposed_data[1], 0)

    # custom memory pinning method on custom type
    def pin_memory(self):
        self.inp = self.inp.pin_memory()
        self.tgt = self.tgt.pin_memory()
        return self

with open(target_path, 'r') as f:
    lines = f.readlines()
    img_list = [os.path.join(input_path, i.split()[0]) for i in lines]
    label_list = [i.split()[1] for i in lines]

print(img_list)
print(label_list)

inps = torch.arange(10 * 5, dtype=torch.float32).view(10, 5)
tgts = torch.arange(10 * 5, dtype=torch.float32).view(10, 5)

dataset = TensorDataset(inps, tgts)


# def collate_wrapper(batch):
#     return SimpleCustomBatch(batch)
