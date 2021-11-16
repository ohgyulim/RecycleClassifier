import torch
from torchvision import models
import os
import torchvision.transforms as transforms
from PIL import Image
from torch.utils.data import Dataset,DataLoader
import torch.nn as nn
 from camera import takePic
 import picamera as pic
 import time

def Result():
    num_class=4

    model=models.mobilenet_v2(pretrained=True)
    model.classifier=nn.Linear(1280,num_class)

    model.load_state_dict(torch.load('/home/pi/Desktop/MobileNet_cpu.pt'))


    trans_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((224,224)),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    class CustomDataSet(Dataset):

        def __init__(self, main_dir, transform):
            self.main_dir = main_dir
            self.transform = transform

            all_imgs = os.listdir(main_dir)
            self.total_imgs = sorted(all_imgs)

        def __len__(self):
            return len(self.total_imgs)

        def __getitem__(self, idx):
            
            img_loc = os.path.join(self.main_dir, self.total_imgs[idx])
            image = Image.open(img_loc).convert("RGB")
            tensor_image = self.transform(image)

            return tensor_image


     test_data = CustomDataSet(takePic(), transform=trans_test)
#    test_data = CustomDataSet('/home/pi/Desktop/image/', transform=trans_test)
    test_set = DataLoader(dataset = test_data, batch_size = 3)

    result =[]

    with torch.no_grad():
        result=[]
        for data in test_set:
            imgs = data
            pre_sum=0
            prediction=model(imgs)
            result.append(torch.argmax(prediction,1).tolist())
            
        print(result[0])

    return result[0]
