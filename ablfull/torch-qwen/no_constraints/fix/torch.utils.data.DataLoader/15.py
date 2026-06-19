import torch
from torch.utils.data import DataLoader
dataset = torch.rand(10, 5)
batch_size = 2
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)