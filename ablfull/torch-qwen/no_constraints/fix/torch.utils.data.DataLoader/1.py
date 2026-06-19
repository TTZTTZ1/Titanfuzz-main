import torch
from torch.utils.data import DataLoader
dataset = torch.utils.data.TensorDataset(torch.randn(10, 5))
batch_size = 2
shuffle = True
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)