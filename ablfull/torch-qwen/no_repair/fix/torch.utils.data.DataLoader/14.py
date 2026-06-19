
import torch
from torch.utils.data import DataLoader
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3))
batch_size = 2
shuffle = True
num_workers = 0
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
