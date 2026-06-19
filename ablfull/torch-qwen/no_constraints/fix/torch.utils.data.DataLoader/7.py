import torch
from torch.utils.data import DataLoader
dataset = torch.randn(100, 3, 224, 224)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)