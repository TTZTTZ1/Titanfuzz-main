import torch
from torch.utils.data import DataLoader, TensorDataset
data = torch.randn(10, 3)
dataset = TensorDataset(data)
batch_size = 2
shuffle = False
num_workers = 0
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)