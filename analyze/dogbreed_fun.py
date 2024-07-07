from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import torch.nn as nn
import torch
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def classify_dogbreed(img_path, crop = False, xmin = None, ymin = None, xmax = None, ymax = None, test_mode = False):
    '''
    classify the dog breed of the image (or the most similar dog breed if the image is not a dog)
    :param img_path: path to image to classify
    :return: most likely dog breed
    '''

    with open(img_path, 'rb') as f:
        image = Image.open(f).convert("RGB")

    # load the model
    model_path = os.path.abspath(os.path.join('analyze','dog_breed_classifier.pth'))
    print('---------------',model_path)
    model = torch.load(model_path)
    model.eval()
    label_path = os.path.abspath(os.path.join('analyze','dog_labels.npy'))

    all_labels = np.load(label_path)
    if crop:
        image = image.crop((xmin, ymin, xmax, ymax))

    transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    image = transform(image).unsqueeze(0)

    #display image
    outputs = model.forward(image)
    _, predicted = torch.max(outputs, 1)
    predicted = predicted.cpu().numpy()
    predicted = predicted.astype(int)
    predicted_breed = all_labels[predicted]
    #top 5 most likely classes
    _, top5 = outputs.topk(5)
    top5 = top5.cpu().numpy()
    top5 = top5.astype(int)
    top5_breeds = all_labels[top5]

    if test_mode:
        plt.imshow(image.squeeze(0).permute(1, 2, 0).cpu().numpy())
        plt.show()
        print(predicted_breed)
        print(top5_breeds)
    else: 
        return predicted_breed

