import torch
from torch.utils.data import DataLoader
dataset = torch.randn(100, 3, 224, 224)
batch_size = 16
shuffle = True
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)