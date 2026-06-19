import torch
from torch.utils.data import DataLoader, TensorDataset
data = torch.randn(10, 5)
dataset = TensorDataset(data)
batch_size = 2
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)