import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math

class WineDataset(Dataset):

    def __init__(self):
        xy=np.loadtxt('wine.csv',delimiter=",",skiprows=1)
        self.x = torch.from_numpy(xy[:, 1:])
        self.y = torch.from_numpy(xy[:,[0]])
        self.n_samples = xy.shape[0]
    def __getitem__(self,index):
        return self.x[index],self.y[index]

    def __len__(self):
        return self.n_samples

dataset = WineDataset()

#dataset display
#first_data =  dataset[0]

#features, labels = first_data

#print(features,labels)

dataloader =  DataLoader(dataset=dataset,batch_size=4,shuffle=True,num_workers=2)

#iterating through datasets
#dataiter = iter(dataloader)
#data = dataiter.next()
#features,labels = data
#print(features,labels)

#traning loop

num_epoch = 2
total_samples = len(dataset)
n_iterations =math.ceil (total_samples/4)
print(total_samples,n_iterations)

for epoch in range(num_epoch):
    for i,(input,labels) in enumerate(dataloader):
        #forward backward
        if (i+1) %5 == 0:
            print(f'epoch {epoch+1}/{num_epoch},step {i+1}/{n_iterations}, inputs {input.shape}')

torchvision.datasets.MNIST()

