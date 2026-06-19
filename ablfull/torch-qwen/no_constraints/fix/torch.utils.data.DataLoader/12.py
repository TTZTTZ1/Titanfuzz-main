import torch
from torch.utils.data import DataLoader
dataset = torch.randn(100, 3, 256, 256)
batch_size = 4
shuffle = True
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)