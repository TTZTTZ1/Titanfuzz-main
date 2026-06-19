import torch
from torch.utils.data import DataLoader
dataset = torch.randn(100, 10)
dataloader = DataLoader(dataset, batch_size=5)