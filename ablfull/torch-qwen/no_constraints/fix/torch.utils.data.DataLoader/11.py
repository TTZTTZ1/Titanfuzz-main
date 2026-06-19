import torch
from torch.utils.data import DataLoader
dataset = torch.randn(100, 10)
batch_size = 5
shuffle = True
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)