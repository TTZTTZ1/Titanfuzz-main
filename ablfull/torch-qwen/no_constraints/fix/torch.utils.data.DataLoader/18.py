import torch
from torch.utils.data import DataLoader, TensorDataset
data = torch.randn(100, 3, 256, 256)
dataset = TensorDataset(data)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)