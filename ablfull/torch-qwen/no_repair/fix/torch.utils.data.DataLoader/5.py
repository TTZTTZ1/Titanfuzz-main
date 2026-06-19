
import torch
from torch.utils.data import DataLoader
dataset = torch.randn(10, 3)
dataloader = DataLoader(dataset, batch_size=2, shuffle=False)
